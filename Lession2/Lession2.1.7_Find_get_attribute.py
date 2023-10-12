import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


urlLink = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(urlLink)

    # Нахожу картинку
    img_element = browser.find_element(By.ID, "treasure")
    # Нахожу значение атрибута и сохраняю в меременную
    x = img_element.get_attribute("valuex")

    # Высчитываю x
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    input_area = browser.find_element(By.ID, "answer")
    input_area.send_keys(calc(x))

    input_checkbox = browser.find_element(By.ID, "robotCheckbox")
    input_checkbox.click()

    input_radiobutton = browser.find_element(By.ID, "robotsRule")
    input_radiobutton.click()

    send_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    send_button.click()

finally:
    time.sleep(10)
    browser.quit()
