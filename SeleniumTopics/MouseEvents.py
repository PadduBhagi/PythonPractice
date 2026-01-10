import time

from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=webdriver.Chrome()
driver.maximize_window()
'''
driver.get("https://tutorialsninja.com/demo")
action=ActionChains(driver)

action.move_to_element(driver.find_element(By.XPATH,"//*[text()='Desktops']")).click().perform()
time.sleep(5)
action.move_to_element(driver.find_element(By.XPATH,"//*[text()='PC (0)']")).click().perform()
action.move_to_element(driver.find_element(By.XPATH,"//*[contains(text(),'Laptops & Notebooks (5)')]")).click().perform()
time.sleep(5)
action.scroll_by_amount(100,1000).perform()
time.sleep(5)
'''

driver.get("https://the-internet.herokuapp.com/context_menu")

time.sleep(10)
action=ActionChains(driver)
action.context_click(driver.find_element(By.ID,"hot-spot")).perform()
time.sleep(5)
alert=driver.switch_to.alert
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.alert_is_present())
alert.accept()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(5)
driver.find_element(By.XPATH,"//*[text()='Drag and Drop']").click()
source=driver.find_element(By.ID,"column-a")
dest=driver.find_element(By.ID,"column-b")
#action.drag_and_drop(source,dest).perform()
action.click_and_hold(source).move_to_element(dest).release().perform()
time.sleep(10)
