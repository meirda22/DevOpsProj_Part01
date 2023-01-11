import time
import requests

time.sleep(10)
res1 = requests.get(f'http://127.0.0.1:5000/stop_server')
if res1 is not False:
    print('Server Stopped')
else:
    raise Exception('Could not stop server, Try again later...')

res2 = requests.get(f'http://127.0.0.1:5001/stop_server')
if res2 is not False:
    print('Server Stopped')
else:
    raise Exception('Could not stop server, Try again later...')


