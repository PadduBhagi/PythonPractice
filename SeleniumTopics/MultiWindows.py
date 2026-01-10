import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(10)
driver.find_element(By.LINK_TEXT,"Multiple Windows").click()

wait=WebDriverWait(driver,10)
wait.until(expected_conditions.url_to_be("https://the-internet.herokuapp.com/windows"))
time.sleep(10)
driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(10)

handles=driver.window_handles
print(handles)
for handle in handles:
    driver.switch_to.window(handle)
    time.sleep(5)
    if "New Window" in driver.title:
        windowtext=driver.find_element(By.XPATH,"//h3[text()='New Window']").text
        print(windowtext)
        break



