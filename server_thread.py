# ======================================================================================================================

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

#
# import socket
# import os
#
# serv_sock = socket.socket(socket.AF_INET,      # задаем семейство протоколов 'Интернет' (INET)
#                           socket.SOCK_STREAM,  # задаем тип передачи данных 'потоковый' (TCP)
#                           proto=0              # выбираем протокол 'по умолчанию' для TCP, т.е. IP
#                           )
# print(type(serv_sock))                         # <class 'socket.socket'>
# # print(os.fork())
#
# # чтобы привязать сразу ко всем, можно использовать ''
# serv_sock.bind(('127.0.0.1', 53210))
#
# # 10 - это размер очереди входящих подключений, т.н. backlog
# serv_sock.listen(10)
#
# # Пример чтения и записи данных в клиентский сокет
# while True:
#     # Бесконечно обрабатываем входящие подключения
#     # получить соединение из этой очереди
#     client_sock, client_addr = serv_sock.accept()
#     print('Connected by', client_addr)
#
#     while True:
#         # Пока клиент не отключился, читаем передаваемые
#         # им данные и отправляем их обратно
#         data = client_sock.recv(1024)
#         if not data:
#             # Клиент отключился
#             break
#         client_sock.sendall(data)
#
#     client_sock.close()
