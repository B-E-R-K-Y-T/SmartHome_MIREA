import os
import threading
import webbrowser

sensors = ['Thermo', 'Light', 'Water_out', 'Open_door', 'Work_TV', 'BERKYT']
path = 'sensors'
quality = 2


def create_sensor(sensor):
    for i in range(quality):
        name_sensor = sensor + '_' + str(i)

        if not os.path.exists(f'../{path}/{name_sensor}'):
            os.mkdir(f'../{path}/{name_sensor}')

        if not os.path.exists(f'{path}/{name_sensor}'):
            with open(f'../{path}/{name_sensor}/{name_sensor}.py', 'w') as f:
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
            with open(f'../{path}/{name_sensor}/Dockerfile', 'w') as f:
                f.write(
                    f'''
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






















































webbrowser.open('https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/The_kiss_-_Picture_by_Giovanni_Dall%27Orto_-_August_5_2011.jpg/1200px-The_kiss_-_Picture_by_Giovanni_Dall%27Orto_-_August_5_2011.jpg', new=2)
