import time
from asyncio import wait_for

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

#from SeleniumTopics.Locators import element

'''
Calendar type1:
driver=webdriver.Chrome()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.maximize_window()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.ID,"datepicker")))
driver.find_element(By.ID,"datepicker").click()
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='ui-datepicker-div']")))


def select_date(day,month,year):
    current_month=driver.find_element(By.CLASS_NAME,"ui-datepicker-month").text
    current_year=driver.find_element(By.CLASS_NAME,"ui-datepicker-year").text
    while current_month!=(month) or current_year != str(year):
        driver.find_element(By.XPATH,"//*[@title='Next']").click()
        current_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
        current_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

    driver.find_element(By.XPATH,"//*[text()="+str(day)+"]").click()
    #driver.find_element(By.XPATH,"//*[text()="+day+"]")
    time.sleep(30)
    driver.quit()

select_date(25,"December",2026)
'''

'''
------------------
driver.execute_script("document.getElementById('datepicker').value='25/12/2026'")
time.sleep(20)
---------------
'''

#calendar 2
driver=webdriver.Chrome()
driver.get("https://www.path2usa.com/travel-companion/")
driver.maximize_window()
wait=WebDriverWait(driver,20)
wait.until(expected_conditions.presence_of_element_located((By.ID,"form-field-travel_comp_date")))

element=driver.find_element(By.ID,'form-field-travel_comp_date')
driver.execute_script("arguments[0].scrollIntoView('true')",element)
time.sleep(30)
driver.find_element(By.ID,"form-field-travel_comp_date").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[contains(@class,'flatpickr-calendar')]")))

current_month=driver.find_element(By.CLASS_NAME,"cur-month").text
print(current_month)
current_year=driver.find_element(By.XPATH,"//*[contains(@class,'cur-year')]").get_attribute("min")
print(int(current_year))
month="January"
year=2026
while current_month<month or current_year<str(year):
    nextbutton=driver.find_element(By.CLASS_NAME,"//*[@class='flatpickr-next-month']")
    driver.execute_script("arguments[0].click()",nextbutton)

    current_month=driver.find_element(By.CLASS_NAME,"cur-month").text
    current_year=driver.find_element(By.XPATH,"//*[contains(@class,'cur-year')]").get_attribute("min")

    driver.find_element(By.XPATH,"//*[contains(@class,'flatpickr-day') and text()='31']").click()
    time.sleep(20)