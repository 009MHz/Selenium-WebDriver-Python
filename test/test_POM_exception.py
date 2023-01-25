import time

import pytest
from page_objects.exception_page import ExceptionPage


class TestException:
    @pytest.mark.exception
    def test_no_element_exception(self, driver):
        exc = ExceptionPage(driver)
        exc.open_page()
        assert exc.r1_presence(), "Row 1 Can't be found on the page"
        exc.r1_hit_add()
        exc.toast_presence()
        assert exc.r2_presence(), "Row 2 can't be located on the page"
        assert exc.toast_text() == "Row 2 was added", "Added Toast Message is incorrect"

    @pytest.mark.exception
    def test_not_interactable_element(self, driver):
        exc = ExceptionPage(driver)
        exc.open_page()
        exc.r1_hit_add()
        exc.r2_type_text("Written by Python Selenium")
        exc.r2_hit_save()
        assert exc.toast_presence(), "Saved toast bar can't be found on the page"
        assert exc.toast_text() == "Row 2 was saved", "Saved Toast Message is incorrect"

    @pytest.mark.exception
    def test_invalid_state(self, driver):
        exc = ExceptionPage(driver)
        exc.open_page()
        exc.r1_hit_edit()
        assert not exc.r1_input_presence(), "Row 1 textbox is disabled "
        exc.r1_input_clear()
        exc.r1_type_text("Written using Selenium")
        exc.r1_hit_save()
        assert exc.toast_presence(), "Saved toast bar is missing"
        assert exc.toast_text() == "Row 1 was saved", "Unexpected toast bar message is found"

    @pytest.mark.exception
    def test_stale_element_reference(self, driver):
        exc = ExceptionPage(driver)
        exc.open_page()
        exc.inst_presence()
        exc.r1_hit_add()
        assert not exc.inst_absence(), "Instruction text still exist"

    @pytest.mark.exception
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        pass
        # Open Page
        # Click Add Button
        # Wait for 3 seconds for the next field is displayed
        # Verify the Toast Bar appearance for successful adding
        # Verify the Second row availability for successful adding