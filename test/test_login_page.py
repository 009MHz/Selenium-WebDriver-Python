import time
import pytest
from selenium.webdriver.common.by import By


class TestPositiveLogin:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # driver.close() # intentionally issue for debuggin purpose

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Hit Submit button
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_locator.click()

        """Verify new page URL contains proper elements"""
        # User is directed to correct page
        actual_URL = driver.current_url
        assert actual_URL == "https://practicetestautomation.com/logged-in-successfully/"

        # The Page is displaying Logged In Successfully header
        success_header_loc = driver.find_element(By.TAG_NAME, "h1")
        actual_header = success_header_loc.text
        assert actual_header == "Logged In Successfully"

        # New page contains expected text ('Congratulations' or 'successfully logged in')
        success_subhead_loc = driver.find_element(By.TAG_NAME, "p")
        actual_subhead = success_subhead_loc.text
        assert actual_subhead == "Congratulations student. You successfully logged in!"

        # Log out CTA is displayed on the new page
        logout_link = driver.find_element(By.LINK_TEXT, 'Log out')
        assert logout_link.is_displayed()