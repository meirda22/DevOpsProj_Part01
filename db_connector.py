import datetime
import pymysql

## add_new_user will be called from the rest_app and will insert new user to db
## with the id passed in the POST request
## E.g.:

def add_new_user(user_id, username):
    table_name = 'users'
    schema_name = 'freedb_DevOpsProjectDB'

    # Establish DB connection #
    try:
        my_db = pymysql.connect(
            host='sql.freedb.tech',
            port=3306,
            user='freedb_kerenda1',
            passwd='TFmccNt*vH8d%&4',
            db=schema_name
        )
        my_db.autocommit(True)

        ##### Getting a cursor from Database #####
        my_cursor = my_db.cursor()
        current_date = datetime.datetime.now()

        # Inserting data into table
        my_sql: str = f"INSERT into {schema_name}.{table_name}(user_id, user_name, creation_date) " \
                      f"VALUES('{user_id}','{username}','{current_date}')"
        my_cursor.execute(my_sql)
    finally:
        my_cursor.close()
        my_db.close()

## update_user_by_id is being called from the rest_app, and will modify the name ofexisting user
## in db for the given user_id

def update_user_by_id(user_id,new_user_name):
    table_name = 'users'
    schema_name = 'freedb_DevOpsProjectDB'

    # Establishing a connection to DB ######
    try:
        my_db = pymysql.connect(
            host='sql.freedb.tech',
            port=3306,
            user='freedb_kerenda1',
            passwd='TFmccNt*vH8d%&4',
            db=schema_name
        )
        my_db.autocommit(True)

        ##### Getting a cursor from Database #####
        my_cursor = my_db.cursor()

       # Update table with new user name
        my_sql: str = f"UPDATE {schema_name}.{table_name} Set user_name = '{new_user_name}' where user_id = '{user_id}'"
        my_cursor.execute(my_sql)
    finally:
        my_cursor.close()
        my_db.close()

## get_user_by_id is being called from the rest_app and will return the user_name restored
## in db for the given user_id

def get_user_by_id(user_id):
    table_name = 'users'
    schema_name = 'freedb_DevOpsProjectDB'

    # Establishing a connection to DB ######
    try:
        my_db = pymysql.connect(
            host='sql.freedb.tech',
            port=3306,
            user='freedb_kerenda1',
            passwd='TFmccNt*vH8d%&4',
            db=schema_name
        )
        my_db.autocommit(True)

        ##### Getting a cursor from Database #####
        my_cursor = my_db.cursor()
        current_date = datetime.datetime.now()

        # Getting data from table
        my_sql: str = f"Select user_name,creation_date from {schema_name}.{table_name} where user_id = '{user_id}'"
        my_cursor.execute(my_sql)
        my_result = my_cursor.fetchone()
        return (my_result)

    finally:
        my_cursor.close()
        my_db.close()

## delete_user_by_id will be called from the rest_app and will delete existing user
## with the id passed in the DELETE request

def delete_user_by_id(user_id):
    table_name = 'users'
    schema_name = 'freedb_DevOpsProjectDB'

    # Establishing a connection to DB ######
    try:
        my_db = pymysql.connect(
            host='sql.freedb.tech',
            port=3306,
            user='freedb_kerenda1',
            passwd='TFmccNt*vH8d%&4',
            db=schema_name
        )
        my_db.autocommit(True)

        ##### Getting a cursor from Database #####
        my_cursor = my_db.cursor()

        # Getting data from table
        my_sql: str = f"Delete from {schema_name}.{table_name} where user_id = '{user_id}'"
        my_cursor.execute(my_sql)
    finally:
        my_cursor.close()
        my_db.close()

# below function is called from web_app.py
def get_user_name_from_db(user_id):
    table_name = 'users'
    schema_name = 'freedb_DevOpsProjectDB'

    # Establishing a connection to DB ######
    try:
        my_db = pymysql.connect(
        host='sql.freedb.tech',
        port=3306,
        user='freedb_kerenda1',
        passwd='TFmccNt*vH8d%&4',
        db=schema_name
        )
        my_db.autocommit(True)

        ##### Getting a cursor from Database #####
        my_cursor = my_db.cursor()

        # Getting data from table
        my_sql: str = f"Select user_name,creation_date from {schema_name}.{table_name} where user_id = '{user_id}'"
        my_cursor.execute(my_sql)
        my_result = my_cursor.fetchone()
        return (my_result[0])

    finally:
        my_cursor.close()
        my_db.close()




