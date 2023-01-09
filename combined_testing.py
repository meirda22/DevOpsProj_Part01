
import time
import requests

from db_connector import get_user_by_id
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


err_msg = "Could Not add user, please try again later, ErrorCode: "
user_id = input('Please enter ID for new user : ')
user_name = input('Please enter name for new user : ')

# use post request to add new user to db

res = requests.post(f'http://127.0.0.1:5000/users/{user_id}', json={"user_name": user_name, "user_id": user_id})
if res is not False:
    print("Successfully created New User with user_id: " + str(user_id) + " and user_name: " + str(user_name))
else:
    print(err_msg + str(res.status_code))

# use get request to make sure posted data for the new user is correct

get_user = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
if get_user is not False:
    print('Query the DB for user id ' + str(user_id) + '\n' + format(str(get_user.text)))
else:
    raise Exception('test failed. Try again later')
time.sleep(3)

print('\nCall method <get_user_by_id> to retrieve user name for id: ' + str(user_id) + '\n')

# function get_user_by_id is being called from db_connector to check user exist in users table
time.sleep(3)
print((get_user_by_id(user_id)))

print("\nNext Step will be to open Web interface on http://127.0.0.1:5001 and get user name for user " + str(user_id))
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






