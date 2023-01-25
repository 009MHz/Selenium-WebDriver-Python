from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    # Assign  the locator into protected variable
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        """Open The Passed Page"""
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        """Executing Login Processes, by finding the elements then passing the correct value for respective field"""
        # Type username student into Username field
        super()._type(self.__username_field, username)

        # Type password Password123 into Password field
        super()._type(self.__password_field, password)

        # Hit Submit button
        super()._click(self.__submit_button)
