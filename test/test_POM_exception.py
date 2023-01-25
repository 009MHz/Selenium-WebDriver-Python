import time

import pytest
from page_objects.exception_page import ExcPage


class TestException:
    @pytest.mark.exception
    def test_no_element_exception(self, driver):
        exc = ExcPage(driver)
        exc.open_page()
        assert exc.r1_presence(), "Row 1 Can't be found on the page"
        exc.r1_hit_add()
        exc.toast_presence()
        assert exc.r2_presence(), "Row 2 can't be located on the page"
        assert exc.toast_text() == "Row 2 was added", "Added Toast Message is incorrect"

    @pytest.mark.exception
    def test_not_interactable_element(self, driver):
        exc = ExcPage(driver)
        exc.open_page()
        exc.r1_hit_add()
        exc.r2_type_text("Written by Python Selenium")
        exc.r2_hit_save()
        assert exc.toast_presence(), "Saved toast bar can't be found on the page"
        assert exc.toast_text() == "Row 2 was saved", "Saved Toast Message is incorrect"

    @pytest.mark.exception
    @pytest.mark.debug
    def test_invalid_state(self, driver):
        pass
        # Open Page
        "Clear Input Field"
        # Click edit button
        # Locate the textbox
        # Clear the text
        "Type text into the field"
        "Verify The saved text"
        # Hit the save button
        # Verify The success/saved toast-bar