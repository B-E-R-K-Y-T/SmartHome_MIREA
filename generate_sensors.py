# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import os
import threading

sensors = ['Thermo', 'Light', 'Water_out', 'Open_door', 'Work_TV', 'BERKYT']
path = 'sensors'
quality = 100


def create_sensor(sensor):
    for i in range(0, quality + 1):
        name_sensor = sensor + '_' + str(i)

        if not os.path.exists(f'{path}'):
            os.mkdir(f'{path}')
        if not os.path.exists(f'{path}/{name_sensor}'):
            os.mkdir(f'{path}/{name_sensor}')

        if os.path.exists(f'{path}/{name_sensor}'):
            with open(f'{path}/{name_sensor}/{name_sensor}.py', 'w') as f:
                f.write(
                    f'''# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

from sensors import client
import random
import time
import code

sensor = client.Client('127.0.0.1', 1234).get_client()

while True:
    bool_list = [True, False]

    if 'BERKYT_0' != 'Termo_0':
        sensor.send(('BERKYT_0: ' + str(random.choice(bool_list))).encode('utf-8'))
        time.sleep(1)
    else:
        sensor.send(('BERKYT_0: ' + str(random.randint(1, 20))).encode('utf-8'))
        time.sleep(1)
'''
                )
            with open(f'{path}/{name_sensor}/Dockerfile', 'w') as f:
                f.write(
                    f'''# ======================================================================================================================

# Authors: BERKYT and Александр Хаметзянов

# ======================================================================================================================

FROM python:3.9

WORKDIR /{name_sensor}

COPY . .

ADD {name_sensor}.py /{name_sensor}

ENV PYTHONUNBUFFERED 1

EXPOSE 1234
'''
                )


t = []
for sensor in sensors:
    t.append(
        threading.Thread(
            target=create_sensor,
            args=(sensor,)
        )
    )

    t[-1].start()
