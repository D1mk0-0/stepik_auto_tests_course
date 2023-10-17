import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

url_link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    start_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    start_button.click()

    # Теперь переключаюсь на всплывающее окно типа confirm
    confirm = browser.switch_to.alert
    # Принимаю confirm
    confirm.accept()

    # Решаю капчу
    x_number = browser.find_element(By.ID, "input_value")
    x = x_number.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    input_area = browser.find_element(By.ID, "answer")
    input_area.send_keys(calc(x))

    send_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    send_button.click()

finally:
    time.sleep(15)
    browser.quit()


