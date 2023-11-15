"""
Область видимости scope
Для фикстур можно задавать область покрытия фикстур. Допустимые значения: “function”, “class”, “module”, “session”.
Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса, один раз для модуля или
один раз для всех тестов, запущенных в данной сессии.

Запустим все наши тесты из класса TestMainPage1 в одном браузере для экономии времени, задав scope="class" в фикстуре
browser:
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

urlLink = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class")
def browser():
    # Действие перед открытием браузера
    print("\nСтарт браузера для теста...")
    browser = webdriver.Chrome()
    # Ключевое слово для действия после теста
    yield browser
    print('\nЗакрытие браузера...')
    browser.quit()

class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print('Начало теста 1')
        browser.get(urlLink)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print('Конец теста 1')

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('Начало теста 2')
        browser.get(urlLink)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')
        print('Конец теста 2')

"""
Мы видим, что в данном примере браузер открылся один раз и тесты последовательно выполнились в этом браузере. Здесь мы 
проделали это в качестве примера, но мы крайне рекомендуем всё же запускать отдельный экземпляр браузера для каждого 
теста, чтобы повысить стабильность тестов. Фикстуры, которые занимают много времени для запуска и ресурсов (обычно это 
работа с базами данных), можно вызывать и один раз за сессию запуска тестов.
"""