import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/downloads/")
releaseversion="Selenium 4.38.0"
'''
previous_link_text=driver.find_element(By.XPATH,"//*[text()='C# NuGet']")
driver.execute_script("arguments[0].scrollIntoView('true')",previous_link_text)
'''
try:
    driver.find_element(By.XPATH, "//*[text()='releases']").click()

except ElementClickInterceptedException:
    print("element is not clicked at this position")

time.sleep(20)
driver.find_element(By.XPATH,"//*[text()='releases']").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH,"//*[text()='Selenium 4.38.0']").click()
'''
releasedate_text=driver.find_element(By.XPATH,"//*[@id='release-3']//h6//following-sibling::span/a").text
print(releasedate_text)
'''
releasedate_text=driver.find_element(By.XPATH,f"//span[text()='{releaseversion}']//ancestor::p//following-sibling::div//h6//a").text
print(releasedate_text)