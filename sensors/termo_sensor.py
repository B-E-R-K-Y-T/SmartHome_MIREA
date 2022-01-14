# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import socket
import random
import time

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
client.connect(('127.0.0.1', 1234))

while True:
    client.send(('Termo: ' + str(random.randint(1, 20))).encode('utf-8'))
    time.sleep(1)
