from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

LOGIN_URL = 'http://test-stage.geekbrains.ru:8080/login'
browser = webdriver.Chrome()
EMAIL = 'rollandcar@mail.ru'
PASSWORD = 'ещкеещке'


def wait_until_visible(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, value))
    )

def wait_until_clickable(driver, by, value, timeout=10):
   return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

try:
    browser.get(LOGIN_URL)
    email_field = wait_until_visible(browser, By.CSS_SELECTOR, "[name='email']")
    password_field = wait_until_visible(browser, By.CSS_SELECTOR, "[name='password']")
    email_field.send_keys(EMAIL)
    password_field.send_keys(PASSWORD)
    browser.find_element_by_css_selector('.button').click()
    time.sleep(3)
    browser.execute_script("document.getElementsByClassName('menu')[0]").click()
    current_url = browser.execute_script("return document.URL")
    wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
    browser.execute_script("document.getElementsByClassName('menu')[1]").click()
    current_url = browser.execute_script("return document.URL")
    wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
    browser.execute_script("document.getElementsByClassName('menu')[2]").click()
    current_url = browser.execute_script("return document.URL")
    wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
    browser.execute_script("document.getElementsByClassName('menu')[3]").click()
    current_url = browser.execute_script("return document.URL")
    wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
    browser.execute_script("document.getElementsByClassName('menu')[4]").click()
    current_url = browser.execute_script("return document.URL")
    wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
    browser.execute_script("document.getElementsByClassName('menu')[5]").click()
    current_url = browser.execute_script("return document.URL")
    wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
    browser.execute_script("document.getElementsByClassName('menu')[6]").click()
    current_url = browser.execute_script("return document.URL")
    wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
    browser.execute_script("document.getElementsByClassName('menu')[7]").click()
    current_url = browser.execute_script("return document.URL")
    wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
    browser.execute_script("document.getElementsByClassName('menu')[8]").click()
    current_url = browser.execute_script("return document.URL")
    wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
    browser.execute_script("document.getElementsByClassName('menu')[9]").click()
    current_url = browser.execute_script("return document.URL")

finally:
    browser.quit()

