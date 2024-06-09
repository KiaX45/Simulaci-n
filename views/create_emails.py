import flet as ft
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from server.post_email import EmailSender 
from server.get_email import Get_email

class Email_creation(ft.UserControl):
    def __init__(self, page, darkMode: bool = True) ->None:
        super().__init__()
        self.darkMode = darkMode
        self.page = page
        
        
        self.Title = ft.Text("welcome to the Email creation page!")
        
        self.Final_email = []
        
        self.enviar = False
        
        self.mostrar = True
        
        self.nombre = ft.TextField(value="", label="Nombre personalizado", hint_text="Nombre destinatario", text_align=ft.TextAlign.CENTER, width=200, border_color="#99B898" if self.darkMode else "#007ba7")
        
        self.propietario = "contrasena"
        
        self.correo = ft.TextField(value="", label="Correo", hint_text="Correo destinatario", text_align=ft.TextAlign.CENTER, width=200, border_color="#99B898" if self.darkMode else "#007ba7")
        
        self.tipo = ft.TextField(value="", label="Tipo", hint_text="Tipo destinatario", text_align=ft.TextAlign.CENTER, width=200, border_color="#99B898" if self.darkMode else "#007ba7")
        
        
        self.boton_añadir = ft.ElevatedButton("Añadir", ft.icons.ADD, icon_color="green400", on_click=self.añadir, style=ft.ButtonStyle(overlay_color="#99B898", color={ft.MaterialState.HOVERED: "#FFFFFF"}, shadow_color="black", elevation=5))
        
        self.form = ft.Row(
            [
                self.nombre,
                self.correo,
                self.tipo,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            height=100,
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
            scroll=True
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
                ft.TextField(value=correo, text_align=ft.TextAlign.CENTER, width=200, border_color="green400"),
                ft.TextField(value=tipo, text_align=ft.TextAlign.CENTER, width=100, border_color="green400"),
                ft.TextField(value=nombre, text_align=ft.TextAlign.CENTER, width=100, border_color="green400"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
        
        
    def añadir(self, e):
        print(self.nombre.value)
        print(self.correo.value)
        print(self.tipo.value)
        
        if(self.nombre.value == "" or self.correo.value == "" or self.tipo.value == ""):
            #mostramos un mensaje de error
            dialog = ft.AlertDialog(title=ft.Text("Error"), content=ft.Text("Todos los campos son obligatorios"))
            self.page.dialog = dialog
            return
        
        email_sender = EmailSender()
        response = email_sender.send_email(self.correo.value, self.enviar, self.mostrar, self.nombre.value, self.propietario, self.tipo.value)
        print(response["message"])
        
        correct_dialog = ft.AlertDialog(title=ft.Text("Exito"), content=ft.Text(response["message"]))
        self.page.dialog = correct_dialog
        correct_dialog.open = True
        self.page.update()
        
        
    def build(self) -> ft.Column:
        self.add_destinatarios(None)
        #cambiamos el tema de la pagina dependiendo del valor de darkMode
        return ft.Row(
            controls=[
                ft.Row(
                    controls=[
                        self.Title,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,),
                ft.Row({
                    self.form,
                    self.boton_enviar,
                }),
                ft.Row(
                    controls=[
                        self.destinatarios_column,
                    ],
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

         
