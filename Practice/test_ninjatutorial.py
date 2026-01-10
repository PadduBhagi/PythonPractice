import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup_and_teardown")
class TestNinja:
    def test_searchProduct(self):
        self.driver.find_element(By.XPATH, "//*[@name='search']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element(By.XPATH, "//*[@name='search']").send_keys("Hp")
        self.driver.find_element(By.XPATH,"//*[contains(@class,'btn-default')]").click()
        assert self.driver.find_element(By.XPATH, "//a[contains(text(),'HP')]").text.__contains__("HP"),"given product displayed"

    def test_registeraccountwithvalidcredentials(self):
        self.driver.find_element(By.XPATH, "//li[@class='dropdown']//a[@title='My Account']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//*[contains(@class,'dropdown-menu-right')]/li/a[text()='Register']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,"//h1[text()='Register Account']").text.__eq__("Register Account"),"account registered page not displayed"
        self.driver.find_element(By.NAME,"firstname").send_keys("sreenu")
        self.driver.find_element(By.NAME,"lastname").send_keys("poola")
        self.driver.find_element(By.NAME,"email").send_keys("sreenu2025@gmail.com")
        self.driver.find_element(By.ID,"input-telephone").send_keys("123456789")
        self.driver.find_element(By.NAME,"password").send_keys("12345")
        self.driver.find_element(By.NAME, "confirm").send_keys("12345")
        self.driver.find_element(By.XPATH,"//*[@type='checkbox' and @name='agree']").click()
        self.driver.find_element(By.XPATH,"//*[@type='submit']").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element(By.XPATH,"//h1[text()='Register Account']").text.__eq__("Register Account")
    def test_loginpageverify(self):
        self.driver.find_element(By.XPATH,"//li[@class='dropdown']//a[@title='My Account']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,"//*[contains(@class,'dropdown-menu-right')]/li/a[text()='Login']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,"//*[@name='email']").send_keys("sreenu2025@gmail.com")
        self.driver.find_element(By.XPATH, "//*[@name='password']").send_keys("12345")
        self.driver.find_element(By.XPATH,"//*[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//h2[text()='My Account']").text.__eq__("My Account")
        self.driver.find_element(By.XPATH, "//li[@class='dropdown']//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "//*[contains(@class,'dropdown-menu-right')]/li/a[text()='Logout']").click()


