from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    # Assign  the locator into protected variable
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")


    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open_page(self):
        """Open The Passed Page"""
        self._driver.get(self.__url)

    def execute_login(self, username: str, password: str):
        """Executing Login Processes, by finding the elements then passing the correct value for respective field"""
        wait = WebDriverWait(self._driver, 10)

        # Type username student into Username field
        wait.until(ec.visibility_of_element_located(self.__username_field))
        self._driver.find_element(self.__username_field).send_keys(username)

        # Type password Password123 into Password field
        wait.until(ec.visibility_of_element_located(self.__password_field))
        self._driver.find_element(self.__password_field).send_keys(password)

        # Hit Submit button
        wait.until(ec.visibility_of_element_located(self.__submit_button))
        self._driver.find_element(self.__submit_button).click()
