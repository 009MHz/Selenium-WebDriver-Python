import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the page
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)

# Type username student into Username field
username_locator = driver.find_element(By.ID, "username")  # finding the elements by ID
username_locator.send_keys("student")  # inserting given value into the fields

# Type password Password123 into Password field
password_locator = driver.find_element(By.NAME, "password")  # finding the elements by the name
password_locator.send_keys("Password123")  # inserting given value into the fields

# Hit Submit button
submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")  # finding the elements by Xpath
submit_locator.click()  # calling the click function from submit elements instance
time.sleep(3)  # adding a waiting time for page is loaded before below scripts is executed

"""Verify new page URL contains proper elements"""
# User is directed to correct page
expected_URL = driver.current_url  # property to validating the elements

# The Page is displaying Logged In Successfully header
success_header_loc = driver.find_element(By.TAG_NAME, "h1")  # finding elements by TAG_NAME (class name)
expected_header = success_header_loc.text  # property to validating the elements

# New page contains expected text ('Congratulations' or 'successfully logged in')
success_subhead_loc = driver.find_element(By.TAG_NAME, "p")  # finding elements by TAG_NAME
expected_subhead = success_subhead_loc.text  # property to validating the elements

# Log out CTA is displayed on the new page
logout_link = driver.find_element(By.LINK_TEXT, 'Log out')

