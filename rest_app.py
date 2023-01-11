import signal

from flask import Flask, request
import os
from db_connector import add_new_user
from db_connector import get_user_name_from_db
from db_connector import update_user_by_id
from db_connector import delete_user_by_id

app = Flask(__name__)


# supported methods

@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def users(user_id):
    # Below method will add new user to DB
    if request.method == 'POST':

        # getting the json data payload from request
        request_data = request.json

        # treating request_data as a dictionary to get a specific value from key
        user_id = request_data.get('user_id')
        user_name = request_data.get('user_name')

        if add_new_user(user_id, user_name) is False:
            return {"status": "Error", "reason": "ID already exist", "Code": "500"}, 500
        else:
            return {"user id": user_id, "user name": user_name, "status": "OK", "Code": "200"}, 200  # status code

    # Below method will update existing user in DB
    elif request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json

        # treating request_data as a dictionary to get a specific value from key
        user_id = request_data.get("user_id")
        new_user_name = request_data.get("user_name")
        update_user = update_user_by_id(user_id, new_user_name)

        if update_user is False:
            return {"status": "Error", "reason": "No Such ID", "Code": "500"}, 500
        else:
            return {"user id": user_id, "user name": new_user_name, "status": "OK", "Code": "200"}, 200  # status code

    # Below method will get username from DB (related to the given user_id)

    elif request.method == 'GET':
        user_name = get_user_name_from_db(user_id)
        if not user_name:
            return {"status": "Error", "reason": "ID Not Found", "Code": "500"}, 500  # status code
        else:
            return {"user name": user_name, "status": "OK", "Code": "200"}, 200  # status code

    ####### Request is DELETE #########

    elif request.method == 'DELETE':
        user_name = delete_user_by_id(user_id)

        if not user_name:
            return {"status": "Error", "reason": "ID Not Found", "Code": "500"}, 500  # status code
        else:
            return {"user name": user_name, "status": "OK", "Code": "200"}, 200  # status code


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return "Server stopped"


app.run(host='127.0.0.1', debug=True, port=5000)
