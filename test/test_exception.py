import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located as elem_vis, \
    presence_of_element_located as elem_loc, element_to_be_clickable, invisibility_of_element_located
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
        row2_input_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")  # expected error (no waiting time)
        wait = WebDriverWait(driver, 15)
        # row2_input_locator = wait.until(element_to_be_clickable((By.XPATH, "//div[@id='row2']/input")))  # fix the issue
        row2_input_locator.send_keys("Written using python selenium")

        "Push Save button using locator By.name('Save')"
        # save_btn_locator = driver.find_element(By.NAME, "Save") # buggy script
        save_btn_locator = driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']")
        save_btn_locator.click()

        "Verify text saved"
        save_toast_locator = wait.until(elem_vis((By.ID, "confirmation")))
        actual_save_toast = save_toast_locator.text
        assert actual_save_toast == "Row 2 was saved", "Saved Toast Message is incorrect"

    @pytest.mark.exception
    def test_invalid_state(self, driver):
        # Open Page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        wait = WebDriverWait(driver, 10)

        "Clear Input Field"
        # Click edit button
        driver.find_element(By.ID, "edit_btn").click()

        # Locate the textbox
        row1_textbox = driver.find_element(By.CLASS_NAME, "input-field")
        wait.until(element_to_be_clickable(row1_textbox))

        # Clear the text
        row1_textbox.clear()

        "Type text into the field"
        row1_textbox.send_keys("Written using Python Selenium")

        "Verify The saved text"
        # Hit the save button
        wait.until(elem_loc((By.ID, "save_btn"))).click()

        # Verify The success/saved toast-bar
        saved_toast = wait.until(elem_vis((By.ID, "confirmation")))
        assert saved_toast.text == "Row 1 was saved", "Unexpected toast bar message is found"

    @pytest.mark.exception
    def test_stale_element_reference(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        "Find the instructions text element"
        instruction_locator = driver.find_element(By.ID, "instructions")
        assert instruction_locator.is_displayed(), "Instructor is missing"

        "Hit Add Button"
        driver.find_element(By.ID, "add_btn").click()

        "Instruction text should be disappear"
        wait = WebDriverWait(driver, 15)
        assert wait.until(invisibility_of_element_located(instruction_locator), "Instruction text still exist")

    @pytest.mark.exception
    def test_timeout_exception(self, driver):
        # Open Page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add Button
        driver.find_element(By.ID, "add_btn").click()

        # Wait for 3 seconds for the next field is displayed
        wait = WebDriverWait(driver, 13)

        # Verify the Toast Bar appearance for successful adding
        wait.until(elem_vis((By.ID, "confirmation")), "Expected Toast Bar is not displayed")

        # Verify the Second row availability for successful adding
        wait.until(elem_loc((By.ID, "row2")), "Row 2 couldn't be located")
