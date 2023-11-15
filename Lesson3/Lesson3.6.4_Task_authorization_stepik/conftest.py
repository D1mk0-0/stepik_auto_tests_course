import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='function')
def browser():
    print('\nСтарт браузера для теста..')
    browser = webdriver.Chrome()
    yield browser
    time.sleep(5)
    print('\nЗавершения работы браузера.')
    browser.quit()