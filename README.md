State Machine Model for flet app

This is a model for manage app pages, it contains a AppState class that init the states in Python Dict pattern, with the state as key, and the page load function as the value, and a State Machine class that manage the states in the app.


class AppState:

    "HOME": pages.home_page.load,


class StateMachine:

    self.appstates: instance of AppStates class.

    self.page: the page by itself.

    self.state: the current state in app.
    
    self.history: list of states keys, it will be used as a stack.

    self.load_page(): clean the page and load the new page from the current state. It gives self.goto_page as a parameter for pages load function, so that can contains links to navigate between other pages.

    self.goto_page(state): method used for transitioning to a new state, if state parameter is "BACK", it calls self.back().

    self.back(): method used for back in self.history state, it deletes the last state in self.history and loads the new last state.

The StateMachine class must be instantiated at main(), and the app will run naturally.
