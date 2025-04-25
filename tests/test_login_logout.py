from pages.login_page import LoginPage
from pages.secure_page import SecurePage

def test_successful_login_logout(browser):
    login_page = LoginPage(browser)
    secure_page = SecurePage(browser)

    login_page.load()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in secure_page.get_flash_message()

    secure_page.logout()
    assert "You logged out of the secure area!" in login_page.get_error_message()

def test_invalid_login(browser):
    login_page = LoginPage(browser)

    login_page.load()
    login_page.login("wronguser", "wrongpass")

    assert "Your username is invalid!" in login_page.get_error_message()
