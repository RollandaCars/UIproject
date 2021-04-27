from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
try:
   browser.get('http://test-stage.geekbrains.ru:8080/about2')
   time.sleep(3)
   find_element(By.NAME, "name").send_keys("Любовь")
   find_element(By.NAME, "surname").send_keys("Сизова")
   checkbox = browser.find_element_by_id('age1')
   if not checkbox.get_attribute('checked'):
       checkbox.click()
   time.sleep(3)
   checkbox = browser.find_element_by_id('age2').click()
   time.sleep(3)
   checkbox = browser.find_element_by_id('lang1').click()
   checkbox = browser.find_element_by_id('lang2').click()
   select = Select(browser.find_element_by_name('level')
   select.select_by_index(2)
   time.sleep(3)
   surname_field = browser.find_element(By.NAME, 'surname')
   surname_field.send_keys(Keys.ENTER)
   assert find_element(By.CLASS_NAME, "notification is-success").text = "Успех", "Неверный текст кнопки"
   finally:
   browser.quit()

   find_element(By.NAME, "email").send_keys("user@user.ru")
   find_element(By.NAME, "city").send_keys("Nightcity")
   find_element(By.CLASS_NAME, "button is-block is-info is-large is-fullwidth").click()
   assert find_element(By.CLASS_NAME, "notification is-success").text = "Успех", "Неверный текст кнопки"
finally:
   browser.quit()

... вторая часть задания

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
try:
   browser.get('http://test-stage.geekbrains.ru:8080/uploading')
   time.sleep(3)
   input_area = browser.find_element_by_class('file-input')
   input_area.send_keys(os.path.join(os.getcwd(), "resources", '33462347123.jpg'))
   time.sleep(3)
   find_element(By.CLASS_NAME, "button is-block is-info is-large is-fullwidth").click()
    assert find_element(By.CLASS_NAME, "notification is-success").text = "Успех", "Неверный текст кнопки"
    browser.refresh()
    assert find_element(By.CLASS_NAME, "notification is-success").text = "Успех", "Неверный текст кнопки"
finally:
    browser.quit()

