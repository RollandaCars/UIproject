from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


LOGIN_URL = 'http://test-stage.geekbrains.ru:8080/login'
BROWSER = webdriver.Chrome()
EMAIL = 'rollandcar@mail.ru'
PASSWORD = 'fr0ntend'

def login():
   BROWSER.get(LOGIN_URL)
   email_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='email']")
   password_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='password']")
   email_field.send_keys(EMAIL)
   password_field.send_keys(PASSWORD)
   BROWSER.find_element_by_css_selector('.button').click()


try:
   browser.get('http://test-stage.geekbrains.ru:8080/timer')
   wait = WebDriverWait(browser, 100) until_not(
       ec.element_to_be_clickable((By.class, "button is-block is-info is-large is-fullwidth"))
   ), "Кнопка кликабельна"
   WebDriverWait(browser, 10).until(EC.alert_is_present())
   alert = browser.switch_to.alert
   assert "Успех!" in alert.text

   //// второе задание


   from selenium import webdriver
   from selenium.webdriver.support.wait import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   from selenium.webdriver.common.by import By


   browser = webdriver.Chrome()


   try:
       browser.get('http://test-stage.geekbrains.ru:8080/slow')
       wait = WebDriverWait(browser, 10) until_not(
           ec.element_to_be_clickable((By.class , "button is-block is-info is-large is-fullwidth"))
       ), "Кнопка кликабельна"
       WebDriverWait(browser, 10).until(EC.alert_is_present())
       alert = browser.switch_to.alert
       assert "Успех!" in alert.text

##Убрав ожидания первый скрипт упал, как как кнопка не кликабельна, второй скрипт также упал, так как кнопка не кликабельна.
