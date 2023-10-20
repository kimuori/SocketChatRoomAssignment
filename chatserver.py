import threading
import socket
import queue


def receive():
    while True:
        try:
            message, address = server.recvfrom(1024)
            q_message.put((message, address))  # put on queue
        except:
            pass

def broadcast():
    while True:
        while not q_message.empty():
            message, address = q_message.get()  # gets message from client via line 60
            print("**" + message.decode())

            if address not in clients:
                clients.append(address)

            for c in clients:
                try:
                    if message.decode().startswith("ACK USERNAME: "):
                        # chat line formatting
                        name = message.decode()[message.decode().index(":") + 2:]
                        # msg sends to notify all clients
                        server.sendto(f"[{name} joined the chatroom!]".encode(), c)

                    else:
                        server.sendto(message, c)
                except:
                    clients.remove(c)


if __name__ == '__main__':
    q_message = queue.Queue()  # messages are treated as queue

    clients = []  # store clients
    profiles = {}

    # connects the server
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("", 9999))
    # sends local console message that the server is now running
    print('Server waits operation from client...')

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    broadcast_thread = threading.Thread(target=broadcast)
    broadcast_thread.start()
