#create emails
import flet as ft
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from server.post_email import EmailSender
from server.get_email import Get_email


class Email_creation(ft.UserControl):
    def __init__(self, page, darkmode: bool = True) -> None:
        super().__init__()
        self.darkmode = darkmode
        self.page = page

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

        self.Final_email = []

        self.enviar = False

        self.mostrar = True

        self.nombre = ft.TextField(
            value="",
            label="Nombre personalizado",
            hint_text="Nombre destinatario",
            text_align=ft.TextAlign.CENTER,
            width=200,
            border_color="#99B898" if self.darkmode else "#007ba7",
        )

        self.propietario = "contrasena"

        self.correo = ft.TextField(
            value="",
            label="Correo",
            hint_text="Correo destinatario",
            text_align=ft.TextAlign.CENTER,
            width=200,
            border_color="#99B898" if self.darkmode else "#007ba7",
        )

        self.tipo = ft.TextField(
            value="",
            label="Tipo",
            hint_text="Tipo destinatario",
            text_align=ft.TextAlign.CENTER,
            width=200,
            border_color="#99B898" if self.darkmode else "#007ba7",
        )

        self.boton_añadir = ft.ElevatedButton(
            "Añadir",
            ft.icons.ADD,
            icon_color="green400",
            on_click=self.añadir,
            style=ft.ButtonStyle(
                overlay_color="#99B898",
                color={ft.MaterialState.HOVERED: "#FFFFFF"},
                shadow_color="black",
                elevation=5,
            ),
        )
        
        self.row_titulos = ft.Row(
            [
                ft.Container(
                    ft.Text("Correo", size=24),
                    margin=ft.margin.only(left=80, right=20),
                ),
                ft.Container(
                    ft.Text("Tipo", size=24), margin=ft.margin.only(left=40,right=20)
                ),
                ft.Container(
                    ft.Text("Nombre", size=24), margin=ft.margin.only(right=20)
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.form = ft.Container(
            ft.Row(
                [
                    self.nombre,
                    self.correo,
                    self.tipo,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                height=100,
            ),
            margin=ft.margin.only(bottom=30),
        )

        self.boton_enviar = ft.Row(
            [
                self.boton_añadir,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        get_email = Get_email()

        self.filtered_emails = get_email.get_emails()

        self.destinatarios_column = ft.Column(
            controls=[],
            width=500,
            height=500,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            scroll=True,
        )

    def add_destinatarios(self, e):

        for email in self.filtered_emails:
            correo = email["Email"]
            estado = email["Mostrar"]
            tipo = email["Tipo"]
            nombre = email["Nombre"]
            fila = self.crear_fila(correo, nombre, estado, tipo)
            self.destinatarios_column.controls.append(fila)

    def crear_fila(self, correo, nombre, estado, tipo):
        print(correo)
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
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )

    def añadir(self, e):
        print(self.nombre.value)
        print(self.correo.value)
        print(self.tipo.value)

        if self.nombre.value == "" or self.correo.value == "" or self.tipo.value == "":
            # mostramos un mensaje de error
            dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Todos los campos son obligatorios"),
            )
            self.page.dialog = dialog
            return

        email_sender = EmailSender()
        response = email_sender.send_email(
            self.correo.value,
            self.enviar,
            self.mostrar,
            self.nombre.value,
            self.propietario,
            self.tipo.value,
        )
        print(response["message"])

        correct_dialog = ft.AlertDialog(
            title=ft.Text("Exito"), content=ft.Text(response["message"])
        )
        self.page.dialog = correct_dialog
        correct_dialog.open = True
        self.page.update()
        
        #creamos una nueva fila con los datos del correo
        fila = self.crear_fila(self.correo.value, self.nombre.value, self.mostrar, self.tipo.value)
        self.destinatarios_column.controls.append(fila)
        self.page.update()
        #limpiamos los campos
        self.nombre.value = ""
        self.correo.value = ""
        self.tipo.value = ""
        self.page.update()
        
    def actualizar_correos(self):
        self.destinatarios_column.controls.clear()
        self.add_destinatarios(None)
        self.page.update()
        

    ###################################################################################

    def changeTheme(self, e):
        self.darkmode = not self.darkmode
        self.page.theme_mode = (
            ft.ThemeMode.DARK if self.darkmode else ft.ThemeMode.LIGHT
        )
        self.nombre.border_color = "#99B898" if self.darkmode else "#007ba7"
        self.correo.border_color = "#99B898" if self.darkmode else "#007ba7"
        self.tipo.border_color = "#99B898" if self.darkmode else "#007ba7"
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

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def build(self):
        self.add_destinatarios(None)

        # Cambiamos el tema de la página dependiendo del valor de darkMode
        return ft.Column(
            controls=[
                ft.Row(controls=[self.cTitle], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.theme_button], alignment=ft.MainAxisAlignment.END),
                ft.Row(
                    controls=[
                        self.form,
                        self.boton_enviar,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                self.row_titulos,
                ft.Row(
                    controls=[self.destinatarios_column],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )


def main(page: ft.Page):
    page.title = "Ordenar Elementos"
    ordenar_elementos_app = Email_creation(page)
    page.add(ordenar_elementos_app)


if __name__ == "__main__":
    ft.app(target=main)
