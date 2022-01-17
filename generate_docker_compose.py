# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import os

if not os.path.exists(f'server'):
    os.mkdir(f'server')

with open(f'server/server_thread.py', 'w') as f:
    f.write(
            '''# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import socket
import threading
from config import IP, PORT

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
server.bind((IP, PORT))

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

    '''
        )

with open(f'server/config.py', 'w') as f:
    f.write(
            '''# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

# Telegram-bot
# ----------------------------------------------------------------------------------------------------------------------

# link t.me/smart_home_mirea_bot
TOKEN = '5062184023:AAF-xY8uVWoZoC4u5WoiAGpf36UyDlqTHV8'

# ----------------------------------------------------------------------------------------------------------------------

# PostgreSQL
# ----------------------------------------------------------------------------------------------------------------------

HOST = 'localhost'
USER = 'postgres'
PASSWORD = '1488'
DATABASE = 'postgres'

# ----------------------------------------------------------------------------------------------------------------------

# Server
# ----------------------------------------------------------------------------------------------------------------------

IP = '127.0.0.1'
PORT = 1234

# ----------------------------------------------------------------------------------------------------------------------


    '''
        )

with open(f'docker-compose.yaml', 'w') as f:
        f.write(
            f'''# ======================================================================================================================

# Authors: BERKYT and Александр Хаметзянов

# ======================================================================================================================

version: "3.2"
services:

    # -------------------------------------------------------
    # Это контейнер для сервера.
    # -------------------------------------------------------
    server:
        container_name: server
        build: server/
        command: python ./server_thread.py
        network_mode: host
        ports:
            - 1234:1234     
        environment:
            - PYTHONUNBUFFERED=1
    # -------------------------------------------------------
    
'''
        )


def create_dc(name_sensor):
    with open(f'docker-compose.yaml', 'a') as f:
        f.write(
            f'''
            
    # -------------------------------------------------------
    # Это контейнер для сервера.
    # -------------------------------------------------------    
    tv_1:
        container_name: {name_sensor}
        build: sensors/{name_sensor}/
        command:
            python ./{name_sensor}.py
        network_mode: host
        ports:
            - 1234:1234
        environment:
            - PYTHONUNBUFFERED=1
        depends_on:
            - server
    # -------------------------------------------------------
    
'''
        )
