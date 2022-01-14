# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import socket
import asyncio
from other.config import ip, port

event_loop = asyncio.get_event_loop()
clients = {
    'user_socket': [],
    'data': [],
}

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
server.bind((ip, port))

server.listen()


async def message():
    await asyncio.sleep(0.4)


async def accept_sockets():
    while True:
        user_socket, address = await event_loop.sock_accept(server)
        print(f'User <{address[0]}> connected!')
        clients['user_socket'].append(user_socket)

        await listen_socket(clients['user_socket'][-1])


async def listen_socket(user_socket=None):
    if not user_socket:
        return

    while True:
        clients['data'].append(
            event_loop.sock_recv(user_socket, 1024)
        )

        print(await event_loop.sock_recv(user_socket, 1024).decode('utf-8'))

        await message()


async def main():
    tasks = [
        asyncio.create_task(accept_sockets()),
        asyncio.create_task(listen_socket()),
    ]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
