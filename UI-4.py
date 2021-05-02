from selenium import webdriver
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

   browser.get('http://test-stage.geekbrains.ru:8080/many_fields')
   time.sleep(5)
   browser.find_element_by_name("test").send_keys("lesson4")
   time.sleep(3)
   browser.find_element_by_class_name('button').click()
   time.sleep(3)
   assert browser.find_element_by_class_name('is-success').text == "Успех.", "Неверный текст кнопки"
   time.sleep(3)
   browser.find_element_by_name("field13").send_keys("lesson4")
   browser.find_element_by_class_name('button').click()
   assert browser.find_element_by_class_name('is-danger').text == "Неправильное поле.", "Неверный текст кнопки"

finally:
   browser.quit()

### вторая часть задания

rom selenium import webdriver
from selenium.webdriver.common.by import By
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
    browser.get('http://test-stage.geekbrains.ru:8080/about1')
    time.sleep(3)
    browser.find_element(By.NAME,'name').send_keys("Любовь")
    time.sleep(3)
    browser.find_element(By.NAME, 'surname').send_keys("Сизова")
    time.sleep(3)
    browser.find_element(By.NAME, "email").send_keys("user@user.ru")
    time.sleep(3)
    browser.find_element(By.NAME, "city").send_keys("Nightcity")
    time.sleep(3)
    browser.find_element(By.CLASS_NAME, "button").click()
    time.sleep(3)
    assert browser.find_element(By.CLASS_NAME, "is-success").text == "Успех.", "Неверный текст кнопки"
finally:
   browser.quit()
