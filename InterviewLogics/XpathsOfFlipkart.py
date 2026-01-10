from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[contains(@placeholder,'Search for Products')]").send_keys("mobiles")
list0fMobiles=driver.find_elements(By.XPATH,"//ul/li//a[contains(@href,'/search?q=')]")
for mobile in list0fMobiles:
    print(mobile.text)
    if "samsung" in mobile.text:
        mobile.click()
mobilestext=driver.find_elements(By.XPATH,"//*[@class='ZFwe0M row']/div[1]/div[1]")
for texts in mobilestext:
    print(texts.text)
