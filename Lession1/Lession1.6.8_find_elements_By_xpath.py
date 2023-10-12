from selenium import webdriver
from selenium.webdriver.common.by import By
import time

urlLink = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(urlLink)

    allInput = browser.find_elements(By.XPATH, "//input")
    for allInput in allInput:
        allInput.send_keys("My result")

    sendButton = browser.find_element(By.XPATH, "//button[text()='Submit']")
    sendButton.click()

finally:
    time.sleep(30)
    browser.quit()
