# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import sensors.client as client
import random
import time
import joke 

sensor = client.Client('127.0.0.1', 1234).get_client()

while True:
    bool_list = [True, False]

    if 'a_1' != 'Termo_1':
        sensor.send(('a_1_sensor: ' + str(random.choice(bool_list))).encode('utf-8'))
        time.sleep(1)
    else:
        sensor.send(('a_1_sensor: ' + str(random.randint(1, 20))).encode('utf-8'))
        time.sleep(1)
