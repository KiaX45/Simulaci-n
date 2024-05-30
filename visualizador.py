import flet as ft
import os

def main(page: ft.Page):
    darkmode = True
    page.theme_mode = ft.ThemeMode.DARK if darkmode else ft.ThemeMode.LIGHT

    current_directory = os.path.expanduser("~")  # Empezar en el directorio del usuario

    def listar_archivos_y_directorios(directory):
        try:
            items = os.listdir(directory)
            items.sort()
            return [(item, os.path.join(directory, item)) for item in items]
        except PermissionError:
            return []  # Manejar error de permiso

    def actualizar_lista_column():
        lista_column.controls.clear()
        items = listar_archivos_y_directorios(current_directory)
        for item, path in items:
            if os.path.isdir(path):
                fila = crear_fila(item, path, is_dir=True)
            else:
                fila = crear_fila(item, path, is_dir=False)
            lista_column.controls.append(fila)
        page.update()

    def crear_fila(item, path, is_dir):
        icon = ft.icons.FOLDER if is_dir else ft.icons.DESCRIPTION
        return ft.Row(
            [
                ft.Icon(icon),
                ft.TextButton(item, on_click=lambda e: navegar(path) if is_dir else abrir_archivo(path)),
            ],
            alignment=ft.MainAxisAlignment.START,
        )

    def navegar(path):
        nonlocal current_directory
        current_directory = path
        actualizar_lista_column()

    def abrir_archivo(path):
        if os.path.isfile(path):
            with open(path, 'r', errors='ignore') as f:
                content = f.read()
                file_viewer.value = content
                page.update()

    def subir_un_nivel(e):
        nonlocal current_directory
        parent_directory = os.path.dirname(current_directory)
        if parent_directory != current_directory:  # Evitar quedarse atascado en la raíz
            current_directory = parent_directory
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

    iconButton = ft.icons.DARK_MODE if not darkmode else ft.icons.LIGHT_MODE
    theme_button = ft.ElevatedButton("Dark", iconButton, on_click=changeTheme)

    subir_button = ft.ElevatedButton("Subir un nivel", on_click=subir_un_nivel)

    file_viewer = ft.TextField(value="", multiline=True, width=500, height=300, border_color="green400", read_only=True)
    
    lista_column = ft.Column()

    page.add(ft.Row([theme_button], alignment=ft.MainAxisAlignment.END))
    page.add(subir_button)
    page.add(lista_column)
    page.add(file_viewer)

    actualizar_lista_column()

ft.app(main)
