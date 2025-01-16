
import flet as ft

class GUI_Appbar(ft.AppBar) :
    
    def __init__(self, back_M) :
        super().__init__(
            title = ft.Text("app"),
            actions = [
                ft.Button(
                    text = "voltar",
                    icon = ft.Icons.PERSON,
                    on_click = lambda e: back_M()
                )
            ]
        )

        
