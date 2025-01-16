
import flet as ft

from AppStates import AppStates

from components.GUI.AppBar import GUI_Appbar

class StateMachine:

    def __init__(self, page: ft.Page):

        self.appStates = AppStates()

        self.page = page

        self.state = "HOME"

        self.history = ["HOME"]

        self.page.appbar = GUI_Appbar(self.back)

        self.load_page()

    def load_page(self):
        self.page.clean()

        self.page.add(
            self.appStates[self.state]()
        )

    def goto(self, state) :
        if state == "BACK":
            self.back()
        if state in self.appStates :

            self.state = state
            self.history.append(self.state)

            self.load_page()
        
    def back(self) :
        if not len(self.history) == 1 : 
            self.history.pop()
            self.state = self.history[-1]

            self.load_page()


