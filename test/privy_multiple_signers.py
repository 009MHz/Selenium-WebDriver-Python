import pytest
import time
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



class TestMultipleAddress:
    def test_login(self, driver):
        wait = WebDriverWait(driver, 20)
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

        "Switch to Enterprise"
        # Click Avatar
        wait.until((ec.presence_of_element_located((By.CSS_SELECTOR, ".avatar:nth-child(2) > .avatar__img")))).click()

        # Click Enterprise
        wait.until(ec.visibility_of_element_located((By.ID, "__BVID__51___BV_tab_button__"))).click()

        # Select Privy Demo
        wait.until(ec.visibility_of_element_located((By.XPATH, "//li[@class='d-flex align-items-center'][2]"))).click()

        "Upload Documents"
        # Click Upload Button
        time.sleep(5)
        wait.until(ec.visibility_of_element_located((By.ID, 'v-step-0'))).click()

        # Hit direct URL
        driver.get("https://app.privy.id/upload/share-only/upload")

        # Select request from other
        wait.until(ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Request From Others"))).click()

        # hit browse
        #wait.until(ec.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "browse"))).click()

        # Upload the docs

        # Find the hidden input element
        file_input = driver.find_element(By.ID, "fileSelector")

        # Execute JavaScript to set the value of the input element
        driver.execute_script("arguments[0].style.display = 'none';", file_input)
        file_input.send_keys("/Users/MHB8700/dummy_docs_2.pdf")

        # upload validation
        upload_file = wait.until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-danger']")))
        upload_file.click()

        success_icon = wait.until(ec.presence_of_element_located((By.CLASS_NAME, "text-success px-1 success-upload")))
        assert success_icon.is_displayed(), "Document not uploaded"
        time.sleep(10)

    @pytest.mark.debug
    def add_recipients(self, driver):
        wait = WebDriverWait(driver, 20)
        driver.get("https://app.privy.id/upload/share-only/share?docToken=cdc3c8b07fecf76bb87dbc32cac1d6b52f4e8567dae4a6fd9a471d25ff0ae004")

        "login with the correct user"
        # Type the username
        username_locator = wait.until(ec.element_to_be_clickable((By.ID, "__BVID__4")))
        username_locator.send_keys("MHB8700")
        cont_button = wait.until(ec.element_to_be_clickable((By.ID, "tag-lg001")))
        cont_button.click()
        cont_button.click()

        # Type the password
        password_locator = wait.until(ec.element_to_be_clickable((By.ID, "__BVID__6")))
        password_locator.send_keys("Geo11787")
        cont_button = wait.until(ec.element_to_be_clickable((By.ID, "tag-lg001")))
        cont_button.click()

        # Wait for the overlay to become invisible
        time.sleep(10)
        # overlay_locator = (By.CLASS_NAME, "overlay overlay-dark")
        # wait.until(ec.invisibility_of_element_located(overlay_locator))

        # Wait for the radio button to become clickable and click it
        radio_locator = (By.XPATH, "//div[@class='custom-control custom-control-inline custom-radio'][2]")
        radio = wait.until(ec.element_to_be_clickable(radio_locator))
        radio.click()

        wait.until(ec.element_to_be_clickable((By.ID, "v-recipient-1"))).click()

        # Type the recipient
        textbox = wait.until(ec.element_to_be_clickable((By. CLASS_NAME, "multiselect__tags")))
        textbox.click()
        textbox.send_keys("mse.01@mailinator.com")
        # new_path = (By.CSS_SELECTOR, "input.multiselect__input[style='width: 100%;']")
        # textbox = wait.until(ec.visibility_of_element_located(new_path))
        # textbox.click()

        time.sleep(10)









        # Request From Others
        # Add recipients using mse001@mailinator.com
        # Select the recipients as reviewer
        # Inspect Network
        # Check the Preserve log
        # Continue