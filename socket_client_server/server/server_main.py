import socket
from threading import Thread


class ClientThread(Thread):
    def __init__(self, connection, address):
        super().__init__()
        self.connection = connection
        self.address = address

    def read(self, buf_size=1000):
        return self.connection.recv(buf_size).decode()

    def send(self, text: str):
        self.connection.send(text.encode())

    def run(self) -> None:
        try:
            print(f'CONNECTED: {self.connection=} {self.address=}')
            self.send('hello connection!')
            data = self.read(100)
            self.send(f'RETURN TO SENDER: {data}')
            self.connection.close()
        except Exception as e:
            print(e)


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(10)

    print('listening for connections...')
    while True:
        try:
            conn, address = server_socket.accept()
            ClientThread(connection=conn, address=address).start()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
