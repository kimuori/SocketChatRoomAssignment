import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

nickname = input('Enter Username: ')
password = input('Enter password: ')

#def login():
#    while True:
#        username = input("Enter: ")

#        try:
#            message = client.recv(1024).decode('ascii')
#            if message == "USER":
#                client.send(username)

def receive():
    while True:
        try:
            # this block will receive messages from the server
            message = client.recv(1024).decode('ascii')  # client receives from the server
            if message == 'NICK':  # server side sends the NICK message
               client.send(nickname.encode('ascii'))
               pass

            #elif message == 'PASS':
            #    client.send(password.encode('ascii'))
            # else:
            #     print(message) # if it's not the client's nickname, it will print what the server is showing
        except:
            print('An error occurred!')
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

# login_thread = threading.thread(target=login)

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()