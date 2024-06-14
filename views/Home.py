# home

import flet as ft


class Home(ft.UserControl):
    def __init__(self, darkmode: bool = True) -> None:
        super().__init__()
        
        
        self.darkmode = darkmode

        self.emailsHome_button = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.EMAIL, color="#a9916b", size=20),
                            ft.Text("Email", size=16, color="#e3d6ab"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    # on_click=self.send_email,
                    style=ft.ButtonStyle(
                        overlay_color="#99B898",
                        bgcolor="none",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        side=ft.BorderSide(color="#778979", width=2),
                        shadow_color="#778979",
                        elevation=5,
                        color={
                            ft.MaterialState.HOVERED: "white",
                            ft.MaterialState.PRESSED: "white",
                        },
                    ),
                    width=370,
                    height=250,
                    animate_scale=True,
                    scale=1.1,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self.ordenarHome_button = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.FOLDER, color="#a9916b", size=20),
                            ft.Text("Extensiones", size=16, color="#e3d6ab"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    # on_click=self.send_email,
                    style=ft.ButtonStyle(
                        overlay_color="#99B898",
                        bgcolor="none",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        side=ft.BorderSide(color="#778979", width=2),
                        shadow_color="#778979",
                        elevation=5,
                        color={
                            ft.MaterialState.HOVERED: "white",
                            ft.MaterialState.PRESSED: "white",
                        },
                    ),
                    width=370,
                    height=250,
                    animate_scale=True,
                    scale=1.1,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self.crearEmailHome_button = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(
                                ft.icons.MARK_EMAIL_READ_SHARP,
                                color="#a9916b",
                                size=20,
                            ),
                            ft.Text("Crear Email", size=16, color="#e3d6ab"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    # on_click=self.send_email,
                    style=ft.ButtonStyle(
                        overlay_color="#99B898",
                        bgcolor="none",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        side=ft.BorderSide(color="#778979", width=2),
                        shadow_color="#778979",
                        elevation=5,
                        color={
                            ft.MaterialState.HOVERED: "white",
                            ft.MaterialState.PRESSED: "white",
                        },
                    ),
                    width=370,
                    height=250,
                    animate_scale=True,
                    scale=1.1,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self.eliminarTempHome_button = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.DELETE, color="#a9916b", size=20),
                            ft.Text(
                                "Eliminar Archivos Temporales", size=16, color="#e3d6ab"
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    # on_click=self.send_email,
                    style=ft.ButtonStyle(
                        overlay_color="#99B898",
                        bgcolor="none",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        side=ft.BorderSide(color="#778979", width=2),
                        shadow_color="#778979",
                        elevation=5,
                        color={
                            ft.MaterialState.HOVERED: "white",
                            ft.MaterialState.PRESSED: "white",
                        },
                    ),
                    width=370,
                    height=250,
                    animate_scale=True,
                    scale=1.1,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self.convertirCSVHome_button = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.TABLE_CHART, color="#a9916b", size=20),
                            ft.Text("Convertir CSV", size=16, color="#e3d6ab"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    # on_click=self.send_email,
                    style=ft.ButtonStyle(
                        overlay_color="#99B898",
                        bgcolor="none",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        side=ft.BorderSide(color="#778979", width=2),
                        shadow_color="#778979",
                        elevation=5,
                        color={
                            ft.MaterialState.HOVERED: "white",
                            ft.MaterialState.PRESSED: "white",
                        },
                    ),
                    width=370,
                    height=250,
                    animate_scale=True,
                    scale=1.1,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.test6_button = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.TABLE_CHART, color="#a9916b", size=20),
                            ft.Text("Test 6", size=16, color="#e3d6ab"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    # on_click=self.send_email,
                    style=ft.ButtonStyle(
                        overlay_color="#99B898",
                        bgcolor="none",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        side=ft.BorderSide(color="#778979", width=2),
                        shadow_color="#778979",
                        elevation=5,
                        color={
                            ft.MaterialState.HOVERED: "white",
                            ft.MaterialState.PRESSED: "white",
                        },
                    ),
                    width=370,
                    height=250,
                    animate_scale=True,
                    scale=1.1,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.container1 = ft.Container(self.emailsHome_button, expand=True, height=280)
        self.container2 = ft.Container(self.ordenarHome_button, expand=True, height=280)
        self.container3 = ft.Container(
            self.crearEmailHome_button, expand=True, height=280
        )
        self.container4 = ft.Container(
            self.convertirCSVHome_button, expand=True, height=280
        )
        self.container5 = ft.Container(
            self.eliminarTempHome_button, expand=True, height=280
        )
        self.container6 = ft.Container(self.test6_button, expand=True, height=280)
        

    def build(self):
        # Cambiamos el tema de la página dependiendo del valor de darkmode
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            ft.Text(
                                "BIENVENIDO",
                                size=48,
                                font_family="georgia",
                                color="#FECEA8",
                            ),
                            margin=ft.margin.only(20),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            ft.Text(
                                "BIENVENIDO",
                                size=16,
                                font_family="georgia",
                                color="#b89789",
                            ),
                            margin=ft.margin.only(20),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        self.container1,
                        self.container2,
                        self.container3,
                    ]
                ),
                ft.Row(
                    controls=[
                        self.container4,
                        self.container5,
                        self.container6,
                    ]
                ),
            ]
        )
