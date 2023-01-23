import pytest
from page_objects.login_page import LoginPage
from page_objects.login_success import LoginSuccessPage


class TestPositiveLogin:
    @pytest.mark.login
    @pytest.mark.positive
    @pytest.mark.debug
    def test_positive_login(self, driver):
        login_control = LoginPage(driver)
        login_verificator = LoginSuccessPage(driver)

        # Open page
        login_control.open_page()

        # Type username student into Username field
        # Type password Password123 into Password field
        # Push Submit button
        login_control.execute_login("student", "Password123")

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        # Verify button Log out is displayed on the new page

        assert login_verificator.validate_url == login_verificator.get_url, "Actual URL is not the same as expected"
        assert login_verificator.get_header == "Logged In Successfully", "Header is not expected"
        assert login_verificator.get_sub_header == "Congratulations student. You successfully logged in!", \
            "Sub Header is not as expected"
        assert login_verificator.logout_validator(), "Logout CTA is not discoverable"
