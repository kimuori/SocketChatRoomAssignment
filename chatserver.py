import threading
import socket
import queue

def receive():

    while True:
        try:
          message, address = server.recvfrom(1024)
          messages.put((message, address))
        except:
            pass

def broadcast():
    while True:
        while not messages.empty():
            message, address = messages.get()
            print(message.decode())

            if address not in clients:
                clients.append(address)
            for c in clients:
                try:
                    if message.decode().startswith("SIGNUP TAG: "):
                        name = message.decode()[message.decode().index(":") + 1:]
                        server.sendto(f"{name} joined!".encode(), c)
                    else:
                        server.sendto(message, c)
                except:
                    clients.remove(c)

if __name__ == '__main__':
    messages = queue.Queue()

    clients = [] # store clients

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("", 9999))
    print('Server waits operation from client...')

    receive_thread = threading.Thread(target=receive)
    broadcast_thread = threading.Thread(target=broadcast)
    receive_thread.start()
    broadcast_thread.start()
