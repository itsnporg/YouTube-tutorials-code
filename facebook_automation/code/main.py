import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

fb_url = "https://www.facebook.com/login/"  # login page URL


class FacebookLogin:
    def __init__(self, email, password, browser):
        self.email = email
        self.password = password

        if browser == "Chrome":
            self.driver = webdriver.Chrome(
                executable_path=ChromeDriverManager().install()
            )
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install()
            )

        self.driver.get(fb_url)
        time.sleep(1)

    def login(self):
        email_element = self.driver.find_element_by_id("email")
        email_element.send_keys(self.email)

        password_element = self.driver.find_element_by_id("pass")
        password_element.send_keys(self.password)

        login_button = self.driver.find_element_by_id("loginbutton")
        login_button.click()

        time.sleep(2)


if __name__ == "__main__":
    fb_login = FacebookLogin(
        email="youremail", password="yourpassword", browser="Firefox"
    )  # Browser =  your browser-        chrome/ FIrefox
    fb_login.login()
