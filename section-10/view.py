from flet import *

def starter(page: Page):
    page.title = "First flet App"
    page.bgcolor = Colors.BLUE_400

    view = View(
        route = "/",
        bgcolor= Colors.AMBER_700,
        controls=[
            Container(
                width = 200,
                height = 200,
                bgcolor= Colors.RED_400
            ),
            Card(
                color= Colors.BLACK38,
                margin= 20,
                elevation = 5.0,
                clip_behavior= ClipBehavior.HARD_EDGE,
                content= Container(
                    width = 50,
                    height = 50,
                    bgcolor= Colors.PINK_300
                ),
                shadow_color = Colors.BLUE_ACCENT_700
            )
        ]
    )
    print(page.views)
    page.views.append(view)
    page.go("/")

app(starter)