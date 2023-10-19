#!/usr/bin/env python3
""" A multithreaded chat client """

import sys, socket, threading
from ipaddress import ip_address

def print_help():
    print(f'usage:\t{sys.argv[0]} <ip address> <port num>')
    sys.exit(1)
    
if len(sys.argv) > 1:
    try:
        ip = ip_address(sys.argv[1])
        HOST = str(ip)
    except ValueError:
        print('invalid ip address')
        print_help()
    try:
        PORT = int(sys.argv[2])
    except ValueError:
        print('invalid port')
        print_help()
else:
	HOST = '127.0.0.1'
	PORT = 1234	


def handle_input(sock):
    # Loop indefinitely to receive messages from server
    while True:
        msg = ''
        while not msg:
            try:
                recvd = sock.recv(1024)
            except (socket.error, ConnectionError) as e:
                print(f'Connection error {e}')
                sock.close()
                break
            msg = recvd.decode('utf-8')
        print(msg)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
    except socket.error as e:
        print(e)
        sys.exit(1) 
    print(f'Connected to {HOST}:{PORT}') 

    # Create thread for handling user input and message sending
    thread = threading.Thread(target=handle_input,
                              args=[sock],
                              daemon=True)
    thread.start()

    """ Prompt user for message and send it to server """
    print("Type messages, enter to send. 'q' to quit")
    while True:
        msg = input()
        if msg == 'q':
            # sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            sys.exit(0)
        try:
            sock.send(msg.encode())
        except (BrokenPipeError, ConnectionError) as e:
            print(f'Error: {e}')
            break
