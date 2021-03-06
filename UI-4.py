from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
   browser.get('http://test-stage.geekbrains.ru:8080/many_fields')
   time.sleep(5)
   browser.find_element_by_name("test").send_keys("lesson4")
   time.sleep(3)
   browser.find_element_by_class_name('button is-block is-info is-large is-fullwidth').click()
   time.sleep(3)
   assert browser.find_element_by_class_name('notification is-success').text == "Успех.", "Неверный текст кнопки"
time.sleep(3)
    browser.find_element_by_name("field13").send_keys("lesson4")
    browser.find_element_by_class_name('button is-block is-info is-large is-fullwidth').click()
    assert browser.find_element_by_class_name('notification is-danger').text == "Неправильное поле", "Неверный текст кнопки"
finally:
   browser.quit()

/// вторая часть задания

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
try:
   browser.get('http://test-stage.geekbrains.ru:8080/about1')
   time.sleep(3)
   find_element(By.NAME, "name").send_keys("Любовь")
   find_element(By.NAME, "surname").send_keys("Сизова")
   find_element(By.NAME, "email").send_keys("user@user.ru")
   find_element(By.NAME, "city").send_keys("Nightcity")
   find_element(By.CLASS_NAME, "button is-block is-info is-large is-fullwidth").click()
   assert find_element(By.CLASS_NAME, "notification is-success").text = "Успех", "Неверный текст кнопки"
finally:
   browser.quit()

