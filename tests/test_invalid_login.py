from pages.login_page import LoginPage
from utils.decorators import capture_screenshot_on_fail


class TestInvalidLogin:

    @capture_screenshot_on_fail
    def test_wrong_password(self, driver):

        self.driver = driver

        login = LoginPage(driver)

        login.open()
        login.login("Admin", "wrong123")

        assert "Invalid credentials" in login.get_error()