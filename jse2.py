from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

promptbutton=driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']")
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[text()='Click for JS Prompt']")))

promptbutton.click()
time.sleep(10)
alert1=Alert(driver)
alert1.send_keys("bhargava")

print("this is second program from local system")

time.sleep(10)
