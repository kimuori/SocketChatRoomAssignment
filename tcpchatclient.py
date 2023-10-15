import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

nickname = input('Type your nickname: ')


def receive():
    while True:
        try:
            # this block will receive messages from the server
            message = client.recv(1024).decode('ascii')  # client receives from the server
            if message == 'NICK':  # server side sends the NICK message
                client.send(nickname.encode('ascii'))
                pass
            else:
                print(message)  # if it's not the client's nickname, it will print what the server is showing
        except:
            print('An error occurred!')
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()