import flet as ft
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logic.csv_back import Csv_convert


class Csv_convertion(ft.UserControl):
    def __init__(
        self,
        page,
        darkmode: bool = True,
    ) -> None:
        super().__init__()
        self.darkmode = darkmode
        self.page = page

        self.file_name = ft.Text(value="No file selected", size=16)
        self.file_path = ft.Text(value="", size=12)
        self.file_picker = ft.FilePicker(on_result=self.on_file_picked)
        self.page.overlay.append(self.file_picker)

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
            "Convertidor de CSV",
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

        self.mainColumn = ft.Column(controls=[], alignment=ft.MainAxisAlignment.CENTER)

        self.setup_ui()

    ###################################################################################

    def changeTheme(self, e):
        self.darkmode = not self.darkmode
        self.page.theme_mode = (
            ft.ThemeMode.DARK if self.darkmode else ft.ThemeMode.LIGHT
        )
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

    ##################################################################################

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
            self.converCSV()

    def converCSV(self):
        file_path = self.file_path.value
        converter = Csv_convert(file_path)

        try:
            converter.convert()
            dialog = ft.AlertDialog(
                title=ft.Text("Exito"), content=ft.Text("Archivo convertido a Excel")
            )
            self.page.dialog = dialog
            dialog.open = True
            self.page.update()
        except Exception as e:
            dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Ocurrio un error al convertir el archivo"),
            )
            self.page.dialog = dialog
            dialog.open = True
            self.page.update()

    def build(self):
        # cambiamos el tema de la pagina dependiendo del valor de darkMode
        return ft.Column(
            controls=[
                self.cTitle,
                ft.Row([self.theme_button], alignment=ft.MainAxisAlignment.END),
                self.mainColumn,
            ]
        )


def main(page: ft.Page):
    page.title = "Ordenar Elementos"
    ordenar_elementos_app = Csv_convertion(page)
    page.add(ordenar_elementos_app)


if __name__ == "__main__":
    ft.app(target=main)
