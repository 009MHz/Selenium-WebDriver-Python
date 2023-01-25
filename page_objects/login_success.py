from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoginSuccessPage(BasePage):
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __header = (By.TAG_NAME, "h1")
    __sub_header = (By.TAG_NAME, "p")
    __logout_CTA = (By.LINK_TEXT, 'Log out')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def validate_url(self) -> str:
        """Validated the expected url vs actual url"""
        return super().get_url

    @property
    def get_header(self) -> str:
        """Obtaining the actual header text on the loaded page"""
        return super()._get_text(self.__header)

    @property
    def get_sub_header(self) -> str:
        """Obtaining the actual sub header text on the loaded page"""
        return super()._get_text(self.__sub_header)

    def logout_validator(self) -> bool:
        """Validate the logout CTA availability"""
        return super()._display_checker(self.__logout_CTA)