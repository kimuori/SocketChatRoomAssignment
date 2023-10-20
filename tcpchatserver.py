import threading
import socket

host = '127.0.0.1' #the localhost
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# listing empty lists and it will store clients and nicknames
clients = []  # ip addressese
nicknames = []
users = {'bill':'123', 'james':'321'}

# broadcast
''' sends message to all clients currently connected to the server '''
def broadcast(message):
    for client in clients:
        client.send(message)

# handle the client connection
def handle(client):
    while True:
        try:
            # broadcasting messages
            message = client.recv(1024)
            broadcast(message)  # broadcasts the message
        except:
            #remove and close clients
            index = clients.index(client)  # find the client that failed
            clients.remove(client)  # remove the client
            client.close()  # close the connection to the client
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)  # remove the client's nickname
            break  # terminates


# receive method
def receive():
    # sends local consolse message that the server is running
    print('Server is ready to listen...')

    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        # request and store nickname
        client.send('NICK'.encode('ascii'))  # sends the NICK to the client
        nickname = client.recv(1024).decode('ascii')
        # client.send('PASS').encode('ascii')
        # password = client.recv(1024).decode(ascii)

        # while True:
        #   try:
        #       if users[nickname] == password: ....
        #           clients.append(client)
        #           nicknames[nickname]
        #           break
        #   except: ....
        #        client.send("USername/password is incorrect. Try again.")
        #        client.send
        nicknames.append(nickname)
        clients.append(client)

        # print and broadcast nickname
        print(f'Nickname is "{nickname}"')
        broadcast(f'{nickname} joined this chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        # Start handling Thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
