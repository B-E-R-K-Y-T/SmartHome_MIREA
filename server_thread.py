# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import socket
import threading
from other.config import ip, port

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
server.bind((ip, port))

server.listen()

users = []


def listening_user(user):
    print('Listening user...')

    while True:
        data = user.recv(1024).decode('utf-8')
        print(f'User send = {data}')


def start_server():
    while True:
        user_socket, address = server.accept()

        print('Connected.')

        users.append(user_socket)
        accepted_user = threading.Thread(
            target=listening_user,
            args=(user_socket,)
        )

        accepted_user.start()


if __name__ == '__main__':
    start_server()
