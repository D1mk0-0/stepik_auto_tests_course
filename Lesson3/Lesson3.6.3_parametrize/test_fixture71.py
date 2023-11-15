"""
Можно задавать параметризацию также для всего тестового класса, чтобы все тесты в классе запустились с заданными
параметрами. В таком случае отметка о параметризации должна быть перед объявлением класса:
"""
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('language', ['ru', 'en-gb'])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        url_link = f'http://selenium1py.pythonanywhere.com/{language}/'
        browser.get(url_link)
        browser.find_element(By.CSS_SELECTOR, '#login_link' )
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, browser, language):
        pass
        # этот тест тоже запустится дважды
