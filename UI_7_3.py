from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

LOGIN_URL = 'http://test-stage.geekbrains.ru:8080/login'
ALERT_URL = 'http://test-stage.geekbrains.ru:8080/iframe'
BROWSER = webdriver.Chrome()
EMAIL = 'rollandcar@mail.ru'
PASSWORD = 'ещкеещке'

def wait_until_visible(driver, by, value, timeout=10):
   return WebDriverWait(driver, timeout).until(
       EC.visibility_of_element_located((by, value))
   )

def wait_until_clickable(driver, by, value, timeout=10):
   return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

def wait_until_present(driver, by, value, timeout=10):
  return WebDriverWait(driver, timeout).until(
      EC.presence_of_element_located((by, value))
  )

try:
   BROWSER.get(LOGIN_URL)
   email_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='email']")
   password_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='password']")
   email_field.send_keys(EMAIL)
   password_field.send_keys(PASSWORD)
   BROWSER.find_element_by_css_selector('.button').click()
   BROWSER.get(ALERT_URL)
   BROWSER.find_element(By.ID, "photo")
   assert find_element(By.CLASS_NAME, "button").click()
   alert = BROWSER.switch_to.alert
   assert alert.text == 'Отлично!'
   alert.accept()
   BROWSER.find_element(By.ID, "photo")
   print(width, height)

finally:
 BROWSER.quit()
