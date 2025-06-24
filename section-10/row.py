from flet import *

def main(page: Page):
    page.title = "First flet App"
    page.bgcolor = Colors.BLUE_400

    view = View(
        route = "/",
        bgcolor= Colors.AMBER_700,
        controls=[
            Row(
                controls=[
                    Container(bgcolor=Colors.RED, width=100, height=100),
                    Container(bgcolor=Colors.BLUE, width=100, height=100),
                    Container(bgcolor=Colors.GREEN, width=100, height=100),
                    Container(bgcolor=Colors.YELLOW, width=100, height=100),
                    Container(bgcolor=Colors.PINK, width=100, height=100),
                    Container(bgcolor=Colors.WHITE, width=100, height=100),
                    Container(bgcolor=Colors.BLACK, width=100, height=100),
                    Container(bgcolor=Colors.LIGHT_BLUE_200, width=100, height=100),
                    Container(bgcolor=Colors.CYAN, width=100, height=100),
                    Container(bgcolor=Colors.BROWN, width=100, height=100),
                ]
            )
        ]
    )
    page.views.append(view)
    page.go("/")

app(main)