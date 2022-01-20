import asyncio


class EchoServerProtocol(asyncio.Protocol):
    # Вызывается если соединение с сервером было
    # установлено!
    def connection_made(self, transport):
        # transport как я понял это
        # объект соединения
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        # Ссылка на transport.
        self.transport = transport

    # Called when some data is received.
    # The argument is a bytes object.
    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(message))
        self.transport.write(data)

        print('Close the client socket')
        # Закрывает соединение после того, как получит
        # Какой - то запрос.
        self.transport.close()

    def connection_lost(self, exc):
        print('Connection is lost!')


class Server(EchoServerProtocol):
    def __init__(self, host, port):
        asyncio.run(self.start_server(host, port))

    @staticmethod
    async def start_server(host, port):
        loop = asyncio.get_running_loop()

        server = await loop.create_server(
            lambda: EchoServerProtocol(),
            host, port)

        async with server:
            # Метод Server.serve_forever() начинает принимать
            # подключения, пока сопрограмма не будет отменена.
            # Отмена задачи serve_forever приводит к закрытию сервера.
            #
            # Представляет собой сопрограмму.
            #
            # Этот метод можно вызвать, если сервер уже принимает
            # соединения. На один объект Server может существовать
            # только одна задача Server.serve_forever().
            await server.serve_forever()
