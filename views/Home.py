#home

import flet as ft

class Home(ft.UserControl):
    def __init__(self, darkMode: bool = True) -> None:
        super().__init__()
        self.darkMode = darkMode
        self.container = ft.Container(bgcolor="#2A363B")
        
        self.emailsHome_button = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.SEND_ROUNDED, color="green400", size=20),
                            ft.Text("Enviar", size=16),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    #on_click=self.send_email,
                    style=ft.ButtonStyle(
                        overlay_color="#99B898",
                        bgcolor="none",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        side=ft.BorderSide(color="green400", width=2),
                        shadow_color="grey600",
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
                            ft.Icon(ft.icons.SEND_ROUNDED, color="green400", size=20),
                            ft.Text("Enviar", size=16),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    #on_click=self.send_email,
                    style=ft.ButtonStyle(
                        overlay_color="#99B898",
                        bgcolor="none",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        side=ft.BorderSide(color="green400", width=2),
                        shadow_color="grey600",
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
        self.test3_button = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.SEND_ROUNDED, color="green400", size=20),
                            ft.Text("Enviar", size=16),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    #on_click=self.send_email,
                    style=ft.ButtonStyle(
                        overlay_color="#99B898",
                        bgcolor="none",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        side=ft.BorderSide(color="green400", width=2),
                        shadow_color="grey600",
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
        self.test4_button = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.SEND_ROUNDED, color="green400", size=20),
                            ft.Text("Enviar", size=16),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    #on_click=self.send_email,
                    style=ft.ButtonStyle(
                        overlay_color="#99B898",
                        bgcolor="none",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        side=ft.BorderSide(color="green400", width=2),
                        shadow_color="grey600",
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
        self.test5_button = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.SEND_ROUNDED, color="green400", size=20),
                            ft.Text("Enviar", size=16),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    #on_click=self.send_email,
                    style=ft.ButtonStyle(
                        overlay_color="#99B898",
                        bgcolor="none",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        side=ft.BorderSide(color="green400", width=2),
                        shadow_color="grey600",
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
        
        self.container1 = ft.Container(
            self.emailsHome_button,
            expand=True, height= 280
        )
        self.container2 = ft.Container(
            self.ordenarHome_button,
            expand=True, height= 280
        )
        self.container3 = ft.Container(
            self.test3_button,
            expand=True, height= 280
        )
        self.container4 = ft.Container(
            self.test3_button,
            expand=True, height= 280
        )
        self.container5 = ft.Container(
            self.test4_button,
            expand=True, height= 280
        )
        self.container6 = ft.Container(
            ft.Text("container 6"),
            expand=True, height= 280
        )

    def build(self):
        # Cambiamos el tema de la página dependiendo del valor de darkMode
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                ft.Container(ft.Text("BIENVENIDO", size=48), margin=ft.margin.only(20))
                
                    ],
                 alignment=ft.MainAxisAlignment.CENTER
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
                )
            ]
        )
