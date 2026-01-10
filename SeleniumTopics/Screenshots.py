import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(10)
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(10)
driver.save_screenshot("image.png")
driver.get_screenshot_as_file("image2.png")
element=driver.find_element(By.CLASS_NAME,"widget-content")
element.click()
element.screenshot("element.png")