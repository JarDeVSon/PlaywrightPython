from utils.highlight import highlight
from playwright.sync_api import expect

class TestLogin:
    """Test suite for the Login Page of The Internet."""
    def test_login_page_object(self, login_page):
        login_page.login("tomsmith", "SuperSecretPassword!")
        expect(login_page.flash_message).to_contain_text("You logged into a secure area!")
        highlight(login_page.flash_message)
        