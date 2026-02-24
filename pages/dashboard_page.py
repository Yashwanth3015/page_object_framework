from utils.helpers import *


class DashboardPage:

    def __init__(self, driver):

        self.driver = driver

        self.profile = "//p[@class='oxd-userdropdown-name']"
        self.logout_btn = "//a[text()='Logout']"
        self.dashboard = "//h6[text()='Dashboard']"

    def is_logged_in(self):
        wait_for(self.driver, self.dashboard)
        return True

    def logout(self):
        click(self.driver, self.profile)
        click(self.driver, self.logout_btn)