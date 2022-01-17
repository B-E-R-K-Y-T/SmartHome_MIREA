# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

from sensors import client
import random
import time
import code

sensor = client.Client('127.0.0.1', 1234).get_client()

while True:
    bool_list = [True, False]

    if 'test_1' != 'Termo_1':
        sensor.send(('BERKYT_0: ' + str(random.choice(bool_list))).encode('utf-8'))
        time.sleep(1)
    else:
        sensor.send(('test_1_sensor: ' + str(random.randint(1, 20))).encode('utf-8'))
        time.sleep(1)
