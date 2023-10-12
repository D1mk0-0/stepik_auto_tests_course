import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

url_link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(url_link)
    # Запоминаю первую страницу
    first_window = browser.window_handles[0]

    trollface_button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    trollface_button.click()

    # Запоминаю вторую страницу
    second_window = browser.window_handles[1]
    # переключаюсь на новую вкладку
    browser.switch_to.window(second_window)

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