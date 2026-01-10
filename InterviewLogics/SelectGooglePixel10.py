import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
wait=WebDriverWait(driver,20)
wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@title='Search']")))
driver.find_element(By.XPATH,"//*[@title='Search']").send_keys("google pixel 10")
wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@class='wM6W7d']")))
mobiles_list=driver.find_elements(By.XPATH,"//*[@class='wM6W7d']")
for mobile in mobiles_list:
    if mobile.text=="google pixel 10 pro xl":
        mobile.click()
        time.sleep(20)
        break

