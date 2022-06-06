import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# os.environ['PATH'] += "C:/SeleniumDriver"

# path = Service("C:/SeleniumDriver/chromedriver.exe")

driver = webdriver.Edge()

driver.get("https://opensource-demo.orangehrmlive.com")

user_name = driver.find_element(by=By.NAME, value="txtUsername")
user_name.send_keys("admin")

user_pass = driver.find_element(by=By.ID, value="txtPassword")
user_pass.send_keys("admin123")
 
btn = driver.find_element(by=By.ID, value="btnLogin")
btn.click()


actual_title = driver.title
expected_title = "OrangeHRM"
if actual_title == expected_title:
    print("Test Passed")
else:
    print("Test Failed")

