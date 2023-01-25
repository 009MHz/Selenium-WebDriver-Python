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
    def test_invalid_state(self, driver):
        exception = ExcPage(driver)
        exception.open_page()
        exception.r1_hit_edit()
        assert not exception.r1_input_presence(), "Row 1 textbox is disabled "
        exception.r1_input_clear()
        exception.r1_type_text("Written using Selenium")
        exception.r1_hit_save()
        assert exception.toast_presence(), "Saved toast bar is missing"
        assert exception.toast_text() == "Row 1 was saved", "Unexpected toast bar message is found"

    @pytest.mark.exception
    @pytest.mark.debug
    def test_stale_element_reference(self, driver):
        pass
        # Open page
        "Find the instructions text element"
        "Hit Add Button"
        "Instruction text should be disappear"