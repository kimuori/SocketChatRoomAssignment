import sys
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
    name = input("Nickname: ")
    server_name = input("Server IP: ")
    password = input("password (will not do anything): ")

    # check user function
    #

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind((server_name, random.randint(8000, 9000)))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    # sends this msg of client info to server
    client.sendto(f"ACK USERNAME: {name}".encode(), (server_name, 9999))
    # local print message of chat instructions.
    print('INSTRUCTIONS:\n* Type a message and hit enter.\n* You may chose the command lines below:')
    print('   1. "EX"/"ex" to exit program.')
    while True:
        message = input(">>") # indicates a message being passed in the server

        if message.upper() == "EX": #if user decides to exit
            # msg sends to notify all clients that this client has left
            client.sendto(f"[{name} left the server.]".encode(), (server_name, 9999))
            print('>>You left the server.')  # local message of this user leaving
            client.close()  # closes the client
            sys.exit(0)  # exits the client from program

        else:
            # msg = input('> ')
            client.sendto(f"{name}: {message}".encode(), (server_name, 9999))
