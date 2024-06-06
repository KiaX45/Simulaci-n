import flet as ft
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.emailsender import send_email


class Email(ft.UserControl):
    def __init__(self, page, darkMode: bool = True):
        super().__init__()

        self.page = page  # Asignar la página al atributo self.page

        self.email = ft.TextField(label="Correo Electrónico", hint_text="Ingrese su correo electrónico")
        self.password = ft.TextField(label="Contraseña", hint_text="Ingrese su contraseña", password=True)
        self.message = ft.TextField(label="Mensaje", hint_text="Ingrese su mensaje")
        self.subject = ft.TextField(label="Asunto", hint_text="Ingrese el asunto")

        self.submit_button = ft.ElevatedButton("Enviar", icon=ft.icons.SEND_ROUNDED, on_click=self.send_email)
        self.destinatarios = [["Correo 1", False, "Trabajo", "Luis"], ["Correo 2", True, "Personal", "Camilo"],
                              ["Correo 3", False, "Familia", "Andres"], ["Correo 4", True, "Amigos", "Jon"],
                              ["Correo 5", False, "Trabajo", "Sara"], ["Correo 6", True, "Personal", "Luisa"]]
        
        # Creamos un atributo fila para contener todos los inputs necesarios 
        self.form = ft.Column(
            [
                ft.Text("Enviar Correo Electrónico"),
                self.email,
                self.password,
                self.subject,
                self.message,
                self.submit_button
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        # Creamos un atributo que contendrá los destinatarios 
        self.destinatarios_column = ft.Column(
            controls=[],
            alignment=ft.MainAxisAlignment.START,
            scroll=ft.ScrollMode.ALWAYS  # Asegurarse de que el scroll esté habilitado
        )
        
        self.add_destinatarios()
        
        
    def add_destinatarios(self):
        self.destinatarios_column.controls.clear()
        for correo, estado, tipo, nombre in self.destinatarios:
            fila = self.crear_fila(correo, nombre, estado, tipo)
            self.destinatarios_column.controls.append(fila)
        self.page.update()  # Asegurarse de que la página se actualice
        
    def actualizar_estado(self, e):
        fila = e.control.data
        index:int = 0
        for nombre, estado, tipo in self.destinatarios:
            if nombre == fila[0]:
                self.destinatarios[index][1] = not estado
                break
            index += 1
        
        self.page.update()
        
    def crear_fila(self, correo,nombre, estado,  tipo):
        fila = [correo, nombre, estado, tipo]
        return ft.Row(
            [
                ft.TextField(value=correo, text_align=ft.TextAlign.CENTER, width=200, border_color="green400"),
                ft.TextField(value=tipo, text_align=ft.TextAlign.CENTER, width=100, border_color="green400"),
                ft.TextField(value=nombre, text_align=ft.TextAlign.CENTER, width=100, border_color="green400"),
                ft.Checkbox(value=estado, width=100, data=fila, active_color="green400", on_change=self.actualizar_estado),
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
        

    def send_email(self, e):
        if self.email.value == "" or self.password.value == "" or self.message.value == "" or self.subject.value == "":
            dialog = ft.AlertDialog(title=ft.Text("Error"), content=ft.Text("Todos los campos son obligatorios"))
            self.page.dialog = dialog
            dialog.open = True
            self.page.update()
            return
        
        #filtramos los destinatarios
        destinatarios_finales = list(filter(lambda x: x[1] == True, self.destinatarios))
        destinatarios_finales = list(map(lambda x: x[0], destinatarios_finales))
        
        sender = self.email.value
        password = self.password.value
        message = self.message.value
        subject = self.subject.value
        
        send = send_email(sender, destinatarios_finales, password, message, subject)
        result = send.send()
        print(result)

    def build(self) -> ft.Column:
        return ft.Column(
            controls=[
                self.form,
                ft.Container(self.destinatarios_column, height=200)  # Añadir un contenedor con altura fija para el scroll
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        )


def main(page: ft.Page):
    page.title = "Enviar Correo"
    email_app = Email(page)
    page.add(email_app)


if __name__ == "__main__":
    ft.app(target=main)
