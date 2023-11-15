from LogPass.log_and_pass import LogAndPass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url_link = 'https://stepik.org/lesson/236895/step/1'

def test_authorization_for_stepik(browser):
    browser.get(url_link)
    BTN_IN_LOGIN = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'ember33')))
    BTN_IN_LOGIN.click()
    INPUT_EMAIL = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'id_login_email')))
    INPUT_EMAIL.send_keys(LogAndPass.login)
    INPUT_PASSWORD = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'id_login_password')))
    INPUT_PASSWORD.send_keys(LogAndPass.password)
    browser.find_element(By.CSS_SELECTOR, '#login_form > button').click()




