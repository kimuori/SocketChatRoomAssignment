#!/usr/bin/env python3
""" A multithreaded chat server """
from socket import *
import sys, threading


def print_help():
    print(f'usage:\t{sys.argv[0]} <port num> port num betwenn 1200-65535')
    sys.exit(1)
    
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[2])
    except ValueError:
        print('invalid port')
        print_help()
else:
	PORT = 1234	

BUFSIZ = 1024
HOST = ''
ADDR = (HOST, PORT)



def handle_client(sock, addr):
    """ Receive one message and echo it back to client, then close socket """
    while True:
        try:
            msg = sock.recv(BUFSIZ)
            """
            while True:
                recv_msg = sock.recv(BUFSIZ)
                if recv_msg:
                    msg += recv_msg.decode()
                else:
                    break
            """
            #if msg:
            #print('msg from {}: {}'.format(addr, msg.decode()))
            modified_msg = msg.decode().upper()
            sock.send(modified_msg.encode())
        except (ConnectionError, BrokenPipeError) as e:
            print(f'Socket error: {e}')
            break
    # print('Closed connection to {}'.format(addr))
    # sock.close()

if __name__ == '__main__':
    listen_sock = socket(AF_INET, SOCK_STREAM)
    listen_sock.bind(ADDR)
    listen_sock.listen(5) 
    listen_sock.setsockopt( SOL_SOCKET, SO_REUSEADDR, 1 )
    srv_addr = listen_sock.getsockname()
    print(f'Listening on {srv_addr}')

    while True:
        client_sock, addr = listen_sock.accept()
        print(f'Client connected from: {addr}')

        # Create thread for handling user input and message sending
        thread = threading.Thread(target=handle_client,
                                  args=[client_sock, addr],
                                  daemon=True)
                                
        thread.start()