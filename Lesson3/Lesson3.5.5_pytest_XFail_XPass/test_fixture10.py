"""
Отметить тест как падающий

Теперь добавим в наш тестовый класс тест, который проверяет наличие кнопки "Избранное":

def test_guest_should_see_search_button_on_the_main_page(self, browser):
     browser.get(link)
     browser.find_element(By.CSS_SELECTOR, "button.favorite")
Предположим, что такая кнопка должна быть, но из-за изменений в коде она пропала. Пока разработчики исправляют баг, мы
хотим, чтобы результат прогона ﻿всех ﻿наших тестов был успешен, но падающий тест помечался соответствующим
образом, чтобы про него не забыть. Добавим маркировку @pytest.mark.xfail для падающего теста.

test_fixture10.py:
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url_link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture(scope='function')
def browser():
    print('\nСтарт браузерадля теста..')
    browser = webdriver.Chrome()
    yield browser
    print('\nЗакрытие браузера..')
    browser.quit()

class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        print('\nНачало 1 теста из класса')
        browser.get(url_link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('\nНачало 2 теста из класса')
        browser.get(url_link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')

    @pytest.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        print('\nНачало 3 теста с маркером xfail')
        browser.get(url_link)
        browser.find_element(By.CSS_SELECTOR, 'button.favorite')

"""
Запустим наши тесты:

pytest -v test_fixture10.py
Наш упавший тест теперь отмечен как xfail, но результат прогона тестов помечен как успешный:
"""

