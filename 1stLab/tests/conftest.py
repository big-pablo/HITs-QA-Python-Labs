import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit