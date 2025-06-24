import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.bgcolor = ft.Colors.AMBER_700
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Text("My first flet APP!"),
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Container(
                    bgcolor=ft.Colors.BLACK38,
                    height=200,
                    width=200
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)

