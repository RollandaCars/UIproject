from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

try:
   browser.get('http://test-stage.geekbrains.ru:8080/login')
   time.sleep(3)
   browser.find_element_by_name('email').send_keys("rollandcar@mail.ru")
   time.sleep(3)
   browser.find_element_by_name('password').send_keys('ещкеещке')
   time.sleep(3)
   browser.find_element_by_class_name("button").click()
   time.sleep(3)
   browser.get('http://test-stage.geekbrains.ru:8080/about2')
   time.sleep(3)
   browser.find_element(By.NAME, "name").send_keys("Любовь")
   browser.find_element(By.NAME, "surname").send_keys("Сизова")
   checkbox = browser.find_element_by_id('age1')
   if not checkbox.get_attribute('checked'):
       checkbox.click()
   time.sleep(3)
   checkbox = browser.find_element_by_id('age2').click()
   time.sleep(3)
   checkbox = browser.find_element_by_id('lang1').click()
   time.sleep(3)
   checkbox = browser.find_element_by_id('lang2').click()
   time.sleep(3)
   select = Select(browser.find_element_by_name('lvl'))
   time.sleep(3)
   select.select_by_index(2)
   time.sleep(3)
   browser.find_element_by_class_name("button").click()
   assert find_element(By.CLASS_NAME, "is-success").text == "Успех.", "Неверный текст кнопки"

finally:
   browser.quit()

## вторая часть задания

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

browser = webdriver.Chrome()
try:
   browser.get('http://test-stage.geekbrains.ru:8080/login')
   time.sleep(3)
   browser.find_element_by_name('email').send_keys("rollandcar@mail.ru")
   time.sleep(3)
   browser.find_element_by_name('password').send_keys('ещкеещке')
   time.sleep(3)
   browser.find_element_by_class_name("button").click()
   time.sleep(3)
   browser.get('http://test-stage.geekbrains.ru:8080/uploading')
   time.sleep(3)
   input_area = browser.find_element_by_class_name('file-input')
   input_area.send_keys(os.path.join(os.getcwd(), "resources", '0df7fe543ebb70ec7fb9c6c481.jpg'))
   time.sleep(3)
   browser.find_element(By.CLASS_NAME, "button").click()
   assert find_element(By.CLASS_NAME, "notification is-success").text == "Успех", "Неверный текст кнопки"
   browserrowser.refresh()
   assert find_element(By.CLASS_NAME, "notification is-success").text == "Успех", "Неверный текст кнопки"
finally:
    browser.quit()