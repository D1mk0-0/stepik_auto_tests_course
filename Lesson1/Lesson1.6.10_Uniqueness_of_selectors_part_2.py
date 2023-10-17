from selenium import webdriver
from selenium.webdriver.common.by import By
import time

urlLink = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(urlLink)

    # Ваш код, который заполняет обязательные поля
    reqInput1 = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
    reqInput1.send_keys("Ivan")
    reqInput2 = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
    reqInput2.send_keys("Petrov")
    reqInput3 = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
    reqInput3.send_keys("ivanp@gmail.com")

    # Отправляем заполненную форму
    sendButton = browser.find_element(By.CSS_SELECTOR, "button.btn")
    sendButton.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

