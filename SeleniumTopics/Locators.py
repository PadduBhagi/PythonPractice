import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(10)
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(10)

element=driver.find_element(By.ID,"ta1")
element.send_keys("hello")

driver.find_element(By.NAME,"q").send_keys("i am busy")
time.sleep(10)

element1=driver.find_element(By.LINK_TEXT,"Page One")
element1.click()
time.sleep(10)
driver.back()
time.sleep(10)

driver.refresh()
element=driver.find_element(By.CLASS_NAME,"gsc-input")
element.send_keys("nenu evaru")
time.sleep(10)



driver.find_element(By.PARTIAL_LINK_TEXT,"compend").click()
driver.back()
time.sleep(10)

textboxes=driver.find_elements(By.XPATH,"//input[@type='text']")
print(len(textboxes))


time.sleep(20)
driver.quit()

