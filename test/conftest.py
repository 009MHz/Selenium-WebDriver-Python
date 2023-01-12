import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browsers")
    print(f"Creating {browser} Driver...")
    if browser == "chrome":
        test_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "edge":
        test_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    yield test_driver
    print(f"\n{browser} Driver is created, exiting the processes...\n")
    test_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browsers",
        action="store",
        default="chrome",
        help="browsers to run the tests (Chrome/Edge)"
    )