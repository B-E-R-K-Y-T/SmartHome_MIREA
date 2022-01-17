# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import socket
import python_static_type as st


# noinspection PyGlobalUndefined
class Client:
    client = None

    def __init__(self, ip: str, port: int):
        global client

        client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        client.connect((ip, port))

    def get_client(self):
        global client
        return client
