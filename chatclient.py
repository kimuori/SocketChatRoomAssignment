import sys
import threading
import socket


def receive():
    while True:
        try:
            # message = input('>')
            message, _ = client.recvfrom(1024) # this user receives other public msgs from other clients
            # print("$$" + message.decode())  #  their own msg will also show up
            print(message.decode())

        except:
            pass


if __name__ == '__main__':
    # use: 127.0.0.1 as server_name
    if len(sys.argv) < 3 or sys.argv[2] == "9999":
        print("CDM Instructions: 'python chatclient.py [IP address] [port num =/= 9999] [username]'")
        print("DO NOT USE PORT NUMBER '9999'. ")
        print("This program will close now.")
        sys.exit(0)  # exits the client from program

    server_name = sys.argv[1]
    client_port = int(sys.argv[2])
    name = sys.argv[3]

    # binds the client to a socket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind((server_name, client_port))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    # sends this msg of client info to server
    client.sendto(f"ACK USERNAME: {name}".encode(), (server_name, 9999))
    # local print message of chat instructions.
    print('INSTRUCTIONS:\n* Type a message and hit enter.\n* You may chose the command lines below:')
    print('   1. "EX"/"ex" to exit program.')

    while True:
        message = input(">>") # indicates local client

        if message.upper() == "EX": #if user decides to exit
            # msg sends to notify all clients that this client has left
            client.sendto(f"[{name} left the server]".encode(), (server_name, 9999)) # sends message to server via line 60
            print('>>You left the server.')  # local console message of this user leaving
            client.close()  # closes the client
            sys.exit(0)  # exits the client from program

        else:
            # msg = input('> ')
            client.sendto(f"{name}: {message}".encode(), (server_name, 9999))
