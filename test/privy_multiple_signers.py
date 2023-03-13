import time
import pyautogui
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import os


class TestMultipleAddress:
    def test_positive(self, driver):
        wait = WebDriverWait(driver, 15)
        """Login The Page"""
        # Open The page
        driver.get("https://app.privy.id/dashboard")

        # Pass the user & Password
        username_locator = wait.until(ec.element_to_be_clickable((By.ID, "__BVID__4")))
        username_locator.send_keys("MHB8700")
        cont_button = wait.until(ec.element_to_be_clickable((By.ID, "tag-lg001")))
        cont_button.click()
        cont_button.click()
        # Pass the password
        password_locator = wait.until(ec.element_to_be_clickable((By.ID, "__BVID__6")))
        password_locator.send_keys("Geo11787")
        cont_button = wait.until(ec.element_to_be_clickable((By.ID, "tag-lg001")))
        cont_button.click()

        # Switch to Enterprise
        ava_loc = wait.until((ec.presence_of_element_located((By.ID, "v-step-3__BV_button_"))))
        ava_loc.click()

        enterp_loc = wait.until(ec.visibility_of_element_located((By.ID, "__BVID__51___BV_tab_button__")))
        enterp_loc.click()

        demo_loc = wait.until(ec.presence_of_element_located((By.XPATH, "//li[@class='d-flex align-items-center'][2]")))
        demo_loc.click()

        # Upload Documents
        upload_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//button[@id='v-step-0']")))
        upload_locator.click()

        upload_req_locator = wait.until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Request From Others")))
        upload_req_locator.click()

        # upload_docs = wait.until(ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "browse")))
        # upload_docs.click()

        driver.find_element(By.ID, "fileSelector").send_keys("/Users/MHB8700/dummy_docs_2.pdf")
        time.sleep(10)



        # pyautogui.typewrite("/Users/MHB8700/dummy_docs_2.pdf")
        # time.sleep(3)
        # pyautogui.press("Enter")
        # pyautogui.press("Open")







        # Request From Others
        # Add recipients using mse001@mailinator.com
        # Select the recipients as reviewer
        # Inspect Network
        # Check the Preserve log
        # Continue