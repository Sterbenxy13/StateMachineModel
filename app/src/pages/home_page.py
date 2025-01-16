
import flet as ft

def load(transition_method):
    print("load home_page")

    page = ft.Column(
        controls = [
            ft.Text("Home Page"),
            ft.Button(
                "Register",
                on_click = lambda e: transition_method("REGISTER"),
            )
        ]
    )

    return page



