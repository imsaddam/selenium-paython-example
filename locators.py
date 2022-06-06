from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browser_path = Service("C:/SeleniumDriver/chromedriver.exe")

driver = webdriver.Chrome(service=browser_path)

driver.get("https://www.phptravels.net/login")
driver.maximize_window()


email_id = driver.find_element(by=By.NAME, value='email')
email_id.send_keys("agent@phptravels.com")

password = driver.find_element(by=By.NAME, value='password')
password.send_keys('demoagent')

login_btn = driver.find_element(by=By.CLASS_NAME, value='ladda-label')
login_btn.click()


