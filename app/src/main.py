import flet as ft

from StateMachine import StateMachine

def main(page: ft.Page):

    print("Starting")

    state_machine = StateMachine(page)

    page.update()

    print("end")


ft.app(main)
