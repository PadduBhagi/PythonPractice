import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("chrome://downloads/")
driver.maximize_window()
driver.implicitly_wait(20)


app_root = driver.find_element(By.CSS_SELECTOR, "downloads-manager")

shadow1 = driver.execute_script(
    "return arguments[0].shadowRoot", app_root
)

login_form = shadow1.find_element(By.CSS_SELECTOR, "login-form")

shadow2 = driver.execute_script(
    "return arguments[0].shadowRoot", login_form
)

username = shadow2.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("my_username")
