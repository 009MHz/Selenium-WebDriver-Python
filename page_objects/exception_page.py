from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver



class ExceptionPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __row1 = (By.ID, "row1")
    __input1 = (By.XPATH, "//div[@id='row1']/input")
    __add = (By.ID, "add_btn")
    __edit = (By.ID, "edit_btn")
    __row2 = (By.ID, "row2")
    __input2 = (By.XPATH, "//div[@id='row2']/input")
    __toast = (By.ID, "confirmation")
    __row1save = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __row2save = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __instructions = (By.ID, "instructions")

    def __init__(self, driver=WebDriver):
        super().__init__(driver)


    def open_page(self):
        """Open the Exception Page URL"""
        super()._open_url(self.__url)

    def r1_presence(self) -> bool:
        """Validating row 1 availability"""
        super()._waiting_visibility(self.__row1)
        return super()._display_checker(self.__row1)

    def r1_hit_add(self):
        """Hit 'Add' button on the row 1"""
        super()._click(self.__add)

    def r1_hit_edit(self):
        """Hit 'Edit' button on the row 1"""
        super()._click(self.__edit)

    def r1_input_is_clickable(self) -> bool:
        """Validating r1 input availability editable/uneditable"""
        return super()._waiting_clickable(self.__input1)

    def r1_type_text(self, text: str):
        """Inserting text on the Row 1 textbox"""
        super()._type(self.__input1, text)

    def r1_input_clear(self):
        """Clearing all values on the Row 1 textbox"""
        super()._find(self.__input1).clear()

    def r1_hit_save(self):
        """Hit 'Save' button on the `row 1`"""
        super()._click(self.__row1save)


    def r2_presence(self) -> bool:
        """Waiting for row 2 assets to be displayed"""
        super()._waiting_visibility(self.__row2, time=15)
        return super()._display_checker(self.__row2)

    def r2_type_text(self, text: str):
        """Inserting text on the Row 2 textbox"""
        super()._type(self.__input2, text)

    def r2_hit_save(self):
        """Hit 'Save' button on the `row 2`"""
        super()._click(self.__row2save)


    def toast_presence(self) -> bool:
        """Waiting for confirmation / toast bar to be displayed"""
        super()._waiting_visibility(self.__toast, time=25)
        return super()._display_checker(self.__toast)

    def toast_text(self) -> str:
        """Obtaining the displayed text from the toast bar"""
        return super()._get_text(self.__toast)


    def guide_presence(self) -> bool:
        """Validating the instructions availability"""
        return super()._display_checker(self.__instructions)
