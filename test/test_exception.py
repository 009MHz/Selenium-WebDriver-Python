import pytest
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By


class TestException:
    @pytest.mark.exception
    def test_element_exception(self, driver):
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        """Click Add button on Row 1"""
        # Verify The Row1 is displayed
        row1_locator = driver.find_element(By.ID, "row1")
        assert row1_locator.is_displayed()

        # Click Add button
        add_locator = driver.find_element(By.ID, "add_btn")
        assert add_locator.is_displayed(), "'Add' Button is missing"
        add_locator.click()

        """Row 2 Is displayed"""

        # Verify Row 2 availability
        row2_locator = driver.find_element(By.ID, "row2")
        assert row2_locator.is_displayed(), "Row 2 Is missing"

        # Verify the Toastbar is displayed
        toast_locator = driver.find_element(By.XPATH, "//div[@id='confirmation']")
        actual_toast_msg = toast_locator.text
        assert actual_toast_msg == "Row 2 was added"