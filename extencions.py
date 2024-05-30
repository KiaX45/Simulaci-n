import flet as ft
from logic.ordenar import Ordenamiento 

def main(page: ft.Page):
    darkmode = True
    page.theme_mode = ft.ThemeMode.DARK if darkmode else ft.ThemeMode.LIGHT

    lista_extensiones = [["Documentos", ".docx"], ["Presentaciones", ".pptx"], ["PDF", ".pdf"], ["Imagenes", "img"]]
    
    def actualizar_lista_column():
        lista_column.controls.clear()
        for nombre, extension in lista_extensiones:
            fila = crear_fila(nombre, extension)
            lista_column.controls.append(fila)
        page.update()

    def añadir(e):
        nombre = nombre_input.value.strip()
        extension = extension_input.value.strip()
        
        if not nombre or not extension:
            return  # No añadir si los campos están vacíos
        
        for fila_nombre, fila_extension in lista_extensiones:
            if nombre == fila_nombre or extension == fila_extension:
                print(f"El nombre '{nombre}' o la extensión '{extension}' ya existen.")
                return
        
        lista_extensiones.append([nombre, extension])
        actualizar_lista_column()
        nombre_input.value = ""
        extension_input.value = ""
    
    def eliminar(e):
        fila = e.control.data
        lista_extensiones.remove(fila)
        actualizar_lista_column()
    
    def changeTheme(e):
        nonlocal darkmode
        darkmode = not darkmode
        page.theme_mode = ft.ThemeMode.DARK if darkmode else ft.ThemeMode.LIGHT
        updateThemeButton()
        page.update()
    
    def updateThemeButton():
        iconButton = ft.icons.DARK_MODE if not darkmode else ft.icons.LIGHT_MODE
        theme_button.icon = iconButton
        theme_button.text = "Light" if not darkmode else "Dark"
    
    def crear_fila(nombre, extension):
        fila = [nombre, extension]
        return ft.Row(
            [
                ft.TextField(value=nombre, text_align=ft.TextAlign.CENTER, width=200, border_color="green400"),
                ft.TextField(value=extension, text_align=ft.TextAlign.CENTER, width=100, border_color="green400"),
                ft.ElevatedButton("Eliminar", ft.icons.DELETE, icon_color="red400", data=fila, on_click=eliminar, style=ft.ButtonStyle(overlay_color="#D32F2F", color={ft.MaterialState.HOVERED: "#FFFFFF"})),
                ft.ElevatedButton("Editar", ft.icons.EDIT, icon_color="yellow400", on_click=None, style=ft.ButtonStyle(overlay_color="#1976D2", color={ft.MaterialState.HOVERED: "#FFFFFF"})),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            height=100,
        )

    iconButton = ft.icons.DARK_MODE if not darkmode else ft.icons.LIGHT_MODE
    theme_button = ft.ElevatedButton("Dark", iconButton, on_click=changeTheme)

    nombre_input = ft.TextField(value="", hint_text="Nombre_Carpeta", text_align=ft.TextAlign.CENTER, width=200, border_color="green400")
    extension_input = ft.TextField(value="", hint_text="Extención", text_align=ft.TextAlign.CENTER, width=100, border_color="green400")
    
    button_row = ft.Row(
        [
            nombre_input,
            extension_input,
            ft.ElevatedButton("Añadir", ft.icons.ADD, icon_color="green400", on_click=añadir, style=ft.ButtonStyle(overlay_color="#1976D2", color={ft.MaterialState.HOVERED: "#FFFFFF"})),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        height=100,
    )

    lista_column = ft.Column()
    
    
    #parte de ordenamiento:
    
    def ordenarArchivos(e):
        
        ordenar = Ordenamiento(lista_extensiones, r"E:\testOrdenamiento")
        ordenar.ordenar()
        pass
    
    button_send = ft.Row(
        [
            ft.ElevatedButton("Ordenar", ft.icons.PLAY_ARROW, icon_color="green400", adaptive=True, on_click=ordenarArchivos, style=ft.ButtonStyle(overlay_color="#1976D2", color={ft.MaterialState.HOVERED: "#FFFFFF"}, padding=20 )),
        ],
         alignment= ft.MainAxisAlignment.CENTER
        )

    page.add(ft.Row([theme_button], alignment=ft.MainAxisAlignment.END))
    page.add(button_row)
    page.add(lista_column)
    page.add(button_send)

    actualizar_lista_column()

ft.app(main)
