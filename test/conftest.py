import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# @pytest.fixture(params=["chrome", "edge"]) # passed multiple browser
@pytest.fixture()  # passed selected browser only
def driver(request):
    browser = request.config.getoption("--browsers")
    # browser = request.param
    print(f"Creating virtual {browser} Driver...")
    if browser == "chrome":
        test_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "edge":
        test_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        raise TypeError(f"'{browser}' isn't installed/provided")
    # test_driver.implicitly_wait(15)
    yield test_driver


    print(f"\n{browser} Driver is created, exiting the processes.\n")
    test_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browsers",
        action="store",
        default="chrome",
        help="browsers to run the tests (Chrome/Edge)"
    )