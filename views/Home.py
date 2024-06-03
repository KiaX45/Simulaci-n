import flet as ft

class Home(ft.UserControl):
    def __init__(self, darkMode: bool = True) ->None:
        super().__init__()
        self.darkMode = darkMode
        
        
    def build(self) -> ft.Row:
        #cambiamos el tema de la pagina dependiendo del valor de darkMode
        return ft.Row(
            controls=[
                ft.Text("welcome to the home page!"),
            ]
        )
         