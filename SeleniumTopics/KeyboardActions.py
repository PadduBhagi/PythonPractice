import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
textarea=driver.find_element(By.ID,"ta1")
textarea.send_keys(Keys.ENTER,"hai how are you")
action=ActionChains(driver)
action.send_keys(Keys.TAB).send_keys("hello").send_keys("""
asdcbbcnclknsaclkkkknksakjcaascnaklnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnbhargavannnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnxKXKJjabsxanssxclkasnc""").send_keys(Keys.ARROW_UP)\
 .send_keys(Keys.ARROW_UP).send_keys(Keys.ARROW_UP)\
 .send_keys(Keys.ARROW_UP).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).perform()
action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
action.send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
link=driver.find_element(By.XPATH,"//*[text()='SeleniumTutorial']")
action.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
time.sleep(20)
driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
time.sleep(10)
driver.execute_script("arguments[0].scrollIntoView(true)",driver.find_element(By.ID,"testdoubleclick"))
driver.execute_script("arguments[0].style.background='red'",driver.find_element(By.ID,"testdoubleclick"))
time.sleep(5)
action.double_click(driver.find_element(By.ID,"testdoubleclick")).perform()


time.sleep(10)
driver.find_element(By.ID,"myDropdown").is_displayed()

