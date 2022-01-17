# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

with open(f'docker-compose.yaml', 'w') as f:
    f.write(
         f'''# ======================================================================================================================

# Authors: BERKYT and Александр Хаметзянов

# ======================================================================================================================


version: "3.2"
services:

    server:
        container_name: server
        build: server /
        command: python. /server_thread.py
        network_mode: host
        ports:
            - 1234: 1883     
        environment:
            - PYTHONUNBUFFERED = 1
    
        
'''
     )


def create_dc(name_sensor):
    with open(f'docker-compose.yaml', 'a') as f:
        f.write(
            f'''

    {name_sensor}:
        container_name: {name_sensor}
        build: light /
        command:
            python. /{name_sensor}.py
        network_mode: host
        ports:
            - 1234: 1234
        environment:
            - PYTHONUNBUFFERED = 1
        depends_on:
            - server
        
'''
        )
