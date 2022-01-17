import random

sensors = ['Termo', 'Light', 'Water_out', 'Open_door', 'Work_TV', 'BERKYT']

for i in range(100_000):
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
    sensor.send(('{name_sensor}_sensor: ' + str(random.randint(1, 20))).encode('utf-8'))
    time.sleep(1)
'''
        )
