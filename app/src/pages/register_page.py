
import flet as ft

def load(transition_method):
    print("load register_page")

    username_input = ft.TextField(
        label = "username",
        value = "",
    )
    password_input =  ft.TextField(
        label = "password",
        value = "",
        password = True,
    )

    page = ft.Column(
        controls = [
            ft.Text(
                "register:"
            ),
            username_input,
            password_input,
            ft.FilledButton(
                text = "Register",
                on_click = lambda e: transition_method("BACK")
            )
        ]
    )

    return page
