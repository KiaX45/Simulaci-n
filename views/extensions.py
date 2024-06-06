import flet as ft
from logic.ordenar import Ordenamiento

class OrdenarElementos(ft.UserControl):
    def _init_(self, page, darkmode: bool = True):
        super()._init_()

        self.page = page
        self.darkmode = darkmode
        self.lista_extensiones = [["Documentos", ".docx"], ["Presentaciones", ".pptx"], ["PDF", ".pdf"], ["Imagenes", ".png"]]

        self.page.window_maximized = True
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.padding = 0
        self.page.bgcolor = "#2A363B" if self.darkmode else "#F4F4F4"
        self.page.vertical_alignment = "center"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK if self.darkmode else ft.ThemeMode.LIGHT

        self.image = ft.Image(
            src='https://www.udenar.edu.co/recursos/wp-content/uploads/2021/09/logo-udenar-blanco.png',
            width=100,
            height=100,
            fit='contain'
        )

        self.cTitle_text = ft.Text(
            'ORDENAR ELEMENTOS',
            size=40,
            font_family="georgia",
            color="#FECEA8" if self.darkmode else "black"
        )

        self.text_container = ft.Container(
            self.cTitle_text,
            alignment=ft.alignment.center
        )

        self.cTitle = ft.Container(
            ft.Row(
                [
                    self.text_container,  
                    ft.Container(self.image, alignment=ft.alignment.top_right)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            padding=ft.padding.only(1),
            margin=ft.margin.only(1, 30),
        )

        self.iconButton = ft.icons.DARK_MODE if not self.darkmode else ft.icons.LIGHT_MODE
        self.theme_button = ft.ElevatedButton("Dark", self.iconButton, on_click=self.changeTheme)

        self.nombre_input = ft.TextField(value="", label="Nombre_Carpeta", text_align=ft.TextAlign.CENTER, width=200, border_color="#99B898" if self.darkmode else "#007ba7")
        self.extension_input = ft.TextField(value="", label="Extensión", text_align=ft.TextAlign.CENTER, width=100, border_color="#99B898" if self.darkmode else "#007ba7")

        self.button_row = ft.Row(
            [
                self.nombre_input,
                self.extension_input,
                ft.ElevatedButton("Añadir", ft.icons.ADD, icon_color="green400", on_click=self.añadir, style=ft.ButtonStyle(overlay_color="#99B898", color={ft.MaterialState.HOVERED: "#FFFFFF"}, shadow_color="black", elevation=5)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            height=100,
        )

        self.lista_column = ft.Column()

        self.button_send = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.PLAY_ARROW, color="green400", size=20),
                            ft.Text("Ordenar", size=16),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    on_click=self.ordenarArchivos,
                    style=ft.ButtonStyle(
                        overlay_color="#99B898",
                        bgcolor="none",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        side=ft.BorderSide(color="green400", width=2),
                        shadow_color="grey600",
                        elevation=5,
                        color={
                            ft.MaterialState.HOVERED: "white",
                            ft.MaterialState.PRESSED: "white",
                        }
                    ),
                    width=150,
                    height=40,
                    animate_scale=True,
                    scale=1.1,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.build_ui()

    def build_ui(self):
        self.page.add(self.cTitle)
        self.page.add(ft.Row([self.theme_button], alignment=ft.MainAxisAlignment.END))
        self.page.add(self.button_row)
        self.page.add(self.lista_column)
        self.page.add(self.button_send)

        self.actualizar_lista_column()

    def actualizar_lista_column(self):
        self.lista_column.controls.clear()
        for nombre, extension in self.lista_extensiones:
            fila = self.crear_fila(nombre, extension)
            self.lista_column.controls.append(fila)
        self.page.update()

    def añadir(self, e):
        nombre = self.nombre_input.value.strip()
        extension = self.extension_input.value.strip()
        
        if not nombre or not extension:
            return  # No añadir si los campos están vacíos
        
        for fila_nombre, fila_extension in self.lista_extensiones:
            if nombre == fila_nombre or extension == fila_extension:
                print(f"El nombre '{nombre}' o la extensión '{extension}' ya existen.")
                return
        
        self.lista_extensiones.append([nombre, extension])
        self.actualizar_lista_column()
        self.nombre_input.value = ""
        self.extension_input.value = ""
        self.page.update()

    def eliminar(self, e):
        fila = e.control.data
        self.lista_extensiones.remove(fila)
        self.actualizar_lista_column()

    def changeTheme(self, e):
        self.darkmode = not self.darkmode
        self.page.theme_mode = ft.ThemeMode.DARK if self.darkmode else ft.ThemeMode.LIGHT
        self.page.bgcolor = "#2A363B" if self.darkmode else "#F4F4F4"
        self.cTitle_text.color = "#FECEA8" if self.darkmode else "#434b4d"
        self.nombre_input.border_color = "#99B898" if self.darkmode else "#007ba7"
        self.extension_input.border_color = "#99B898" if self.darkmode else "#007ba7"
        self.image.src = 'https://www.udenar.edu.co/recursos/wp-content/uploads/2021/09/logo-udenar-blanco.png' if self.darkmode else 'https://www.udenar.edu.co/recursos/wp-content/uploads/2017/02/escudo_logosimbolo_udenar_2022.fw_-1.png'
        
        for control in self.lista_column.controls:
            for subcontrol in control.controls:
                if isinstance(subcontrol, ft.TextField):
                    subcontrol.border_color = "#99B898" if self.darkmode else "#007ba7"
                    subcontrol.color = "white" if self.darkmode else "black"
                    
        for control in self.lista_column.controls:
            for subcontrol in control.controls:
                if isinstance(subcontrol, ft.ElevatedButton):
                    subcontrol.bgcolor = "Dark" if self.darkmode else "Light"
                    subcontrol.color = {ft.MaterialState.HOVERED: "#FFFFFF"} if self.darkmode else {ft.MaterialState.HOVERED: "#FFFFFF"}
                    
        self.updateThemeButton()
        self.page.update()

    def updateThemeButton(self):
        iconButton = ft.icons.DARK_MODE if not self.darkmode else ft.icons.LIGHT_MODE
        self.theme_button.icon = iconButton
        self.theme_button.text = "Light" if not self.darkmode else "Dark"

    def crear_fila(self, nombre, extension):
        fila = [nombre, extension]
        return ft.Row(
            [
                ft.TextField(value=nombre, text_align=ft.TextAlign.CENTER, width=200, border_color = "#99B898" if self.darkmode else "#007ba7", color="white" if self.darkmode else "black"),
                ft.TextField(value=extension, text_align=ft.TextAlign.CENTER, width=100, border_color="#99B898"),
                ft.ElevatedButton("Eliminar", ft.icons.DELETE, icon_color="red400", data=fila, on_click=self.eliminar, style=ft.ButtonStyle(overlay_color="#D32F2F", color={ft.MaterialState.HOVERED: "#FFFFFF"}, shadow_color="black", elevation=4)),
                ft.ElevatedButton("Editar", ft.icons.EDIT, icon_color="yellow400", on_click=None, style=ft.ButtonStyle(overlay_color="#ff847c", color={ft.MaterialState.HOVERED: "#FFFFFF"}, shadow_color="black", elevation=4)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            height=100,
        )

    def ordenarArchivos(self, e):
        ordenar = Ordenamiento(self.lista_extensiones, r"E:\testOrdenamiento")
        ordenar.ordenar()

    def build(self) -> ft.Column:
        return ft.Column(
            controls=[
                self.cTitle,
                ft.Row([self.theme_button], alignment=ft.MainAxisAlignment.END),
                self.button_row,
                self.lista_column,
                self.button_send
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

def main(page: ft.Page):
    page.title = "Ordenar Elementos"
    ordenar_elementos_app = OrdenarElementos(page)
    page.add(ordenar_elementos_app)

if __name__ == "_main_":
    ft.app(target=main)