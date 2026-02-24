from utils.helpers import *


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        self.username = "//input[@name='username']"
        self.password = "//input[@name='password']"
        self.login_btn = "//button[@type='submit']"
        self.error_msg = "//p[contains(@class,'alert-content-text')]"

    def open(self):
        self.driver.get(self.url)

    def login(self, user, pwd):
        type_text(self.driver, self.username, user)
        type_text(self.driver, self.password, pwd)
        click(self.driver, self.login_btn)

    def get_error(self):
        return self.driver.find_element("xpath", self.error_msg).text