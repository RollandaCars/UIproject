
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

LOGIN_URL = 'http://test-stage.geekbrains.ru:8080/login'
ALERT_URL = 'http://test-stage.geekbrains.ru:8080/three_button'
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

wait = WebDriverWait(BROWSER, 10)

try:
   BROWSER.get(LOGIN_URL)
   email_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='email']")
   password_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='password']")
   email_field.send_keys(EMAIL)
   password_field.send_keys(PASSWORD)
   wait_until_clickable(BROWSER, By.CLASS_NAME, "button").click()
   BROWSER.get(ALERT_URL)
   wait_until_present(BROWSER, By.CSS_SELECTOR, ".button[onclick='confirm_func()']").click()
   wait.until(EC.alert_is_present())
   alert = BROWSER.switch_to.alert
   prompt = BROWSER.switch_to.alert
   assert "Как тебя зовут?" in prompt.text
   prompt.send_keys("Любовь")
   prompt.accept()
   browser.refresh()
   BROWSER.find_element(By.CLASS_NAME, "button").click()
   assert alert.text == 'Как тебя зовут?'
   alert.dissmiss()
   assert find_element(By.ID, "promt_text").text == "Не ответили на вопрос :(", "Неверный текст кнопки"

finally:
    BROWSER.quit()

