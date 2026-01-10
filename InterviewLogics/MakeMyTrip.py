import json
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(10)
from_city="Bengaluru"
to_city="Tirupati"
departure_date='10 June 2026'
depature_required_year=departure_date.split(" ")[2]
depature_required_month=departure_date.split(" ")[1]
depature_required_day=int(departure_date.split(" ")[0])



driver.find_element(By.XPATH,"//*[@alt='minimize']").click()
driver.find_element(By.XPATH,"//*[contains(@class,'close')]").click()
wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='fromCity']")))
from_city_tb=driver.find_element(By.XPATH,"//*[@id='fromCity']")
driver.execute_script("arguments[0].click()",from_city_tb)
driver.execute_script(f"arguments[0].value='{from_city}'",from_city_tb)
to_city_tb=driver.find_element(By.XPATH,"//*[@id='toCity']")
driver.execute_script("arguments[0].click()",to_city_tb)
driver.execute_script(f"arguments[0].value='{to_city}'",to_city_tb)

calendar=driver.find_element(By.XPATH,"//*[@data-cy='departureDate']")
driver.execute_script("arguments[0].click()",calendar)

current_selected_year_in_calendar=driver.find_element(By.XPATH,"(//div[@class='DayPicker-Caption'])[1]").text
selected_year_after_split=current_selected_year_in_calendar.split(" ")
current_selected_year=selected_year_after_split[1]
current_selected_month=str(selected_year_after_split[0])

while (int(current_selected_year)<int(depature_required_year)):
    next_button=driver.find_element(By.XPATH,"//*[@class='DayPicker-NavBar']//*[@aria-label='Next Month']")
    driver.execute_script("arguments[0].click()",next_button)
    current_selected_year_in_calendar = driver.find_element(By.XPATH, "(//div[@class='DayPicker-Caption'])[1]").text
    selected_year_after_split = current_selected_year_in_calendar.split(" ")
    current_selected_year = selected_year_after_split[1]


while (str(current_selected_month)!=str(depature_required_month)):
    next_button = driver.find_element(By.XPATH, "//*[@class='DayPicker-NavBar']//*[@aria-label='Next Month']")
    driver.execute_script("arguments[0].click()", next_button)
    current_selected_year_in_calendar = driver.find_element(By.XPATH,"(//div[@class='DayPicker-Caption'])[1]").text
    selected_year_after_split = current_selected_year_in_calendar.split(" ")
    current_selected_month = str(selected_year_after_split[0])



xpathcalendar=f"//div[contains(text(),'{depature_required_month}')]/ancestor::div[@class='DayPicker-Month']//div[@class='DayPicker-Body']//*[@class='dateInnerCell']/p[text()='{depature_required_day}']"
dateselection=driver.find_element(By.XPATH,xpathcalendar)
driver.execute_script("arguments[0].click()",dateselection)
travellar=driver.find_element(By.XPATH,"//*[@id='travellers']")
driver.execute_script("arguments[0].click()",travellar)
no_of_adults=3
adults=driver.find_elements(By.XPATH,"//*[@data-cy='adultRange']/following-sibling::ul/li")
for adult in adults:
    if (int(adult.text)==no_of_adults):
        adult.click()
    break
time.sleep(10)


