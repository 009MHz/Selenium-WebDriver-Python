import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    print("Creating Chrome Driver . . .")
    test_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield test_driver
    print("\nChrome Driver is created, exiting the processes. . .\n")
    test_driver.quit()


class TestNegativeLogin:

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self, driver):
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type invalid username into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("invalid")

        # Type Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Hit Submit button
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        err_locator = driver.find_element(By.ID, "error")
        assert err_locator.is_displayed(), "Username Error Message is missing"

        # Verify error message text is Your username is invalid!
        actual_err_text = err_locator.text
        assert actual_err_text == "Your username is invalid!"

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_password(self, driver):
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type valid username into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type invalid password into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("invalid321")

        # Hit Submit button
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        err_locator = driver.find_element(By.ID, "error")
        assert err_locator.is_displayed(), "Password Error Message is missing"

        # Verify error message text is Your username is invalid!
        actual_err_text = err_locator.text
        assert actual_err_text == "Your password is invalid!"
