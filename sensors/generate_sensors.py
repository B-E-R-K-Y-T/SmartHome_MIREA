import random
from rich.progress import track

sensors = ['Termo', 'Light', 'Water_out', 'Open_door', 'Work_TV', 'BERKYT']

for i in track(range(1_000_000), description='   Создаю python-датчики...'):
    name_sensor = random.choice(sensors) + '_' + str(i)
    with open(f'{name_sensor}.py', 'w') as f:
        f.write(
            f'''
# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import client
import random
import time

sensor = client.Client('127.0.0.1', 1234).get_client()

while True:
    bool_list = [True, False]
    
    if '{name_sensor}' != 'Termo{'_' + str(i)}':
        sensor.send(('{name_sensor}: ' + str(random.choice(bool_list))).encode('utf-8'))
        time.sleep(1)
    else:
        sensor.send(('{name_sensor}: ' + str(random.randint(1, 20))).encode('utf-8'))
        time.sleep(1)

'''
        )
