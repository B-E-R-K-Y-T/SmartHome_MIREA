# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import client
import random
import time

# client = socket.socket(
#     socket.AF_INET,
#     socket.SOCK_STREAM
# )
# client.connect(('127.0.0.1', 1234))

client = client.Client('127.0.0.1', 1234)
client = client.get_client()

while True:
    client.send(('Termo: ' + str(random.randint(1, 20))).encode('utf-8'))
    time.sleep(1)
