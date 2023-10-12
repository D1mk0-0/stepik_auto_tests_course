import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
# Подгружаю библиотеку для списка
from selenium.webdriver.support.ui import Select

urlLink = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(urlLink)

    # Нахожу числа
    a_number = browser.find_element(By.ID, "num1")
    a = a_number.text
    b_number = browser.find_element(By.ID, "num2")
    b = b_number.text

    # С помощью int преобразую строку в целое число
    c = int(a) + int(b)
    # Назад преобразую число в текст
    c_number = str(c)

    # Использую Select для работы со списком
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    # Выбираю необходимую строку
    select.select_by_value(c_number)
    # Еще можно искать по:
    # select.select_by_visible_text("text") ищет элемент по видимому тексту
    # elect.select_by_index(index) ищет элемент по его индексу или порядковому номеру
    # select_by_value("1")

    send_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    send_button.click()

finally:
    time.sleep(15)
    browser.quit()



