import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestPositiveLogin:
    def test_positive_login(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Hit Submit button
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_locator.click()
        time.sleep(3)

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