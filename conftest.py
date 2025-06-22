import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests (chrome, firefox, edge)"
    )

@pytest.fixture(scope="module")
def setup(request):
    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get("http://www.way2automation.com/angularjs-protractor/webtables/")
    driver.maximize_window()
    yield driver
    driver.quit()
