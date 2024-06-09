import flet as ft
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from views.Home import Home
from views.emails import Email
from views.extensions import OrdenarElementos
from views.create_emails import Email_creation
from views.csv_front import Csv_convertion
from views.temporales import EliminarArchivosTemporales


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    darkmode = True

    def changeTheme(e):
        nonlocal darkmode
        darkmode = not darkmode
        page.theme_mode = ft.ThemeMode.DARK if darkmode else ft.ThemeMode.LIGHT
        updateThemeButton()
        page.update()
        
    def updateThemeButton():
        icon = ft.icons.DARK_MODE if not darkmode else ft.icons.LIGHT_MODE
        theme_button.icon = icon
        theme_button.text = "Light" if not darkmode else "Dark"

    icon = ft.icons.DARK_MODE if not darkmode else ft.icons.LIGHT_MODE
    theme_button = ft.ElevatedButton(
        text="Dark",
        icon=icon,
        on_click=changeTheme
    )
    
    appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MENU),
        leading_width=50,
        title=ft.Text("Click Solver"),
        center_title=True,
        actions=[theme_button]
    )
    
    ## Creación de instancias de las clases Home y Email
    email = Email(page)
    home = Home()
    extensions = OrdenarElementos(page)
    email_creation = Email_creation(page)
    csv_convertion = Csv_convertion(page)
    eliminarArchivosTemporales = EliminarArchivosTemporales(page)
    
    
    def change_page(event):
        match event.control.selected_index:
            case 0:
                page.go("/")
            case 1:
                page.go("/tienda")
            case 2:
                page.go("/extensiones")
            case 3:
                page.go("/email_creation")
            case 4: 
                page.go("/csv_convertion")
            case 5:
                page.go("/eliminar_archivos_temporales")

    
    #creamos el rail de navegación
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.SELECTED,
        min_width=100,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME,
                label="Home",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.EMAIL,
                label="Email",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.FOLDER,
                label="Extensiones",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.MARK_EMAIL_READ_SHARP,
                label="Crear Email",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.TABLE_CHART,
                label="Convertir CSV",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.DELETE,
                label="Eliminar Archivos Temporales",
            ),
        ],
        on_change=change_page
    )
    
    #Creamos la row de la vista
    filaPrincipalHome = ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([home.build()], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    
    filaPrincipalEmail = ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([email.build()], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True
        )
    
    filaPrincipalExtensiones = ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([extensions.build()], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True
        )
    
    filaPrincipalEmailCreation = ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([email_creation.build()], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True
        )
    
    filaPrincipalCsv = ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([csv_convertion.build()], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True
        )
    
    filaPrincipalEliminarArchivosTemporales = ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([eliminarArchivosTemporales.build()], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True
        )
    
    

    def cambiar_ruta(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    route="/",
                    controls=[
                        appbar,
                        filaPrincipalHome,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        elif page.route == "/tienda":
            page.views.append(
                ft.View(
                    route="/tienda",
                    controls=[
                        appbar,
                        filaPrincipalEmail,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        elif page.route == "/extensiones":
            page.views.append(
                ft.View(
                    route="/extensiones",
                    controls=[
                        appbar,
                        filaPrincipalExtensiones,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        elif page.route == "/email_creation":
            page.views.append(
                ft.View(
                    route="/email_creation",
                    controls=[
                        appbar,
                        filaPrincipalEmailCreation,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        elif page.route == "/csv_convertion":
            page.views.append(
                ft.View(
                    route="/csv_convertion",
                    controls=[
                        appbar,
                        filaPrincipalCsv,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        elif page.route == "/eliminar_archivos_temporales":
            page.views.append(
                ft.View(
                    route="/eliminar_archivos_temporales",
                    controls=[
                        appbar,
                        filaPrincipalEliminarArchivosTemporales,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()


    page.on_route_change = cambiar_ruta
    page.go(page.route)
    
    
   

ft.app(target=main)