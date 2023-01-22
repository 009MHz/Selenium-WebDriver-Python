from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._waiting_visibility(locator, time)
        self._find(locator).send_keys(text)

    def _waiting_visibility(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _click(self, locator: tuple, time: int = 10):
        self._waiting_visibility(locator, time)
        self._find(locator).click()

    @property
    def get_url(self) -> str:
        """Obtaining the current URL Value"""
        return self._driver.current_url

    def display_checker(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
