##Method-1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# import time

## Method-2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import requests
paths= r"E:\PyCharm\chromedriver.exe"

## Importing Options
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options= Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)

# driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(3)

## Display cookies before login
print("Coding for printing the Cookie Details")
print("URL: ",driver.current_url)
print("Title:", driver.title)
print("Cookies Before Login:")
cookies_before_login= driver.get_cookies()
for cookie in cookies_before_login:
    driver.add_cookie(cookie)
    print(cookie)

## Logging in
username=driver.find_element(By.ID,"user-name")
pwd=driver.find_element(By.ID,"password")
login=driver.find_element(By.ID,"login-button")

username.send_keys("standard_user")
pwd.send_keys("secret_sauce")
login.click()
time.sleep(3)

### Display cookies after login
print("Cookies After Login:")
cookies_after_login= driver.get_cookies()
for cookie1 in cookies_after_login:
    print(cookie1)

# Log out from the dashboard
menu_button=driver.find_element(By.ID,"react-burger-menu-btn")
menu_button.click()
logout= driver.find_element(By.ID,"logout_sidebar_link")
logout.click()
time.sleep(3)

## Checking Cookie setting
print("Cookies After LogOut:")
cookie_logout=driver.get_cookies()
for cookie2 in cookie_logout:
    print(cookie2)

driver.quit()
