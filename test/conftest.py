import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    print("Creating Chrome Driver . . .")
    test_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield test_driver
    print("\nChrome Driver is created, exiting the processes. . .\n")
    test_driver.quit()