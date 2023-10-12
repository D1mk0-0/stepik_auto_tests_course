from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url_link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(url_link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Высчитываю x
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Нахожу inpun и ввожу значение
    input_area = browser.find_element(By.TAG_NAME, "input")
    input_area.send_keys(calc(x))

    # Нахожу checkbox и кликаю по label
    checkbox_input = browser.find_element(By.CSS_SELECTOR, ".form-check-custom .form-check-label")
    checkbox_input.click()

    # Нахожу radiobutton и кликаю по Rodots rule
    radiobutton_input = browser.find_element(By.CSS_SELECTOR, ".form-radio-custom .form-check-label")
    radiobutton_input.click()

    send_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    send_button.click()

finally:
    time.sleep(10)
    browser.quit()