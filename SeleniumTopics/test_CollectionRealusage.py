import time

import pytest
from _pytest.mark import Mark
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



driver=webdriver.Chrome()
driver.maximize_window()
#time.sleep(10)

driver.get("https://practice.expandtesting.com/dropdown")
time.sleep(10)
dp=driver.find_element(By.ID,"country")
dpoptions=Select(dp)
dpoptions.select_by_visible_text("Albania")
time.sleep(3)
dpoptions.select_by_index(4)
time.sleep(3)
dpoptions.select_by_value("IN")




driver.get("https://demoqa.com/menu#")
time.sleep(5)
#driver.get("https://testautomationpractice.blogspot.com/")

#
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//h1[text()='Menu']")))
item2dp=driver.find_element(By.XPATH,"//*[@id='nav']/li/a[text()='Main Item 2']")
driver.execute_script("arguments[0].scrollIntoView('true')",item2dp)
action=ActionChains(driver)
action.move_to_element(item2dp).perform()
time.sleep(10)

listcollection=driver.find_elements(By.XPATH,"//*[@id='nav']/li/ul/li")
setcollection=set()
for country in listcollection:
    setcollection.add(country.text)
#for uniquecountry in setcollection:
print(setcollection)

