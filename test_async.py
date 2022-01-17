import asyncio
import socket
import logging
import itertools

from other.config import IP, PORT

# Configure logging
logging.basicConfig(
    format='%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO
)

event_loop = asyncio.get_event_loop()
clients = {
    'client_socket': [],
    'address': [],
    'data': []
}

tcp_server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

tcp_server.bind(
    (IP, PORT)
)

tcp_server.listen()
# tcp_server.setblocking(False)


async def accept_client():
    print('2')
    while True:
        client_socket, client_address = await event_loop.sock_accept(tcp_server)

        print(f'Client {client_socket}: {client_address} connected!')
        clients['client_socket'].append(client_socket)
        clients['address'].append(client_address)

        await listening_client(client_socket)
        print('6')


async def listening_client(client_socket):
    print('3')
    while True:
        if not client_socket:
            break

        clients['data'].append(
            await event_loop.sock_recv(client_socket, 2048)
        )

        await event_loop.sock_sendall(
            clients['client_socket'][-1],
            clients['data'][-1]
        )
        print('4')
    print('5')


async def main():
    print('1')
    event_loop.create_task(accept_client())
    # event_loop.create_task(listening_client())
    # tasks = [
    #     asyncio.create_task(accept_client()),
    #     asyncio.create_task(listening_client()),
    # ]
    #
    # await asyncio.gather(*tasks)


if __name__ == '__main__':
    # asyncio.run(main())
    event_loop.run_until_complete(main())

