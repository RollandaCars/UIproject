from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

LOGIN_URL = 'http://test-stage.geekbrains.ru:8080/login'
BROWSER = webdriver.Chrome()
EMAIL = 'rollandcar@mail.ru'
PASSWORD = 'ещкеещке'

try:
   BROWSER.get(LOGIN_URL)
   email_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='email']")
   password_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='password']")
   email_field.send_keys(EMAIL)
   password_field.send_keys(PASSWORD)
   BROWSER.find_element_by_class_name('button').click()
   BROWSER.get('http://test-stage.geekbrains.ru:8080/open_new_window')
   wait_until_clickable(BROWSER, By.CLASS_NAME, "button").click()
   first_window = BROWSER.window_handles[0]
   second_window = BROWSER.window_handles[1]
   BROWSER.switch_to.window(first_window)
   BROWSER.switch_to.window(second_window)

   print('Заголовок страницы: ' + BROWSER.title + ',' + ' адрес страницы: ' + BROWSER.current_url)
   BROWSER.switch_to.window(first_window)
   print('Заголовок страницы: ' + BROWSER.title + ',' + ' адрес страницы: ' + BROWSER.current_url)
   BROWSER.switch_to.window(second_window)
   wait_until_clickable(BROWSER, By.CLASS_NAME, "button").click()
   alert = BROWSER.switch_to.alert
   assert alert.text == 'Успех!'
   alert.accept()

finally:
 BROWSER.quit()

