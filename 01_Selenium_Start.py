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

# Type password Password123 into Password field
password_locator = driver.find_element(By.NAME, "password")  # finding the elements by the name

# Hit Submit button
submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")  # finding the elements by Xpath

"""Verify new page URL contains proper elements"""
# success_header_loc = driver.find_element(By.XPATH, "//h1[@class='post-title']") # finding the elements by Xpath
success_header_loc = driver.find_element(By.TAG_NAME, "h1")  # finding elements by TAG_NAME (class name)

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
success_subhead_loc = driver.find_element(By.TAG_NAME, "p")  # finding elements by TAG_NAME

# Verify button Log out is displayed on the new page
logout_link = driver.find_element(By.LINK_TEXT, 'Log out')
    # finding elements by CTA name since the element is not a button but "a" class

