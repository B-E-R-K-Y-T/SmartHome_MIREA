import socket

client_sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
client_sock.connect(
    ('127.0.0.1', 1234)
)
client_sock.sendall('Hello, world'.encode('utf-8'))
data = client_sock.recv(1024)
# client_sock.close()
print('Received', repr(data))
