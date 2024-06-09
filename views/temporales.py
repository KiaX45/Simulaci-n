import flet as ft
import os
import shutil
import tempfile

class EliminarArchivosTemporales(ft.UserControl):
    def __init__(self, page, darkmode: bool = True):
        super().__init__()

        self.page = page
        self.darkmode = darkmode

        self.page.window_maximized = True
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.padding = 0
        self.page.bgcolor = "#2A363B" if self.darkmode else "#F4F4F4"
        self.page.vertical_alignment = "center"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK if self.darkmode else ft.ThemeMode.LIGHT

        self.cTitle_text = ft.Text(
            'ELIMINAR ARCHIVOS TEMPORALES',
            size=40,
            font_family="georgia",
            color="#FECEA8" if self.darkmode else "black"
        )

        self.text_container = ft.Container(
            self.cTitle_text,
            alignment=ft.alignment.center
        )

        self.cTitle = ft.Container(
            ft.Row(
                [
                    self.text_container,  
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            padding=ft.padding.only(1),
            margin=ft.margin.only(1, 30),
        )

        self.iconButton = ft.icons.DARK_MODE if not self.darkmode else ft.icons.LIGHT_MODE
        self.theme_button = ft.ElevatedButton("Dark", self.iconButton, on_click=self.changeTheme)

        self.button_delete_temp = ft.ElevatedButton(
            "Eliminar Archivos Temporales",
            icon=ft.icons.DELETE,
            on_click=self.eliminar_archivos_temporales,
            style=ft.ButtonStyle(overlay_color="#99B898", bgcolor="none", shape=ft.RoundedRectangleBorder(radius=12), side=ft.BorderSide(color="red400", width=2), shadow_color="grey600", elevation=5)
        )

        self.build_ui()

    def build_ui(self):
        self.page.add(self.cTitle)
        self.page.add(ft.Row([self.theme_button], alignment=ft.MainAxisAlignment.END))
        self.page.add(ft.Row([self.button_delete_temp], alignment=ft.MainAxisAlignment.CENTER))

    def changeTheme(self, e):
        self.darkmode = not self.darkmode
        self.page.theme_mode = ft.ThemeMode.DARK if self.darkmode else ft.ThemeMode.LIGHT
        self.page.bgcolor = "#2A363B" if self.darkmode else "#F4F4F4"
        self.cTitle_text.color = "#FECEA8" if self.darkmode else "#434b4d"
        
        self.updateThemeButton()
        self.page.update()

    def updateThemeButton(self):
        iconButton = ft.icons.DARK_MODE if not self.darkmode else ft.icons.LIGHT_MODE
        self.theme_button.icon = iconButton
        self.theme_button.text = "Light" if not self.darkmode else "Dark"

    def eliminar_archivos_temporales(self, e):
        temp_dirs = [tempfile.gettempdir(), os.path.join(os.environ['SystemRoot'], 'Temp')]
        for temp_dir in temp_dirs:
            self.eliminar_archivos_en_directorio(temp_dir)
        print("Archivos temporales eliminados.")

    def eliminar_archivos_en_directorio(self, directorio):
        for root, dirs, files in os.walk(directorio):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Archivo eliminado: {file_path}")
                except Exception as ex:
                    print(f"No se pudo eliminar el archivo {file_path}. Error: {ex}")
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    shutil.rmtree(dir_path)
                    print(f"Directorio eliminado: {dir_path}")
                except Exception as ex:
                    print(f"No se pudo eliminar el directorio {dir_path}. Error: {ex}")

def main(page: ft.Page):
    page.title = "Eliminar Archivos Temporales"
    eliminar_archivos_temp_app = EliminarArchivosTemporales(page)
    page.add(eliminar_archivos_temp_app)

if __name__ == "__main__":
    ft.app(target=main)
