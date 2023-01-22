from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginSuccessPage:
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __header = (By.TAG_NAME, "h1")
    __sub_header = (By.TAG_NAME, "p")
    __logout_CTA = (By.LINK_TEXT, 'Log out')

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def get_url(self) -> str:
        """Obtaining the current URL Value"""
        return self._driver.current_url

    @property
    def validate_url(self) -> str:
        """Validated the expected url vs actual url"""
        return self._url

    @property
    def get_header(self) -> str:
        """Obtaining the actual header text on the loaded page"""
        return self._driver.find_element(self.__header).text

    @property
    def get_sub_header(self) -> str:
        """Obtaining the actual sub header text on the loaded page"""
        return self._driver.find_element(self.__sub_header).text

    def logout_validator(self) -> bool:
        """Validate the logout CTA availability"""
        return self._driver.find_element(self.__logout_CTA).is_displayed()