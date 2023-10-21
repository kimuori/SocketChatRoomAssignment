import sys
import threading
import socket
from time import sleep

'''
    This program is the client side that acts as a user interacting with the
    chatroom. They can do PM, DM, or Exit. Every client will enter an IP address
    and connect with their own port number.
    
    This program can have multiple instances of clients as long as they have different
    port numbers that does not conflict with other clients' port numbers.

    @author:
        Jemina
    
    @Note to the professor: 
        A fellow classmate from this class, Darren Isaacson, we 
        have collaborated on this assignment and made our own renditions of
        this assignment. I want to give him credit for the DM idea when you see his work, 
        and I want to be honest with this assignment. His implementation 
        actually works, but mines' a bit goofy as it sends the DM 3 times.

'''

'''
    receive() method to receive the message from what the server sends.
    The client will see public messages and their own sent messages only.
'''
def receive():
    while True:
        try:
            # message = input('>')
            message, _ = client.recvfrom(1024)  # this user receives other public msgs from other clients
            print(">>" + message.decode())  # their own msg will also show up

        except:
            pass

'''
    handler() method to handle messages that the client types.
    When client types PM/DM command, it will send a PM/DM payload to the server.
    When the client types a non command, it will treat that command the same as PM and sends it to the server.
    When the client types EX, it will send the message to the server to disconnect the client.
'''
def handler():
    print("[Type a message type (PM/DM) (EX to exit)]")
    while True:
        sleep(2)
        # print("Type a command. 'DM'/'EX'")
        message = input("")  # indicates local client

        if message.upper() == "EX":  # if user decides to exit
            # msg sends to notify all clients that this client has left
            client.sendto(f"EX| [{name} left the server]".encode(),
                          (server_name, 9999))  # sends message to server via line 60
            print('>>[You left the server]')  # local console message of this user leaving
            client.close()  # closes the client
            sys.exit(0)  # exits the client from program

        elif message.upper() == "PM":  # PUBLIC MESSAGE
            public_msg = input("Type your public message: ")  # local prompt for the client to write a message payload
            client.sendto(f"PM| {name}: {public_msg}".encode(), (server_name, 9999))

        elif message.upper() == "DM":  # DIRECT MESSAGE
            direct_msg = input("Type your direct message: ")  # local prompt for the client to write a message payload
            reciever = input("Type username: ")  # local prompt for client to type the other client's name
            client.sendto(f"DM| {name}> {reciever}: {direct_msg}".encode(), (server_name, 9999))

        else:  # DEFAULT PUBLIC MESSAGE if user does not type "PM".
            client.sendto(f"PM| {name}: {message}".encode(), (server_name, 9999))  # the PM will still be acknowledged


'''
    Main method to check the CMD arguments to connect the client to the server.
    Main will also run threads to receive and handle payloads.
'''
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

    # sends first ACK msg of a client's username connecting to server
    client.sendto(f"UN| {name}".encode(), (server_name, 9999))
    # local print message of chat instructions.
    print('-' * 15)
    print('INSTRUCTIONS: \n*Type a message and hit enter.\n* You may chose the command lines below:')
    print('   1. "EX"/"ex" to exit program.')
    print('   2. "PM"/"pm" for public message. No command is PM by default!')
    print('   3. "DM"/"dm" for direct message. You will be asked for username.')
    print('-' * 15)

    # client threading starts
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    handler_thread = threading.Thread(target=handler)
    handler_thread.start()