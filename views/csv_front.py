import flet as ft

class Csv_convertion(ft.UserControl):
    def __init__(self,  page, darkMode: bool = True,) ->None:
        super().__init__()
        self.darkMode = darkMode
        self.page = page
        
        self.file_name = ft.Text(value="No file selected", size=16)
        self.file_path = ft.Text(value="", size=12)
        self.file_picker = ft.FilePicker(on_result=self.on_file_picked)
        self.page.overlay.append(self.file_picker)
        
        
        self.mainColumn = ft.Column(
            controls=[
            ]
        )
        
        self.setup_ui()
        
        
        
    def setup_ui(self):
        pick_file_button = ft.ElevatedButton(
            text="Pick a file",
            on_click=lambda _: self.file_picker.pick_files(allow_multiple=False)
        )
        
        self.mainColumn.controls.append(pick_file_button)
        self.mainColumn.controls.append(self.file_name)
        self.mainColumn.controls.append(self.file_path)

    def on_file_picked(self, e: ft.FilePickerResultEvent):
        if e.files:
            selected_file = e.files[0]
            self.file_path.value = selected_file.path
            self.file_name.value = selected_file.name
            print(self.file_name.value)
            print(self.file_path.value)
            self.mainColumn.update()
            self.page.update()
        
        
    def build(self) -> ft.Row:
        #cambiamos el tema de la pagina dependiendo del valor de darkMode
        return ft.Row(
            controls=[
                self.mainColumn
            ]
        )
        
        
        
def main(page: ft.Page):
    page.title = "Ordenar Elementos"
    ordenar_elementos_app = Csv_convertion(page)
    page.add(ordenar_elementos_app)

if __name__ == "__main__":
    ft.app(target=main)

         