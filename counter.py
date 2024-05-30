import flet as ft

def main(page: ft.Page):
    darkmode = False
    
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    
    def restar(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()
    
    def sumar(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
    
    def changeTheme(e):
        nonlocal darkmode
        darkmode = not darkmode
        page.theme_mode = ft.ThemeMode.DARK if darkmode else ft.ThemeMode.LIGHT
        updateThemeButton()
        page.update()
    
    # Función para actualizar el botón de tema con el icono correcto
    def updateThemeButton():
        iconButton = ft.icons.DARK_MODE if not darkmode else ft.icons.LIGHT_MODE
        theme_button.icon = iconButton
        theme_button.text = "Light"
    
    # Crear inicialmente el botón de tema
    iconButton = ft.icons.DARK_MODE if not darkmode else ft.icons.LIGHT_MODE
    theme_button = ft.ElevatedButton("Dark",iconButton, on_click=changeTheme)
    
    # Definir el row de los botones de incrementar y decrementar
    button_row = ft.Row(
        [
            ft.IconButton(ft.icons.REMOVE, on_click=restar),
            txt_number,
            ft.IconButton(ft.icons.ADD, on_click=sumar),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        height=100,
    )
    
    # Agregar los elementos a la página
    page.add(button_row)
    page.add(ft.Row([theme_button]))

ft.app(main)
