import threading
import socket
import queue

messages = queue.Queue()

# store clients
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 9999))

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
                        name = message.decode()[message.decode().index(":")+1:]
                        server.sendto(f'{name} joined!'.encode(), c)
                    else:
                        server.sendto(message, c)
                except:
                    clients.remove(c)


receive_thread = threading.Thread(target=receive)
broadcast_thread = threading.Thread(target=broadcast)
receive_thread.start()
broadcast_thread.start()
