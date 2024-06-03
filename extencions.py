import flet as ft
from logic.ordenar import Ordenamiento 

def main(page: ft.Page):
     # acomodar la UI en la interfaz
    page.window_maximized = True
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0
    page.bgcolor = "#2A363B"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    #
    
    #contenedor
    # c1 = ft.Container(
    #     ft.Row([
    #         ft.Container(
    #             ft.Column([
    #                 #(**)
    #             ])
    #         )
            
    #     ]),
        
    #     alignment= ft.alignment.center,
    #     width=700,
    #     height=400,
    #     bgcolor=ft.colors.PURPLE,
    #     border_radius=40
    # )
    
    
    
    darkmode = True
    page.theme_mode = ft.ThemeMode.DARK if darkmode else ft.ThemeMode.LIGHT
    
    
    image = ft.Image(
    src='https://www.udenar.edu.co/recursos/wp-content/uploads/2021/09/logo-udenar-blanco.png',
    width=100,
    height=100,
    fit='contain'
    )
    
    cTitle_text = ft.Text(
        'ORDENAR ELEMENTOS',
        size=40,
        font_family="georgia",
        color="#FECEA8" if darkmode else "black"  
    )
    
    # Contenedor para el texto
    text_container = ft.Container(
    cTitle_text,
    alignment=ft.alignment.center
    )

    cTitle = ft.Container(
    ft.Row(
        [
            text_container,  
            ft.Container(image, alignment=ft.alignment.top_right)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    padding=ft.padding.only(1),
    margin=ft.margin.only(1, 30),
    )
    
    #######

    lista_extensiones = [["Documentos", ".docx"], ["Presentaciones", ".pptx"], ["PDF", ".pdf"], ["Imagenes", ".png"]]
    
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
        # CAmbia el color de fondo según el modo
        page.bgcolor = "#2A363B" if darkmode else "#F4F4F4"
        cTitle_text.color = "#FECEA8" if darkmode else "#434b4d"
        nombre_input.border_color = "#99B898" if darkmode else "#007ba7"
        extension_input.border_color = "#99B898" if darkmode else "#007ba7"
        image.src = 'https://www.udenar.edu.co/recursos/wp-content/uploads/2017/02/escudo_logosimbolo_udenar_2022.fw_-1.png' if not darkmode else 'https://www.udenar.edu.co/recursos/wp-content/uploads/2021/09/logo-udenar-blanco.png'
        
        # Actualizar los colores de los TextField en las filas.
        for control in lista_column.controls:
            for subcontrol in control.controls:
                if isinstance(subcontrol, ft.TextField):
                    subcontrol.border_color = "#99B898" if darkmode else "#007ba7"
                    subcontrol.color = "white" if darkmode else "black"
                    
        for control in lista_column.controls:
            for subcontrol in control.controls:
                if isinstance(subcontrol, ft.ElevatedButton):
                    subcontrol.bgcolor = "Dark" if darkmode else "Light"
                    subcontrol.color={ft.MaterialState.HOVERED: "#FFFFFF"} if darkmode else {ft.MaterialState.HOVERED: "#FFFFFF"}
                    
        
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
                ft.TextField(value=nombre, text_align=ft.TextAlign.CENTER, width=200, border_color = "#99B898" if darkmode else "#007ba7", color="white" if darkmode else "black"),
                ft.TextField(value=extension, text_align=ft.TextAlign.CENTER, width=100, border_color="#99B898"),
                ft.ElevatedButton("Eliminar", ft.icons.DELETE, icon_color="red400", data=fila, on_click=eliminar, style=ft.ButtonStyle(overlay_color="#D32F2F", color={ft.MaterialState.HOVERED: "#FFFFFF"}, shadow_color="black", elevation=4)),
                ft.ElevatedButton("Editar", ft.icons.EDIT, icon_color="yellow400", on_click=None, style=ft.ButtonStyle(overlay_color="#ff847c", color={ft.MaterialState.HOVERED: "#FFFFFF"}, shadow_color="black", elevation=4)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            height=100,
        )

    iconButton = ft.icons.DARK_MODE if not darkmode else ft.icons.LIGHT_MODE
    theme_button = ft.ElevatedButton("Dark", iconButton, on_click=changeTheme)

    nombre_input = ft.TextField(value="", label="Nombre_Carpeta", text_align=ft.TextAlign.CENTER, width=200, border_color="#99B898" if darkmode else "#007ba7")
    extension_input = ft.TextField(value="", label="Extensión", text_align=ft.TextAlign.CENTER, width=100, border_color="#99B898" if darkmode else "#007ba7")
    
    button_row = ft.Row(
        [
            nombre_input,
            extension_input,
            ft.ElevatedButton("Añadir", ft.icons.ADD, icon_color="green400", on_click=añadir, style=ft.ButtonStyle(overlay_color="#99B898", color={ft.MaterialState.HOVERED: "#FFFFFF"}, shadow_color="black", elevation=5)),
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
        ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(ft.icons.PLAY_ARROW, color="green400", size=20),
                    ft.Text("Ordenar", size=16),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            on_click=ordenarArchivos,
            style=ft.ButtonStyle(
                overlay_color="#99B898",
                bgcolor= "none",
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
    

    page.add(cTitle)
    page.add(ft.Row([theme_button], alignment=ft.MainAxisAlignment.END))
    page.add(button_row)
    page.add(lista_column)
    page.add(button_send)

    actualizar_lista_column()

ft.app(main)
