"""
XPASS-тесты

Поменяем селектор в последнем тесте, чтобы тест начал проходить.

test_fixture10b.py:
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url_link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture(scope='function')
def browser():
    print('\nСтарт браузера для теста..')
    browser = webdriver.Chrome()
    yield browser
    print('\nЗакрытие браузера..')
    browser.quit()

# Попробую не обозначать скобки для класса:
class TestMainPage1:

    def test_guest_should_see_login_link(self, browser):
        print('\nНачало 1 теста из класса')
        browser.get(url_link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('\nНачало 2 теста из класса')
        browser.get(url_link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')

    @pytest.mark.xfail(reason='Исправлю эту ошибку прямо сейчас')
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        print('\nНачало 3 теста с маркером xfail')
        browser.get(url_link)
        browser.find_element(By.CSS_SELECTOR, 'input.btn.btn-default')

"""
Запустите тесты. Здесь мы добавили символ X в параметр -r, чтобы получить подробную информацию по XPASS-тестам:

pytest -rX -v test_fixture10b.py
И изучите отчёт: 

Дополнительно об использовании этих меток можно почитать в документации: 
Skip and xfail: dealing with tests that cannot succeed.  
Там есть много разных интересных особенностей, например, как пропускать тест только при выполнении условия, как 
сделать так, чтобы внезапно прошедший xfailed тест в отчете стал красным, и так далее. 
"""

