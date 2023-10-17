import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

urlLink = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(urlLink)

    x_number = browser.find_element(By.ID, "input_value")
    x = x_number.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    input_area = browser.find_element(By.TAG_NAME, "input")
    input_area.send_keys(calc(x))

    checkbox_input = browser.find_element(By.ID, "robotCheckbox")
    # Скролю страницу до элемента
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox_input)
    checkbox_input.click()

    radiobutton_input = browser.find_element(By.ID, "robotsRule")
    # Скролю страницу до элемента
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton_input)
    radiobutton_input.click()

    send_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # Скролю страницу до элемента
    browser.execute_script("return arguments[0].scrollIntoView(true);", send_button)
    send_button.click()

finally:
    time.sleep(15)
    browser.quit()