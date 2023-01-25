from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class LoginFailPage(BasePage):
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __fail_toast = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def validate_url(self) -> str:
        """Validated the expected url vs actual url"""
        return super().get_url

    @property
    def get_error_message(self) -> str:
        """Obtaining the actual error message after passing invalid input"""
        return super()._get_text(self.__fail_toast)

    def toast_display(self) -> bool:
        """Validating the error toast availability"""
        super()._waiting_visibility(self.__fail_toast)
        return super()._display_checker(self.__fail_toast)
