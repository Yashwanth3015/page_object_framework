from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.decorators import capture_screenshot_on_fail


class TestLogout:

    @capture_screenshot_on_fail
    def test_logout(self, driver):

        self.driver = driver

        login = LoginPage(driver)
        dash = DashboardPage(driver)

        login.open()
        login.login("Admin", "admin123")

        dash.logout()

        assert "login" in driver.current_url.lower()