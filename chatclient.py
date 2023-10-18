import threading
import socket
import random


def receive():
    while True:
        try:
            # message = input('>')
            message, _ = client.recvfrom(1024)
            print(message.decode())

        except:
            pass


if __name__ == '__main__':
    # use: 127.0.0.1 as server_name
    name = input('Nickname: ')
    server_name = input('Server IP: ')

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind((server_name, random.randint(8000, 9000)))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    client.sendto(f"SIGNUP TAG: {name}".encode(), (server_name, 9999))

    while True:
        message = input(">>")
        if message == "EX":
            client.sendto(f"{name} left the server.".encode(), (server_name, 9999))
            client.close()
            exit()

        else:
            # msg = input('> ')
            client.sendto(f"{name}: {message}".encode(), (server_name, 9999))
