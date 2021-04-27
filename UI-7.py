from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

LOGIN_URL = 'http://test-stage.geekbrains.ru:8080/login'
BROWSER = webdriver.Chrome()
EMAIL = 'testuser@test.ru'
PASSWORD = '1234'

def wait_until_visible(driver, by, value, timeout=10):
   return WebDriverWait(driver, timeout).until(
       EC.visibility_of_element_located((by, value))
   )

def login():
   BROWSER.get(LOGIN_URL)
   email_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='email']")
   password_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='password']")
   email_field.send_keys(EMAIL)
   password_field.send_keys(PASSWORD)
   BROWSER.find_element_by_css_selector('.button').click()
   assert BROWSER.current_url != LOGIN_URL, BROWSER.current_url

   BROWSER.get(http://test-stage.geekbrains.ru:8080/open_new_window)
   first_window = browser.window_handles[0]
   second_window = browser.window_handles[1]
   browser.switch_to.window(first_window)
   browser.switch_to.window(second_window)

   print('Заголовок страницы: ' + browser.title + ',' + ' адрес страницы: ' + browser.current_url)
   browser.switch_to.window(first_window)
   print('Заголовок страницы: ' + browser.title + ',' + ' адрес страницы: ' + browser.current_url)
   browser.switch_to.window(second_window)

   find_element(By.CLASS_NAME, "button is-block is-info is-large is-fullwidth").click()
   find_element(By.CLASS_NAME, "button is-block is-info is-large is-fullwidth").click()
   wait_until_alert_is_present(BROWSER)
   alert = BROWSER.switch_to.alert
   assert alert.text == 'Успех!'
   alert.accept()

finally:
   browser.quit()

   ##вторая часть.....

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

LOGIN_URL = 'http://test-stage.geekbrains.ru:8080/login'
ALERT_URL = 'http://test-stage.geekbrains.ru:8080/three_button'
BROWSER = webdriver.Chrome()
EMAIL = 'testuser@test.ru'
PASSWORD = '1234'


def wait_until_visible(driver, by, value, timeout=10):
   return WebDriverWait(driver, timeout).until(
       EC.visibility_of_element_located((by, value))
   )


def wait_until_alert_is_present(driver, timeout=10):
   return WebDriverWait(driver, timeout).until(
       EC.alert_is_present()
   )
def login():
   BROWSER.get(LOGIN_URL)
   email_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='email']")
   password_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='password']")
   email_field.send_keys(EMAIL)
   password_field.send_keys(PASSWORD)
   BROWSER.find_element_by_css_selector('.button').click()
   assert BROWSER.current_url != LOGIN_URL, BROWSER.current_url


def test_alert():
   try:
       login()
       BROWSER.get(ALERT_URL)
       wait = WebDriverWait(browser, 100)
       until_not(
           ec.element_to_be_clickable((By.class, "button is-block is-info is-large is-fullwidth"(3)))
   ).(click)
       wait_until_alert_is_present(BROWSER)
       alert = BROWSER.switch_to.alert
       assert alert.text == 'Как тебя зовут' send_keys("Любовь")
       alert.accept()
       assert find_element(By.ID, "promt_text").text = "Привет, Любовь", "Неверный текст кнопки"
       browser.refresh()
       find_element(By.CLASS_NAME, "button is-block is-info is-large is-fullwidth"(3)).click()
       assert alert.text == 'Как тебя зовут'
       alert.dissmiss()
       assert find_element(By.ID, "promt_text").text = "Не ответили на вопрос :(", "Неверный текст кнопки"

   finally:
       BROWSER.quit()

       ## третья часть.....
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

LOGIN_URL = 'http://test-stage.geekbrains.ru:8080/login'
ALERT_URL = 'http://test-stage.geekbrains.ru:8080/iframe'
BROWSER = webdriver.Chrome()
EMAIL = 'testuser@test.ru'
PASSWORD = '1234'

def login():
   BROWSER.get(LOGIN_URL)
   email_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='email']")
   password_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='password']")
   email_field.send_keys(EMAIL)
   password_field.send_keys(PASSWORD)
   BROWSER.find_element_by_css_selector('.button').click()
   assert BROWSER.current_url != LOGIN_URL, BROWSER.current_url

def test_alert():
   try:
       login()
       BROWSER.get(ALERT_URL)
   assert find_element(By.ID, "photo").text = "Успех", "Неверный текст кнопки"
   assert find_element(By.CLASS_NAME, "button").click()
   alert = BROWSER.switch_to.alert
   assert alert.text == 'Отлично!'
   alert.accept()
   find_element(By.ID, "photo")
    print(width, height)

finally:
BROWSER.quit()


