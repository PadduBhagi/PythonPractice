import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(20)
search_box=driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']")
wait=WebDriverWait(driver,20)
wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='twotabsearchtextbox']")))
phone=input("enter iphone model")
search_box.send_keys(phone)
search_box.send_keys(Keys.ENTER)
time.sleep(10)
model=input("enter model along with spec")

xpath= f"//h2[contains(@aria-label,'{phone} {model}')]/following::span[@class='a-price-whole'][1]"
price=driver.find_element(By.XPATH,xpath).text
print(price)