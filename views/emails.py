# emails
import flet as ft
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logic.emailsender import send_email
from server.get_email import Get_email


class Email(ft.UserControl):
    def __init__(self, page: ft.page, darkmode: bool = True):
        super().__init__()

        self.page = page
        self.darkmode = darkmode

        self.email = ft.TextField(
            label="Correo Electrónico",
            hint_text="Ingrese su correo electrónico",
            width=700,
            border_color="#99B898" if self.darkmode else "#007ba7",
        )
        self.password = ft.TextField(
            label="Contraseña",
            hint_text="Ingrese su contraseña",
            password=True,
            width=700,
            border_color="#99B898" if self.darkmode else "#007ba7",
        )
        self.message = ft.TextField(
            label="Mensaje",
            hint_text="Ingrese su mensaje",
            width=700,
            multiline=True,
            min_lines=3,
            border_color="#99B898" if self.darkmode else "#007ba7",
        )
        self.subject = ft.TextField(
            label="Asunto",
            hint_text="Ingrese el asunto",
            width=700,
            border_color="#99B898" if self.darkmode else "#007ba7",
        )

        #######################################################################################################3

        self.page.theme_mode = (
            ft.ThemeMode.DARK if self.darkmode else ft.ThemeMode.LIGHT
        )
        self.iconButton = (
            ft.icons.DARK_MODE if not self.darkmode else ft.icons.LIGHT_MODE
        )
        self.theme_button = ft.ElevatedButton(
            "Dark", self.iconButton, on_click=self.changeTheme
        )

        self.image = ft.Image(
            src="https://www.udenar.edu.co/recursos/wp-content/uploads/2021/09/logo-udenar-blanco.png",
            width=100,
            height=100,
            fit="contain",
        )

        self.image2 = ft.Image(
            src="https://www.udenar.edu.co/recursos/wp-content/uploads/2021/09/logo-udenar-blanco.png",
            width=100,
            height=100,
            fit="contain",
        )

        self.cTitle_text = ft.Text(
            "EMAILS",
            size=40,
            font_family="georgia",
            color="#FECEA8" if self.darkmode else "black",
        )

        self.text_container = ft.Container(
            self.cTitle_text, alignment=ft.alignment.center
        )

        self.cTitle = ft.Container(
            ft.Row(
                [
                    self.text_container,
                    ft.Container(self.image, alignment=ft.alignment.top_right),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.padding.only(1),
            margin=ft.margin.only(1, 30),
        )

        ##################################################################################################################

        self.submit_button = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.SEND_ROUNDED, color="green400", size=20),
                            ft.Text("Enviar", size=16),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    on_click=self.send_email,
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
                        },
                    ),
                    width=150,
                    height=40,
                    animate_scale=True,
                    scale=1.1,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            
        )

        get_email = Get_email()

        self.filtered_emails = get_email.get_emails()

        self.destinatarios = []

        self.filtros = ["Todos"]

        self.create_destinatarios()

        self.createFilter()

        # Crear una lista de DropdownItem a partir del arreglo
        items = [ft.dropdown.Option(opcion) for opcion in self.filtros]

        self.filtrosColumn = ft.Container(
            ft.Row(
            controls=[
                ft.Dropdown(
                    hint_text="Filtrar por tipo",
                    label="Filtros",
                    options=items,
                    width=200,
                    on_change=self.filtrar,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        # Creamos un atributo fila para contener todos los inputs necesarios

        self.row_titulos = ft.Row(
            [
                ft.Container(
                    ft.Text("Correo destinatario", size=24),
                    margin=ft.margin.only(right=20),
                ),
                ft.Container(
                    ft.Text("Lugar", size=24), margin=ft.margin.only(right=20)
                ),
                ft.Container(
                    ft.Text("Nombre", size=24), margin=ft.margin.only(right=20)
                ),
                ft.Text("Seleccionado", size=24),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.form = ft.Container(
            ft.Column(
            [
                ft.Text("Enviar Correo Electrónico"),
                self.email,
                self.password,
                self.subject,
                self.message,
                self.submit_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
            margin=ft.margin.only(left=300),
        )

        # Creamos un atributo que contendrá los destinatarios
        self.destinatarios_column = ft.Column(
            controls=[],
            alignment=ft.MainAxisAlignment.START,
            scroll=ft.ScrollMode.ALWAYS,  # Asegurarse de que el scroll esté habilitado
        )

    ###################################################################################

    def changeTheme(self, e):
        self.darkmode = not self.darkmode
        self.email.border_color = "#99B898" if self.darkmode else "#007ba7"
        self.password.border_color = "#99B898" if self.darkmode else "#007ba7"
        self.message.border_color = "#99B898" if self.darkmode else "#007ba7"
        self.subject.border_color = "#99B898" if self.darkmode else "#007ba7"
        self.page.theme_mode = (
            ft.ThemeMode.DARK if self.darkmode else ft.ThemeMode.LIGHT
        )
        self.page.bgcolor = "#2A363B" if self.darkmode else "#F4F4F4"
        self.cTitle_text.color = "#FECEA8" if self.darkmode else "#434b4d"
        self.image.src = (
            "https://www.udenar.edu.co/recursos/wp-content/uploads/2021/09/logo-udenar-blanco.png"
            if self.darkmode
            else "https://www.udenar.edu.co/recursos/wp-content/uploads/2017/02/escudo_logosimbolo_udenar_2022.fw_-1.png"
        )

        self.updateThemeButton()
        self.page.update()

    def updateThemeButton(self):
        iconButton = ft.icons.DARK_MODE if not self.darkmode else ft.icons.LIGHT_MODE
        self.theme_button.icon = iconButton
        self.theme_button.text = "Light" if not self.darkmode else "Dark"
        self.theme_button.elevation = 4 if not self.darkmode else 3

    def build_ui(self):
        self.page.add(self.cTitle)
        self.page.add(ft.Row([self.theme_button], alignment=ft.MainAxisAlignment.END))

    ##################################################################################

    def create_destinatarios(self):
        for email in self.filtered_emails:
            print(email)
            correo = email["Email"]
            estado = email["Enviar"]
            tipo = email["Tipo"]
            nombre = email["Nombre"]
            self.destinatarios.append([correo, estado, tipo, nombre, True])

    def createFilter(self):
        # vamos a llenar el arreglo de filtros con los tipos de correos
        for correo, estado, tipo, nombre, show in self.destinatarios:
            if tipo not in self.filtros:
                self.filtros.append(tipo)

    def filtrar(self, e):
        filtro = e.control.value
        new_destinatarios = []
        for correo, estado, tipo, nombre, show in self.destinatarios:
            if filtro == "Todos" or filtro == tipo:
                new_destinatarios.append([correo, estado, tipo, nombre, True])
            else:
                new_destinatarios.append([correo, estado, tipo, nombre, False])
        self.destinatarios = new_destinatarios
        self.borrar_destinatario(e)
        self.add_destinatarios(e)
        self.destinatarios_column.update()

    def add_destinatarios(self, e):

        for correo, estado, tipo, nombre, show in self.destinatarios:
            if not show:
                continue
            fila = self.crear_fila(correo, nombre, estado, tipo)
            self.destinatarios_column.controls.append(fila)

    def borrar_destinatario(self, e):
        self.destinatarios_column.controls.clear()
        self.destinatarios_column.update()

    def actualizar_estado(self, e):
        fila = e.control.data
        index = 0
        for correo, estado, tipo, nombre, show in self.destinatarios:
            if correo == fila[0]:
                self.destinatarios[index][1] = not estado
                break
            index += 1
        self.destinatarios
        self.page.update()

    def crear_fila(self, correo, nombre, estado, tipo):
        fila = [correo, nombre, estado, tipo]
        return ft.Row(
            [
                ft.TextField(
                    value=correo,
                    text_align=ft.TextAlign.CENTER,
                    width=200,
                    border_color="#a9916b",
                ),
                ft.TextField(
                    value=tipo,
                    text_align=ft.TextAlign.CENTER,
                    width=100,
                    border_color="#a9916b",
                ),
                ft.TextField(
                    value=nombre,
                    text_align=ft.TextAlign.CENTER,
                    width=100,
                    border_color="#a9916b",
                ),
                ft.Checkbox(
                    value=estado,
                    width=100,
                    data=fila,
                    active_color="green400",
                    on_change=self.actualizar_estado,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )

    def send_email(self, e):
        if (
            self.email.value == ""
            or self.password.value == ""
            or self.message.value == ""
            or self.subject.value == ""
        ):
            dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Todos los campos son obligatorios"),
            )
            self.page.dialog = dialog
            dialog.open = True
            self.page.update()
            return

        # filtramos los destinatarios
        for correo, estado, tipo, nombre, show in self.destinatarios:
            if estado == True and show == True:
                new_message = self.message.value.replace("{nombre}", nombre)
                new_message = new_message.replace("{correo}", correo)
                new_subject = self.subject.value.replace("{nombre}", nombre)
                new_subject = new_subject.replace("{correo}", correo)
                response = send_email(
                    self.email.value,
                    correo,
                    self.password.value,
                    new_message,
                    new_subject,
                ).send()
                print(response)
                
        dialog = ft.AlertDialog(
                title=ft.Text("Exito"),
                content=ft.Text("Todos los correos han sido enviados exitosamente"),
            )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        

        print(self.message.value)
        print(self.subject.value)

    def build(self) -> ft.Column:
        # Asegurarse de que se agreguen destinatarios antes de devolver la estructura de la página
        self.add_destinatarios(e=None)

        return ft.Column(
            controls=[
                self.cTitle,
                ft.Row([self.theme_button], alignment=ft.MainAxisAlignment.END),
                self.form,
                self.filtrosColumn,
                self.row_titulos,
                ft.Container(
                    self.destinatarios_column, height=400
                ),  # Añadir un contenedor con altura fija para el scroll
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.ALWAYS  # Asegurarse de que el scroll esté habilitado
        )
    
    def update_email(self):
        get_email = Get_email()
        self.filtered_emails = get_email.get_emails()
        self.destinatarios = []
        self.create_destinatarios()
        
       
        self.createFilter()
        
        self.borrar_destinatario(e=None)
        self.add_destinatarios(e=None)
        self.destinatarios_column.update()
        
        self.page.update()
        print("hola")


def main(page: ft.Page):
    page.title = "Enviar Correo"
    email_app = Email()
    page.add(email_app)


if __name__ == "__main__":
    ft.app(target=main)
