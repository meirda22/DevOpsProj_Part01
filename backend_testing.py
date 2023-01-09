import time
import requests
from db_connector import get_user_by_id

err_msg = "Could Not add user, please try again later, ErrorCode: "
user_id = input('Please enter ID for new user : ')
user_name = input('Please enter name for new user : ')

res = requests.post(f'http://127.0.0.1:5000/users/{user_id}',
                    json={"user_name": user_name, "user_id": user_id})
if res is not False:
    print("Successfully created New User with user_id: " + str(user_id) + " and user_name: " + str(user_name))
else:
    print(err_msg + str(res.status_code))

get_user = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
print('Query the DB for user id ' + str(user_id) + '\n' + format(str(get_user.text)))
time.sleep(3)
print('\nCall method <get_user_by_id> to retrieve user name for id: ' + str(user_id) + '\n')

# function get_user_by_id is being called from db_connector
time.sleep(3)
print((get_user_by_id(user_id)))





