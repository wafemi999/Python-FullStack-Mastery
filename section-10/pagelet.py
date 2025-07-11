import flet as ft


def main(page: ft.Page):
    def open_pagelet_end_drawer(e):
        pagelet.show_drawer(ed)

    drawer = ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerDestination(
                icon=ft.Icons.ADD_TO_HOME_SCREEN_SHARP, label="Item 1"
            ),
            ft.NavigationDrawerDestination(icon=ft.Icons.ADD_COMMENT, label="Item 2"),
        ],
    )
    ed = ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerDestination(
                icon=ft.Icons.ADD_TO_HOME_SCREEN_SHARP, label="Item 1"
            ),
            ft.NavigationDrawerDestination(icon=ft.Icons.ADD_COMMENT, label="Item 2"),
        ],
    )
    pagelet = ft.Pagelet(
        appbar=ft.AppBar(
            title=ft.Text("Pagelet AppBar Title"), bgcolor=ft.Colors.AMBER_ACCENT
        ),
        content=ft.Container(ft.Text("Pagelet Body"), padding=ft.padding.all(16)),
        bgcolor=ft.Colors.AMBER_100,
        bottom_app_bar=ft.BottomAppBar(
            bgcolor=ft.Colors.BLUE,
            shape=ft.NotchShape.CIRCULAR,
            content=ft.Row(
                controls=[
                    ft.IconButton(icon=ft.Icons.MENU, icon_color=ft.Colors.WHITE),
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE),
                    ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE),
                ]
            ),
        ),
        drawer= drawer,
        end_drawer=ed,
        floating_action_button=ft.FloatingActionButton(
            "Open", on_click=open_pagelet_end_drawer, shape=ft.CircleBorder()
        ),
        floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_FLOAT,
        width=800,
        height=600,
    )

    page.add(pagelet)


ft.app(main)