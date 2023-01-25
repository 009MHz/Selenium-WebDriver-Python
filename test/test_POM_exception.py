import pytest
from page_objects.exception_page import ExcPage


class TestException:
    @pytest.mark.exception
    @pytest.mark.debug
    def test_no_element_exception(self, driver):
        exc = ExcPage(driver)
        exc.open_page()
        assert exc.r1_presence(), "Row 1 Can't be found on the page"
        exc.r1_hit_add()
        exc.toast_presence()
        assert exc.r2_presence(), "Row 2 can't be located on the page"
        assert exc.toast_text() == "Row 2 was added", "Added Toast Message is incorrect"
