import threading
import socket
import queue

'''
    This program is the server that orchestrates the acknowledgements and
    sending messages to broadcast or to DM.
    
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
    receive() method to recieve message that is coming from the client.
    The messages will be put on a queue.
'''
def receive():
    while True:
        try:
            message, address = server.recvfrom(1024)
            q_message.put((message, address))  # puts message and client address on queue

        except:
            pass

'''
    broadcast() method shows up the messages on the client's end.
    It will pop off messages form the queue and parses the acknowledgements
    and sends the message according to the client's given payload.
    
    When a client sends a UN payload, it will acknowledge that the client is connected and connects them.
    When a cleint sends a PM/DM payload, it will acknowledge their command and send the message accordingly.
    When a client sends a EX payload, it will acknowledge their command and disconnects the client.
'''
def broadcast():
    while True:
        # while the queue of messages is not empty
        while not q_message.empty():
            # gets message in the queue
            ack_message, address = q_message.get()  # gets message from client via ACK or general chat
            print("\n$$" + ack_message.decode())  # indicator in the server

            if address not in clients:
                clients.append(address)

            for c in clients:
                try:
                    if ack_message.decode().startswith("UN"):  # takes ACK of client's username
                        name = ack_message.decode()[ack_message.decode().index("|") + 2:]
                        # msg sends to notify all clients -- NOTE: this does not send
                        server.sendto(f"[{name} joined the chatroom!]".encode(), c) #sends the message to broadcast
                        profiles[name] = address

                    elif ack_message.decode().startswith("PM"): # takes ACK to send PM at client's end
                        pm_message = ack_message.decode()[ack_message.decode().index("|") + 2:]
                        server.sendto(pm_message.encode(), c) #sends the message to broadcast

                    elif ack_message.decode().startswith("DM"): # takes ACK to send DM to another client
                        sender = ack_message.decode()[
                               ack_message.decode().index("|") + 2: ack_message.decode().index(">")]
                        receiver = ack_message.decode()[
                               ack_message.decode().index(">") + 2: ack_message.decode().index(":")]
                        dm_message = ack_message.decode()[ack_message.decode().index(":") + 2:]
                        if receiver in profiles:
                            # print(profiles[receiver])
                            dm_msg = "[DM from " + sender + ": " + dm_message + "]"
                            server.sendto(dm_msg.encode(), profiles[receiver]) # broadcasts to the specified client only

                    elif ack_message.decode().startswith("EX"):
                        ex_msg = ack_message.decode()[ack_message.decode().index('|') + 2:]
                        server.sendto(f"{ex_msg}".encode(), c)  # sends the message to broadcast

                    else:  # if it's a normal message. Treats this as a normal PM.
                        server.sendto(ack_message, c)  # broadcast the message
                except:
                    clients.remove(c)  # removes the client in case the client logs out or crashes
                    del profiles[name]

'''
    Main method to set up the server to connect to its given port number.
    Main will also run threads to receive and broadcast coming from client.
'''

if __name__ == '__main__':
    q_message = queue.Queue()  # messages are treated as queue
    clients = []  # store clients
    profiles = {}

    # connects the server
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("", 9999))
    # sends local console message that the server is now running
    print('Server waits operation from client...')

    # receiver_thread = threading.Thread(target=receiver)
    # receiver_thread.start()
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    broadcast_thread = threading.Thread(target=broadcast)
    broadcast_thread.start()