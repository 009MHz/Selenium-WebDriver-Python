import pytest
from page_objects.login_page import LoginPage
from page_objects.login_fail_page import LoginFailPage


class TestNegativeLogin:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize(
        "username, password, error_message",
        [
            ("invalid_name", "Password123", "Your username is invalid!"),
            ("student", "invalid_pass", "Your password is invalid!")
        ])
    def test_negative_login(self, driver, username, password, error_message):
        login_control = LoginPage(driver)
        negative_validator = LoginFailPage(driver)
        # Open the page
        login_control.open_page()

        # Type invalid username & Password into respective field
        # Hit Submit button
        login_control.execute_login(username, password)

        # Verify error message is displayed

        assert negative_validator.toast_display(), "Fail toast bar is not displayed"

        # Verify error message text is correct
        assert negative_validator.get_error_message == error_message, "Error message is not as expected"