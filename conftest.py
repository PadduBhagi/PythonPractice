import pytest
from _pytest.config.argparsing import Parser
from selenium import webdriver


#from selenium.webdriver.chrome.webdriver import WebDriver

#from selenium.webdriver.chrome.webdriver import Chrome

#global driver

@pytest.fixture()
def test_setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    driver.get("https://tutorialsninja.com/demo")
    yield
    driver.quit()


@pytest.fixture(autouse=True)
def test_setup_and_teardown():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo")
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--env", action="store")


@pytest.fixture()
def get_environment(request):
    return request.config.getoption("--env")
