from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

LOGIN_URL = 'http://test-stage.geekbrains.ru:8080/login'
DRAG_URL = 'http://test-stage.geekbrains.ru:8080/drag_and_drop'
BROWSER = webdriver.Chrome()
EMAIL = 'rollandcar@mail.ru'
PASSWORD = 'ещкеещке'

def wait_until_visible(driver, by, value, timeout=10):
       return WebDriverWait(driver, timeout).until(
           EC.visibility_of_element_located((by, value))
       )

def wait_until_clickable(driver, by, value, timeout=10):
   return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

try:
       BROWSER.get(LOGIN_URL)
       email_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='email']")
       password_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='password']")
       email_field.send_keys(EMAIL)
       password_field.send_keys(PASSWORD)
       BROWSER.find_element_by_css_selector('.button').click()
       BROWSER.get(DRAG_URL)
       actionchains = ActionChains(BROWSER)
       element_to_dnd = BROWSER.find_element_by_id("photo")
       source_element = BROWSER.find_element_by_id("square")
       ActionChains(BROWSER).drag_and_drop(element_to_dnd, source_element).perform()
       time.sleep(2)
       alert = BROWSER.switch_to.alert
       assert alert.text == 'Успех!'
       alert.accept()

finally:
 BROWSER.quit()