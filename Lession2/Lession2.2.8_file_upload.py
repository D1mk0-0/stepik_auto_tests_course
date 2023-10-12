import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

urlLink = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(urlLink)

    firstname_input = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    firstname_input.send_keys("Ivan")

    lastname_input = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    lastname_input.send_keys("Petrov")

    email_input = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    email_input.send_keys("ivanp@gmail.com")

    # Теперь разбираюсь с путем
    # Получаю путь текущего файла (В скобках надо писать наименование ЭТОГО ФАЙЛА)
    current_dir = os.path.abspath(os.path.dirname("Lession2.2.8_file_upload.py"))
    # Сохраняю в переменную имя файла, который буду добавлять
    file_name = "file.txt"
    # Получаю путь к своему файлу
    file_path = os.path.join(current_dir, file_name)

    # Нахожу кнопку для добавления файла
    file_input = browser.find_element(By.ID, "file")
    # Отправляю файл
    file_input.send_keys(file_path)

    send_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    send_button.click()

finally:
    time.sleep(15)
    browser.quit()

"""
Для загрузки файла на веб-страницу, используем метод send_keys("путь к файлу")
Три способа задать путь к файлу:

1. вбить руками

element.send_keys("/home/user/stepik/Chapter2/file_example.txt")



2. задать с помощью переменных

# указывая директорию,где лежит файлу.txt
# в конце должен быть /
directory = "/home/user/stepik/Chapter2/"

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# собираем путь к файлу
file_path = os.path.join(directory, file_name)
# отправляем файл
element.send_keys(file_path)
3.путь автоматизатора.
если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге
# импортируем модуль
import os
# получаем путь к директории текущего исполняемого скрипта lesson2_7.py
current_dir = os.path.abspath(os.path.dirname(__file__))

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)
# отправляем файл
element.send_keys(file_path)
"""