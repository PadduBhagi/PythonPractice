'''import time
from asyncio import wait_for
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait until alert is present


from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import title_is, alert_is_present
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

wait=WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[contains(text(),'omayo (QAFox.com)')]")))

#get title and url
title=str(driver.execute_script("return document.title"))
print(title)
url=str(driver.execute_script("return document.URL"))
print(url)

#flashelement
header=driver.find_element(By.XPATH,"//*[text()='Page One']")
driver.execute_script("arguments[0].style.background='yellow'",header)
time.sleep(5)

#highlighting
driver.execute_script("arguments[0].style.border='3px solid red'",header)
time.sleep(5)

#page refresh
driver.execute_script("history.go(0)")

time.sleep(5)
#scrolling to particular element and total webpage
readonlytextbox=driver.find_element(By.ID,"rotb")
driver.execute_script("arguments[0].scrollIntoView('true')",readonlytextbox)

time.sleep(5)

#senkeys
readonlytextbox=driver.find_element(By.ID,"rotb")
driver.execute_script("arguments[0].value='Bhargava'",readonlytextbox)

driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")

time.sleep(5)




driver.execute_script("window.scrollTo(document.documentElement.scrollHeight,0)")
time.sleep(5)
#create custom alerts(information,prompt,confirmation)
driver.execute_script("alert('hello bhargav')")
driver.switch_to.alert.accept()
time.sleep(10)

driver.execute_script("prompt('what is your name')")
WebDriverWait(driver, 10).until(EC.alert_is_present())

promptalert=driver.switch_to.alert
WebDriverWait(driver, 10).until(EC.alert_is_present())

promptalert.send_keys("saarya")
time.sleep(5)
print(promptalert.text)
promptalert.accept()
time.sleep(5)

driver.execute_script("confirm('are you sure')")
time.sleep(5)
driver.switch_to.alert.dismiss()
time.sleep(5)
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Setup Chrome ---
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

# Wait until page loads
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'omayo (QAFox.com)')]"))
)

# --- Create and trigger a JS prompt ---
driver.execute_script("""
    window.showPrompt = function() {
        return prompt('what is your name?');
    }
""")

driver.execute_script("window.showPrompt();")

# Wait until the alert is visible
WebDriverWait(driver, 10).until(EC.alert_is_present())

# Switch to the alert (prompt)
alert = driver.switch_to.alert
print("Prompt text from website:", alert.text)

# The text you want to send
input_text = "bh"
WebDriverWait(driver, 20).until(EC.alert_is_present())
alert = driver.switch_to.alert
# Send the text into the prompt
alert.send_keys(input_text)
time.sleep(10)

# Accept (click OK)
alert.accept()
print("Entered text:", input_text)

# Wait a bit so you can see result before closing
time.sleep(3)
driver.quit()
'''
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

promptbutton=driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']")
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[text()='Click for JS Prompt']")))

promptbutton.click()
time.sleep(10)
alert1=Alert(driver)
alert1.send_keys("bhargava")

time.sleep(10)





