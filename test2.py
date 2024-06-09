import flet as ft

class FilePickerApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.file_name = ft.Text(value="No file selected", size=16)
        self.file_path = ft.Text(value="", size=12)
        self.file_picker = ft.FilePicker(on_result=self.on_file_picked)
        self.page.overlay.append(self.file_picker)
        
        self.setup_ui()

    def setup_ui(self):
        pick_file_button = ft.ElevatedButton(
            text="Pick a file",
            on_click=lambda _: self.file_picker.pick_files(allow_multiple=False)
        )
        
        self.page.add(
            pick_file_button,
            self.file_name,
            self.file_path
        )

    def on_file_picked(self, e: ft.FilePickerResultEvent):
        if e.files:
            selected_file = e.files[0]
            self.file_path.value = selected_file.path
            self.file_name.value = selected_file.name
            self.page.update()

def main(page: ft.Page):
    FilePickerApp(page)

ft.app(target=main)
