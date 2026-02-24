from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.decorators import capture_screenshot_on_fail


class TestLogin:

    @capture_screenshot_on_fail
    def test_valid_login(self, driver):

        self.driver = driver

        login = LoginPage(driver)
        dash = DashboardPage(driver)

        login.open()
        login.login("Admin", "admin123")

        assert dash.is_logged_in()