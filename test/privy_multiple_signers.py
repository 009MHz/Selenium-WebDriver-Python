import time
import selenium.webdriver.support.expected_conditions as ec

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



class TestMultipleAddress:
    def login(self, driver):
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
        # upload_sidebar
        driver.get("https://app.privy.id/upload/share-only/upload")
        # wait.until(ec.visibility_of_element_located((By.ID, 'v-step-0'))).click()

        # hit request from other
        # wait.until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Request From Others"))).click()

        # hit browse
        wait.until(ec.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "browse"))).click()

        # Upload the docs
        upload_docs = driver.find_element(By.XPATH, "//input[@id='fileSelector']")
        # upload_docs = driver.find_element(By.XPATH, "//input[@name='filename']")
        upload_docs.send_keys("/Users/MHB8700/dummy_docs_2.pdf")

        # upload validation
        upload_file = wait.until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-danger']")))
        upload_file.click()

        success_icon = wait.until(ec.presence_of_element_located((By.CLASS_NAME, "text-success px-1 success-upload")))
        assert success_icon.is_displayed(), "Document not uploaded"
        time.sleep(10)

    def test_add_recipients(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get("https://app.privy.id/upload/share-only/share?docToken=cdc3c8b07fecf76bb87dbc32cac1d6b52f4e8567dae4a6fd9a471d25ff0ae004")

        "login with the correct user"
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

        "Setup the method"
        wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='__BVID__177']"))).click()  # serial method
        wait.until(ec.visibility_of_element_located((By.ID, "v-recipient-1"))).click()  # add recipient button

        # Type the recipient
        textbox = wait.until(ec.element_to_be_clickable(By. CLASS_NAME, "multiselect__input"))
        textbox.send_keys("mse.01@mailinator.com")
        time.sleep(10)









        # Request From Others
        # Add recipients using mse001@mailinator.com
        # Select the recipients as reviewer
        # Inspect Network
        # Check the Preserve log
        # Continue