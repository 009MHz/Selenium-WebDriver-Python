import pytest
from page_objects.exception_page import ExcPage


class TestException:
    @pytest.mark.exception
<<<<<<< HEAD
=======
    @pytest.mark.debug
>>>>>>> origin/master
    def test_no_element_exception(self, driver):
        exc = ExcPage(driver)
        exc.open_page()
        assert exc.r1_presence(), "Row 1 Can't be found on the page"
        exc.r1_hit_add()
        exc.toast_presence()
        assert exc.r2_presence(), "Row 2 can't be located on the page"
        assert exc.toast_text() == "Row 2 was added", "Added Toast Message is incorrect"
<<<<<<< HEAD

    @pytest.mark.exception
    @pytest.mark.debug
    def test_not_intractable_element(self, driver):
        exc = ExcPage(driver)
        # Open The Page
        exc.open_page()
        "Click Add button on Row 1"
        exc.r1_hit_add()
        "Type text into the second input field"
        # Pass the text to the text box
        exc.r2_type_text("Written by Python Selenium")
        "Push Save button using locator By.name('Save')"
        exc.r2_hit_save()
        "Verify text saved"
        # Verify the toast appearance
        assert exc.toast_presence(), "Saved toast bar can't be found on the page"
        # Verify the toast message
        assert exc.toast_text() == "Row 2 was saved", "Saved Toast Message is incorrect"
=======
>>>>>>> origin/master
