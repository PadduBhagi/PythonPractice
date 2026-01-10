import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
search_box=driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']")
search_box.send_keys("iphone17")
search_box.send_keys(Keys.ENTER)
wait=WebDriverWait(driver,20)
wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='brandsRefinements']")))

brandnames=['Apple','OnePlus']
for name in brandnames:
  brand_checkbox=driver.find_element(By.XPATH,f"//*[contains(@aria-label,'{name}')]//label/i")
  driver.execute_script("arguments[0].click()",brand_checkbox)
  time.sleep(20)


selected_brandnames=driver.find_elements(By.XPATH,"//*[@type='checkbox']/ancestor::a[@aria-current='true']")

for selected in selected_brandnames:
  print(selected.text)


