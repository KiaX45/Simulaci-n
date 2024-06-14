import flet as ft
import os
import shutil
import tempfile
import pathlib


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
        self.page.theme_mode = (
            ft.ThemeMode.DARK if self.darkmode else ft.ThemeMode.LIGHT
        )

        self.cTitle_text = ft.Text(
            "ELIMINAR ARCHIVOS TEMPORALES",
            size=40,
            font_family="georgia",
            color="#FECEA8" if self.darkmode else "black",
        )

        self.cDescription_text = ft.Text(
            "               Nuestro asistente digital elimina automáticamente archivos temporales y datos innecesarios, \n manteniendo tu sistema limpio y eficiente para que puedas concentrarte en lo que realmente importa",
            size=16,
            font_family="georgia",
            color="#b89789",
        )

        self.text_container = ft.Container(
            self.cTitle_text, alignment=ft.alignment.center
        )

        self.cTitle = ft.Container(
            ft.Row(
                [
                    self.text_container,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.padding.only(1),
            margin=ft.margin.only(1, 30),
        )

        self.iconButton = (
            ft.icons.DARK_MODE if not self.darkmode else ft.icons.LIGHT_MODE
        )
        self.theme_button = ft.ElevatedButton(
            "Dark", self.iconButton, on_click=self.changeTheme
        )

        self.button_delete_temp = ft.ElevatedButton(
            "Eliminar Archivos Temporales",
            icon=ft.icons.DELETE,
            on_click=self.eliminar_archivos_temporales,
            style=ft.ButtonStyle(
                overlay_color="#ff580f",
                bgcolor="none",
                shape=ft.RoundedRectangleBorder(radius=12),
                side=ft.BorderSide(color="red400", width=1),
                shadow_color="grey600",
                elevation=5,
            ),
            width=300,
            height=45,
        )

        self.result_container = ft.Column()

        self.build_ui()

    def build_ui(self):
        self.page.controls.clear()
        self.page.controls.append(self.cTitle)
        self.page.controls.append(
            ft.Row([self.theme_button], alignment=ft.MainAxisAlignment.END)
        )
        self.page.controls.append(
            ft.Row([self.button_delete_temp], alignment=ft.MainAxisAlignment.CENTER)
        )
        self.page.controls.append(self.result_container)
        self.page.update()

    def changeTheme(self, e):
        self.darkmode = not self.darkmode
        self.page.theme_mode = (
            ft.ThemeMode.DARK if self.darkmode else ft.ThemeMode.LIGHT
        )
        self.page.bgcolor = "#2A363B" if self.darkmode else "#F4F4F4"
        self.cTitle_text.color = "#FECEA8" if self.darkmode else "#434b4d"
        self.cDescription_text.color = color = "#b89789" if self.darkmode else "#434b4d"

        self.updateThemeButton()
        self.page.update()

    def updateThemeButton(self):
        iconButton = ft.icons.DARK_MODE if not self.darkmode else ft.icons.LIGHT_MODE
        self.theme_button.icon = iconButton
        self.theme_button.text = "Light" if not self.darkmode else "Dark"

    def eliminar_archivos_temporales(self, e):
        temp_dirs = [
            tempfile.gettempdir(),
            os.path.join(os.environ["SystemRoot"], "Temp"),
            os.path.expandvars("%temp%"),
            os.path.join(
                os.environ["USERPROFILE"],
                "AppData",
                "Local",
                "Microsoft",
                "Windows",
                "INetCache",
            ),
            os.path.join(
                os.environ["USERPROFILE"],
                "AppData",
                "Local",
                "Microsoft",
                "Windows",
                "Explorer",
            ),
        ]
        archivos_eliminados = []

        for temp_dir in temp_dirs:
            archivos_eliminados += self.eliminar_archivos_en_directorio(temp_dir)

        if archivos_eliminados:
            self.mostrar_resultados(archivos_eliminados)
        else:
            self.mostrar_resultados(["No se eliminaron archivos temporales."])

    def eliminar_archivos_en_directorio(self, directorio):
        archivos_eliminados = []
        for root, dirs, files in os.walk(directorio):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    archivos_eliminados.append(file_path)
                    print(f"Archivo eliminado: {file_path}")
                except Exception as ex:
                    print(f"No se pudo eliminar el archivo {file_path}. Error: {ex}")
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    shutil.rmtree(dir_path)
                    archivos_eliminados.append(dir_path)
                    print(f"Directorio eliminado: {dir_path}")
                except Exception as ex:
                    print(f"No se pudo eliminar el directorio {dir_path}. Error: {ex}")
        return archivos_eliminados

    def mostrar_resultados(self, archivos_eliminados):
        self.result_container.controls.clear()
        self.result_container.controls.append(ft.Text("Archivos eliminados con éxito:"))

        for archivo in archivos_eliminados:
            self.result_container.controls.append(ft.Text(archivo))

        self.page.update()

    def build(self):
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[self.cTitle],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[ft.Container(self.cDescription_text)],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row([self.theme_button], alignment=ft.MainAxisAlignment.END),
                ft.Row(
                    [self.button_delete_temp], alignment=ft.MainAxisAlignment.CENTER
                ),
                self.result_container,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.ALWAYS,  # Asegurarse de que el scroll esté habilitado
        )


def main(page: ft.Page):
    page.title = "Eliminar Archivos Temporales"
    eliminar_archivos_temp_app = EliminarArchivosTemporales(page)
    page.add(eliminar_archivos_temp_app.build())


if __name__ == "__main__":
    ft.app(target=main)
