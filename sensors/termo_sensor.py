# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import client
import random
import time

sensor = client.Client('127.0.0.1', 1234).get_client()

while True:
    sensor.send(('Termo: ' + str(random.randint(1, 20))).encode('utf-8'))
    time.sleep(1)
