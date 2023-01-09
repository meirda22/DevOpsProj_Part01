import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

user_id = input('Please enter ID to search by.\nPress Enter. \nBrowser will be open after 5 sec...')
user_id_extension: str = str(user_id)

time.sleep(5)

driver = webdriver.Chrome(service=Service("C:/DevOps/All_Projects/ChromeDriver/ChromeDriver"))

my_url = "http://127.0.0.1:5001/users/get_user_data/" + user_id_extension
driver.maximize_window()
driver.get(my_url)

my_url1 = driver.current_url
time.sleep(10)
driver.refresh()
my_url2 = driver.current_url
if my_url1 != my_url2:
    print("Not Equal")
else:
    print(my_url)

username_found = driver.find_element(By.ID, "userName")
print(username_found.text)

