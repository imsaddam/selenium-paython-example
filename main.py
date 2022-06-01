import os
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += "C:/SeleniumDriver"

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")

user_name = driver.find_element(by=By.NAME, value="txtUsername")
user_name.send_keys("admin")

user_pass = driver.find_element(by=By.ID, value="txtPassword")
user_pass.send_keys("admin123")

btn = driver.find_element(by=By.ID, value="btnLogin")
btn.click()


