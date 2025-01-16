
import pages.home_page
import pages.register_page

class AppStates(dict):
    def __new__(cls):
        return {
            "HOME": pages.home_page.load,
            "REGISTER": pages.register_page.load,
            # "LOGIN": pages.login_page.load,
            # "SEARCH_USERS": pages.searchUsers_page.load,
            # "PROFILE": pages.profile_page.load,
        }
