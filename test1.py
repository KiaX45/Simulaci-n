import flet as ft

class MyApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.destinatarios_column = ft.Column()

        # Inicialmente agregar algunos controles al column
        self.add_controls()

    def add_controls(self):
        self.destinatarios_column.controls.extend([
            ft.TextField(label="Correo 1"),
            ft.TextField(label="Correo 2"),
            ft.TextField(label="Correo 3")
        ])
        if self.page:
            self.destinatarios_column.update()

    def clear_column(self, e):
        self.destinatarios_column.controls.clear()
        self.destinatarios_column.update()

    def recreate_controls(self, e):
        self.add_controls()

    def build(self):
        return ft.Column(
            controls=[
                ft.ElevatedButton(text="Clear", on_click=self.clear_column),
                ft.ElevatedButton(text="Recreate", on_click=self.recreate_controls),
                self.destinatarios_column
            ]
        )

def main(page: ft.Page):
    page.title = "Clear and Recreate Column Example"
    app = MyApp()
    page.add(app)

if __name__ == "__main__":
    ft.app(target=main)
