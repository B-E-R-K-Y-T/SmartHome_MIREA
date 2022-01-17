# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import os
import threading
import generate_docker_compose as gdc
import joke

sensors = input('Введите типы сенсоров через запятую: ')
sensors = sensors.replace(' ', '').split(',')
path = 'sensors'

if not os.path.exists(f'{path}'):
    os.mkdir(f'{path}')

while True:
    try:
        quality = int(input('Введите кол-во сенсоров: '))
    except Exception as e:
        print(e)
        continue
    else:
        break


def create_sensor(type_sensor):
    for i in range(1, quality + 1):
        name_sensor = type_sensor + '_' + str(i)

        gdc.create_dc(name_sensor)

        if not os.path.exists(f'{path}/{name_sensor}'):
            os.mkdir(f'{path}/{name_sensor}')

        if os.path.exists(f'{path}/{name_sensor}'):
            with open(f'{path}/{name_sensor}/{name_sensor}.py', 'w') as f:
                f.write(
                    f'''# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import sensors.client as client
import random
import time
import joke

sensor = client.Client('127.0.0.1', 1234).get_client()

while True:
    bool_list = [True, False]

    if '{name_sensor}' != 'Termo{'_' + str(i)}':
        sensor.send(('{name_sensor}_sensor: ' + str(random.choice(bool_list))).encode('utf-8'))
        time.sleep(1)
    else:
        sensor.send(('{name_sensor}_sensor: ' + str(random.randint(1, 20))).encode('utf-8'))
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
