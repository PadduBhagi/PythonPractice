from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='table1']")))
table=driver.find_element(By.XPATH,"//*[@id='table1']")
colsheads=driver.find_elements(By.XPATH,"//*[@id='table1']//th")
col=1
for head in colsheads:

    if (head.text.__eq__("Name")):
       names=driver.find_elements(By.XPATH,"//*[@id='table1']//tbody/tr/td["+str(col)+"]")
       for name in names:
           print(name)
col+=1


