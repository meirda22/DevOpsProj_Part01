import signal

from flask import Flask
from db_connector import get_user_name_from_db
import os

app = Flask(__name__)


# Web interface will return the username of a given user id stored inside users table

@app.route('/users/get_user_data/<user_id>', methods={'GET'})
def get_user_name(user_id):
    user_name = get_user_name_from_db(user_id)  # function can be found under db_connector.py
    if not user_name:
        return "<h1 id='error'>" + "No User Found for ID : " + user_id + "</h1>"
    else:
        return "<h1 id='userName'>" + "User Name For User Id " + user_id + " is : " + user_name + "</h1>"

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return "Server stopped"


app.run(host='127.0.0.1', debug=True, port=5001)
