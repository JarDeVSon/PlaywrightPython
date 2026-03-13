
from playwright.sync_api import Page, expect


class LoginPage:
    """Page Object Model for the Login Page of The Internet."""

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.flash_message = page.locator("#flash")

    def login(self, username: str, password: str) -> None:
        """Perform login action with given credentials."""
        self.username_input.click()
        self.username_input.fill(username)
        self.password_input.click()
        self.password_input.fill(password)
        self.login_button.click()
 