from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

LOGIN_URL = 'http://test-stage.geekbrains.ru:8080/login'
PROFILE_URL = 'http://test-stage.geekbrains.ru:8080/profile'
BROWSER = webdriver.Chrome()
EMAIL = 'rollandcar@mail.ru'
PASSWORD = 'ещкеещке'

def wait_until_visible(driver, by, value, timeout=10):
   return WebDriverWait(driver, timeout).until(
       EC.visibility_of_element_located((by, value))
   )

try:
   BROWSER.get(LOGIN_URL)
   email_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='email']")
   password_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='password']")
   email_field.send_keys(EMAIL)
   password_field.send_keys(PASSWORD)
   BROWSER.find_element_by_css_selector('.button').click()
   cookies = BROWSER.get_cookies()
   print(cookies)
   time.sleep(3)
   BROWSER.delete_cookies()
   assert not cookies
   BROWSER.get(PROFILE_URL)
   assert find_element(By.CLASS_NAME, "title").text == "Привет, Васька", "Неверный текст кнопки"

finally:
   BROWSER.quit()


