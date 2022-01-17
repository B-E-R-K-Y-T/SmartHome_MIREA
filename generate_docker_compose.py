# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import os

if not os.path.exists(f'server'):
    os.mkdir(f'server')

with open('__init__.py', 'w') as f:
    f.write('''# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

# Пакет - файл.
''')


with open(f'server/server_thread.py', 'w') as f:
    f.write(
        '''# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================



import socket
import threading
from other.config import IP, PORT

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

with open(f'server/Dockerfile', 'w') as f:
    f.write(
            '''# ======================================================================================================================

# Authors: BERKYT and Александр Хаметзянов

# ======================================================================================================================

FROM python:3.9

WORKDIR /server

COPY . .

ADD server_thread.py /server

ENV PYTHONUNBUFFERED 1

EXPOSE 1234
    '''
        )

with open(f'docker-compose.yaml', 'w') as f:
    f.write(
         f'''# ======================================================================================================================

# Authors: BERKYT and Александр Хаметзянов

# ======================================================================================================================


version: "3.2"
services:

    server:
        container_name: server
        build: server/
        command: python ./server_thread.py
        network_mode: host
        ports:
            - 1234:1883     
        environment:
            - PYTHONUNBUFFERED=1
    
        
'''
     )


def create_dc(name_sensor):
    with open(f'docker-compose.yaml', 'a') as f:
        f.write(
            f'''
   
    {name_sensor}:
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
        
'''
        )
