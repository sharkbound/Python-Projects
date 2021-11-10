from socket import socket

connection = socket()
connection.connect(('127.0.0.1', 9999))

print(connection.recv(100))
connection.send(input('>>> ').encode())
print(connection.recv(100))
