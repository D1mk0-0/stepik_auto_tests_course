"""
Когда баг починят, мы это узнаем, ﻿﻿так как теперь тест будет отмечен как XPASS (“unexpectedly passing” —
неожиданно проходит). После этого маркировку xfail для теста можно удалить. Кстати, к маркировке xfail можно добавлять
параметр reason. Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rx.
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

class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        print('\nНачало 1 теста из класса')
        browser.get(url_link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basken_on_the_main_page(self, browser):
        print('\nНачало 2теста из класса')
        browser.get(url_link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')

    # reason покажет указанное сообщение в консоли
    @pytest.mark.xfail(reason='исправлю эту ошибку прямо сейчас')
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        print('\nНачало теста с маркером fail')
        browser.get(url_link)
        browser.find_element(By.CSS_SELECTOR, 'button.favorite')

"""
Запустим наши тесты:

pytest -rx -v test_fixture10a.py

Сравните вывод в первом и во втором случае.
"""
