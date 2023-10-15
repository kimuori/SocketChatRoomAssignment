import threading
import socket

host = '127.0.0.1'
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# listing empty lists
clients = []
nicknames = []

# broadcast
''' sends message to all clients currently connected to the server'''
def broadcast(message):
    for client in clients:
        client.send(message)


# handle
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break


# receive method
def receive():
    while True:
        client, address = server.accept()
        print('Connected with {}'.format(str(address)))

        # request and store nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # print and broadcast nickname
        print('Nickname is {}'.format(nickname))
        broadcast('{} joined!'.format(nickname).encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        # Start handling Thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
