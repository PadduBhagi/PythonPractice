import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller

print("RUNNING THIS FILE")
driver=webdriver.Chrome()
driver.maximize_window()
#driver.get("https://demo.automationtesting.in/FileUpload.html")
driver.get("https://demoqa.com/upload-download")
time.sleep(5)
#driver.find_element(By.ID,"uploadFile").send_keys(r"D:\OLD F(Life)\sws\abc.txt")
#driver.find_element(By.ID,"input-4").send_keys(r"D:\OLD F(Life)\sws\abc.txt")

'''
#upload using autoit
autoit.win_wait_active("Open")   # dialog title
autoit.control_set_text("Open", "Edit1", file_path)
autoit.control_click("Open", "Button1")
'''
#upload using payautogui
'''
uploadbutton=driver.find_element(By.ID,"uploadFile")
driver.execute_script("arguments[0].style.display='block'",uploadbutton)
driver.execute_script("arguments[0].click();",uploadbutton)
path = r"D:/OLD F(Life)/sws/abc.txt"
pyautogui.write(path)
pyautogui.press('enter')
time.sleep(10)
import os
print("RUNNING FILE:", os.path.abspath(__file__))

keyboard=Controller()
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.element_to_be_clickable((By.ID,"uploadFile")))
elem = driver.find_element(By.ID, "uploadFile")
elem.click()
print("Displayed:", elem.is_displayed())
print("Enabled:", elem.is_enabled())
#driver.execute_script("arguments[0].scrollIntoView('true');",elem)
#driver.execute_script("arguments[0].click();",elem)
time.sleep(5)
path = r"D:/OLD F(Life)/sws/abc.txt"
keyboard.type(path)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(10)
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time
import os

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/upload-download")
time.sleep(5)
# Click the button that opens file dialog
driver.find_element(By.ID, "uploadFile").click()
time.sleep(1)

# Prepare file path
file_path = os.path.abspath(r"D:\OLD F(Life)\sws\abc.txt")   # place sample.txt in project folder

# Pynput keyboard controller
keyboard = Controller()

# Type file path
for char in file_path:
    keyboard.type(char)

# Press Enter
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
'''
# Click Upload
driver.find_element(By.ID, "file-submit").click()

time.sleep(2)

# Validation
msg = driver.find_element(By.TAG_NAME, "h3").text
assert msg == "File Uploaded!", "Upload failed"
'''
print("Upload success!")

driver.quit()




