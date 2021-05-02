from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

def wait_until_clickable(driver, by, value, timeout=10):
   return WebDriverWait(driver, timeout).until(ec.element_to_be_clickable((by, value)))

try:
    wait = WebDriverWait(browser, 10)
    browser.get('http://test-stage.geekbrains.ru:8080/login')
    wait_until_clickable(browser, By.NAME,'email').send_keys("rollandcar@mail.ru")
    wait_until_clickable(browser, By.NAME,'password').send_keys('ещкеещке')
    browser.find_element_by_class_name("button").click()
    time.sleep(3)
    browser.get('http://test-stage.geekbrains.ru:8080/timer')
    time.sleep(3)
    WebDriverWait(browser, 100).until(ec.element_to_be_clickable((By.CLASS_NAME, "button"))).click()
    WebDriverWait(browser, 10).until(ec.alert_is_present())
    alert = browser.switch_to.alert
    assert "Успех." in alert.text

finally:
   browser.quit()

##второе задание

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

def wait_until_clickable(driver, by, value, timeout=10):
   return WebDriverWait(driver, timeout).until(ec.element_to_be_clickable((by, value)))

try:
    wait = WebDriverWait(browser, 10)
    browser.get('http://test-stage.geekbrains.ru:8080/login')
    wait_until_clickable(browser, By.NAME,'email').send_keys("rollandcar@mail.ru")
    wait_until_clickable(browser, By.NAME,'password').send_keys('ещкеещке')
    browser.find_element_by_class_name("button").click()
    time.sleep(3)
    browser.get('http://test-stage.geekbrains.ru:8080/slow')
    wait_until_clickable(browser, By.CLASS_NAME, "input").send_keys("Панорама")
    wait_until_clickable(browser, By.CLASS_NAME, "button").click()
    WebDriverWait(browser, 10).until(ec.alert_is_present())
    alert = browser.switch_to.alert
    assert "Успех." in alert.text

finally:
   browser.quit()