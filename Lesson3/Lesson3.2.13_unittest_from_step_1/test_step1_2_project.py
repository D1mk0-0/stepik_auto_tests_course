from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestStep12(unittest.TestCase):

    # Сделает перед тестом
    def setUp(self):
        self.browser = webdriver.Chrome()

    # По сути я только добавил self к каждому обращению к browser. Что-то вроде ссылки на экземпляр класса
    # Несколько тестов вместе называются TestSuit
    def test_registration1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")
        reqInput1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
        reqInput1.send_keys("Ivan")
        reqInput2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
        reqInput2.send_keys("Petrov")
        reqInput3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
        reqInput3.send_keys("ivanp@gmail.com")
        sendButton = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        sendButton.click()
        time.sleep(1)
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # Теперь применяю метод сравнения, наподобие с assert, только в unittest надо так
        self.assertEquals("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")
        reqInput1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
        reqInput1.send_keys("Ivan")
        reqInput2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
        reqInput2.send_keys("Petrov")
        reqInput3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
        reqInput3.send_keys("ivanp@gmail.com")
        sendButton = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        sendButton.click()
        time.sleep(1)
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # Теперь применяю метод сравнения, наподобие с assert, только в unittest надо так
        self.assertEquals("Congratulations! You have successfully registered!", welcome_text)

    # Сделает после теста
    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()

"""
Попробуйте оформить тесты из первого модуля в стиле unittest.

Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла 
Просмотрите отчёт о запуске и найдите последнюю строчку 
Отправьте эту строчку в качестве ответа на это задание 
Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы 
использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, 
здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения. 
"""