import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def browser():
    print('\nСтарт работы браузера для теста..')
    browser = webdriver.Chrome()
    yield browser
    print('\nЗавершение работы браузера')
    browser.quit()