from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

urlLink = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(urlLink)
    buttonLink = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    buttonLink.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Popov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Rostov")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    sendButton = browser.find_element(By.CSS_SELECTOR, "button.btn")
    sendButton.click()

finally:
    time.sleep(30)
    browser.quit()
