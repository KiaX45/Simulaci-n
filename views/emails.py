import flet as ft
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.emailsender import send_email
from server.get_email import Get_email

class Email(ft.UserControl):
    def __init__(self, darkMode: bool = True):
        super().__init__()

        self.email = ft.TextField(label="Correo Electrónico", hint_text="Ingrese su correo electrónico")
        self.password = ft.TextField(label="Contraseña", hint_text="Ingrese su contraseña", password=True)
        self.message = ft.TextField(label="Mensaje", hint_text="Ingrese su mensaje", multiline=True, min_lines=3 )
        self.subject = ft.TextField(label="Asunto", hint_text="Ingrese el asunto")

        self.submit_button = ft.ElevatedButton("Enviar", icon=ft.icons.SEND_ROUNDED, on_click=self.send_email)
        
        get_email = Get_email()
        
        self.filtered_emails = get_email.get_emails()
        
        
        self.destinatarios = []
        
        self.filtros = ["Todos"]
        
        self.create_destinatarios()
        
        self.createFilter()
        
        # Crear una lista de DropdownItem a partir del arreglo
        items = [ft.dropdown.Option(opcion) for opcion in self.filtros]
        
        self.filtrosColumn = ft.Column(
            controls=[
                ft.Dropdown(
                hint_text="Filtrar por tipo",  
                label="Filtros",
                options=items,
                width=100,
                on_change=self.filtrar
                )
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        )
        
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
        
    def create_destinatarios(self):
        for email in self.filtered_emails:
            print(email)
            correo = email["Email"]
            estado = email["Enviar"]
            tipo = email["Tipo"]
            nombre = email["Nombre"]
            self.destinatarios.append([correo, estado, tipo, nombre, True])
    
    def createFilter(self):
        #vamos a llenar el arreglo de filtros con los tipos de correos 
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
        for correo, estado, tipo, nombre, show in self.destinatarios:
            if estado == True and show == True:
                new_message = self.message.value.replace("{nombre}", nombre)
                new_subject = self.subject.value.replace("{nombre}", nombre)
                response = send_email(self.email.value, correo, self.password.value, new_message, new_subject).send()
                print(response)
        
        
        print(self.message.value)
        print(self.subject.value)
           
        
       

    def build(self) -> ft.Column:
        # Asegurarse de que se agreguen destinatarios antes de devolver la estructura de la página
        self.add_destinatarios(e=None)
        
        return ft.Column(
            controls=[
                self.form,
                self.filtrosColumn,
                ft.Container(self.destinatarios_column, height=400)  # Añadir un contenedor con altura fija para el scroll
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.ALWAYS  # Asegurarse de que el scroll esté habilitado
        )


def main(page: ft.Page):
    page.title = "Enviar Correo"
    email_app = Email()
    page.add(email_app)


if __name__ == "__main__":
    ft.app(target=main)
