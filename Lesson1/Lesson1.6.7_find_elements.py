from selenium import webdriver
from selenium.webdriver.common.by import By
import time

urlLink = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(urlLink)

    allInput = browser.find_elements(By.TAG_NAME, "input")

    # Пишу цикл для поочередного заполнения каждого инпута
    for allInput in allInput:
        allInput.send_keys("My result")

    sendButton = browser.find_element(By.CSS_SELECTOR, "button.btn")
    sendButton.click()

finally:

    time.sleep(30)
    browser.quit()