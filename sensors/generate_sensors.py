import random
import os
import threading

os.mkdir('Termo')
os.mkdir('Light')
os.mkdir('Water_out')
os.mkdir('Open_door')
os.mkdir('Work_TV')
os.mkdir('BERKYT')

sensors = ['Termo', 'Light', 'Water_out', 'Open_door', 'Work_TV', 'BERKYT']


def create_sensor(folder, sensor):
    for i in range(100_000):
        name_sensor = sensor + '_' + str(i)
        with open(f'{folder}/{name_sensor}.py', 'w') as f:
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


t = []
for i in sensors:
    t.append(
        threading.Thread(
            target=create_sensor,
            args=(i, i)
        )
    )

    t[-1].start()




