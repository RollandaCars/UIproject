from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

LOGIN_URL = 'http://test-stage.geekbrains.ru:8080/login'
PROFILE_URL = 'http://test-stage.geekbrains.ru:8080/profile'
BROWSER = webdriver.Chrome()
EMAIL = 'rollandcar@mail.ru'
PASSWORD = 'ещкеещке'

def wait_until_visible(driver, by, value, timeout=10):
   return WebDriverWait(driver, timeout).until(
       EC.visibility_of_element_located((by, value))
   )

def login():
   BROWSER.get(LOGIN_URL)
   cookies = browser.get_cookies()
   email_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='email']")
   password_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='password']")
   email_field.send_keys(EMAIL)
   password_field.send_keys(PASSWORD)
   BROWSER.find_element_by_css_selector('.button').click()
   print(cookies)
   browser.delete_cookie
   assert not cookie
   BROWSER.get(PROFILE_URL)
   assert find_element(By.CLASS_NAME, "title").text == "Привет, Васька", "Неверный текст кнопки"

   browser.quit()



   ###Второе задание


   from selenium.webdriver.support.wait import WebDriverWait
   from selenium import webdriver
   from selenium.webdriver.support import expected_conditions as EC
   from selenium.webdriver.common.by import By

   LOGIN_URL = 'http://test-stage.geekbrains.ru:8080/login'
   DRAG_URL = 'http://test-stage.geekbrains.ru:8080/drag_and_drop'
   BROWSER = webdriver.Chrome()
   EMAIL = 'rollandcar@mail.ru'
   PASSWORD = 'ещкеещке'

   def wait_until_visible(driver, by, value, timeout=10):
       return WebDriverWait(driver, timeout).until(
           EC.visibility_of_element_located((by, value))
       )

   def login():
       BROWSER.get(LOGIN_URL)
       cookies = browser.get_cookies()
       email_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='email']")
       password_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='password']")
       email_field.send_keys(EMAIL)
       password_field.send_keys(PASSWORD)
       BROWSER.find_element_by_css_selector('.button').click()
       BROWSER.get(DRAG_URL)
       actionchains = ActionChains(browser)
       actionchains.drag_and_drop_by_offset(image, 0, 100)
       time.sleep(2)
       assert alert.text == 'Успех!'
       alert.accept()

       browser.quit()

       ###третье задание


       from selenium.webdriver.support.wait import WebDriverWait
       from selenium import webdriver
       from selenium.webdriver.support import expected_conditions as EC
       from selenium.webdriver.common.by import By

       LOGIN_URL = 'http://test-stage.geekbrains.ru:8080/login'
       BROWSER = webdriver.Chrome()
       EMAIL = 'rollandcar@mail.ru'
       PASSWORD = 'ещкеещке'

       def wait_until_visible(driver, by, value, timeout=10):
           return WebDriverWait(driver, timeout).until(
               EC.visibility_of_element_located((by, value))
           )

       def login():
           BROWSER.get(LOGIN_URL)
           cookies = browser.get_cookies()
           email_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='email']")
           password_field = wait_until_visible(BROWSER, By.CSS_SELECTOR, "[name='password']")
           email_field.send_keys(EMAIL)
           password_field.send_keys(PASSWORD)
           BROWSER.find_element_by_css_selector('.button').click()
           time.sleep(3)
           browser.execute_script(" document.getElementsByClassName('menu-list')[0].click();")
           current_url = browser.execute_script("return document.URL")
           wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
           browser.execute_script(" document.getElementsByClassName('menu-list')[1].click();")
           current_url = browser.execute_script("return document.URL")
           wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
           browser.execute_script(" document.getElementsByClassName('menu-list')[2].click();")
           current_url = browser.execute_script("return document.URL")
           wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
           browser.execute_script(" document.getElementsByClassName('menu-list')[3].click();")
           current_url = browser.execute_script("return document.URL")
           wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
           browser.execute_script(" document.getElementsByClassName('menu-list')[4].click();")
           current_url = browser.execute_script("return document.URL")
           wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
           browser.execute_script(" document.getElementsByClassName('menu-list')[5].click();")
           current_url = browser.execute_script("return document.URL")
           wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
           browser.execute_script(" document.getElementsByClassName('menu-list')[6].click();")
           current_url = browser.execute_script("return document.URL")
           wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
           browser.execute_script(" document.getElementsByClassName('menu-list')[7].click();")
           current_url = browser.execute_script("return document.URL")
           wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
           browser.execute_script(" document.getElementsByClassName('menu-list')[8].click();")
           current_url = browser.execute_script("return document.URL")
           wait_until_clickable(browser, By.CLASS_NAME, "menu-list")
           browser.execute_script(" document.getElementsByClassName('menu-list')[9].click();")
           current_url = browser.execute_script("return document.URL")

        browser.quit()

