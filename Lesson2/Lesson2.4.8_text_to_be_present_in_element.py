import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url_link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(url_link)

    # Нахожу элемент с ценой и ожидаю установленного значения
    price_value = WebDriverWait(browser, 15).until(
        # ((что за элемент?) Значение которое ожидать)
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # После наступления кликаю на кнопку
    browser.find_element(By.ID, "book").click()

    x_number = browser.find_element(By.ID, "input_value")
    x = x_number.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element(By.ID, "answer").send_keys(calc(x))

    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(15)
    browser.quit()