import time
import pytest
from selenium.webdriver.common.by import By


class TestNegativeLogin:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize(
        "username, password, error_message",
        [
            ("invalid_name", "Password123", "Your username is invalid!"),
            ("student", "invalid_pass", "Your password is invalid!")
        ])
    def test_negative_login(self, driver, username, password, error_message):
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type the Password into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        # Hit Submit button
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        err_locator = driver.find_element(By.ID, "error")
        assert err_locator.is_displayed(), "Error Message is missing"

        # Verify error message text is correct
        actual_err_text = err_locator.text
        assert actual_err_text == error_message, "Displayed error is incorrect"