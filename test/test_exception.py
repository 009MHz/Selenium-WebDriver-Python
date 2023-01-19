import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located as elem_vis, \
    presence_of_element_located as elem_loc
from selenium.webdriver.support.wait import WebDriverWait


class TestException:
    @pytest.mark.exception
    def test_no_element_exception(self, driver):
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
        wait = WebDriverWait(driver, 15)

        # Verify the Toast bar is displayed
        toast_locator = wait.until(elem_vis((By.ID, "confirmation")))
        actual_toast_msg = toast_locator.text
        assert actual_toast_msg == "Row 2 was added", "Added Toast Message is incorrect"

        # Verify Row 2 availability
        row2_locator = wait.until(elem_loc((By.ID, "row2")))
        assert row2_locator.is_displayed(), "Row 2 Is missing"

    @pytest.mark.exception
    def test_not_intractable_element(self, driver):
        # Open The Page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        "Click Add button on Row 1"
        driver.find_element(By.ID, "add_btn").click()

        "Type text into the second input field"
        # Pass the text to the text box
        row2_input_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        row2_input_locator.send_keys("Written using python selenium")

        "Push Save button using locator By.name('Save')"
        # save_btn_locator = driver.find_element(By.NAME, "Save") # buggy script
        save_btn_locator = driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']")
        save_btn_locator.click()

        "Verify text saved"
        wait = WebDriverWait(driver, 30)
        save_toast_locator = wait.until(elem_vis((By.ID, "confirmation")))
        actual_save_toast = save_toast_locator.text
        assert actual_save_toast == "Row 2 was saved", "Saved Toast Message is incorrect"

    @pytest.mark.exception
    @pytest.mark.debug
    def test_invalid_state(self, driver):
        # Open Page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        wait = WebDriverWait(driver, 3)

        "Clear Input Field"
        # Locate the textbox
        row1_textbox = driver.find_element(By.XPATH, "//div[@id='row1']/input")

        # Clear the text
        row1_textbox.clear()

        "Type Text into Input Field"
        row1_textbox.send_keys("Written Using Python Selenium")

        "Verify Text Changed"
        # Click save
        wait.until(elem_loc((By.NAME, "Save"))).click()

        # Verify the toast message
        toast_saved = wait.until(elem_vis((By.ID, "confirmation")))
        toast_expected = toast_saved.text
        assert toast_expected == "Row 1 was saved", "Saved toast message is not following the criteria"