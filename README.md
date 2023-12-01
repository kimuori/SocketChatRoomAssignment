# Chat Room Socket Programming
This program was a part of my college course assignment to implement a UDP protocol in a chat room. There is also TCP protocol chatroom that has yet to be implemented.

## How to use UDP Chat Room Socket
Two programs must run together: `chatserver.py` and `chatclient.py`.
This program was tested using a Linux machine and terminal to run the program.

First, run the `chatserver.py` in the terminal. There is no need to put port number.
In the terminal, type the command below. This will start the program to start listening for clients.
>`python3 chatserver.py`
* NOTE: Interpreter may vary (e.g. 'py', 'python2', 'python3', etc. ) so type the first part according to your machine.

Second, run the `chatclient.py` in a separate terminal. There are specific instructions to type the arguemnt.
In the terminal, the instructions follows:
>`python3 chatclient.py [IP] [port num =/= 9999] [username]`. 

If this format is incorrectly formatted, it will end the program.
There are notes to keep in mind:
* The chatserver.py currently reserves port number 9999. 
* If typing `localhost` does not work for the IP address, try to type `127.0.0.1`, as an example.
* EXAMPLE OF THE COMMAND: `python chatclient 127.0.0.1 7890 iLoveHunting123`

You can create multiple instances of `chatclient.py` as long as the client instance does not occupy the port number already reserved by another client!

<u><b>Information of the command lines 'PM', 'DM', and 'EX'</b></u>
* EX (Exit) disconnects the client from the server.
* PM (Public Message) allows clients to broadcast their messages to other clients. 
  The client can simply choose to type any message without declaring 'PM'. 
  The server will still treat that message as PM by default.
* DM (Direct Message) is a private message between client and another client.
  The client will be asked to type the username of the client they want to interact with.


## Programming Reference 
[UDP skeleton reference (NeuralNine)](https://youtu.be/3qlhbez-RPI?si=g67BgdWa8CAqGzvF)

# Additonal Notes in regards to the assignment and project
There are other chat room implementation using TCP. This protocol has not been implemented as of right now.

The DM works accordingly to send the message to the appropriate receiver's address. However, my implementation shows that it sent the DM to the receiver's address three times.

There can be additonal functions such as storing username and password. This feature has not been implemented.

The chatserver.py instructions was asked to put a port argument. In my implementation, I put a condition that a client should not match with the server's reserved port number, 9999.

There are other files in here that are copies, skeleton code, and redundant. I do not have time to get around it to polish this project and remove the files. Please take this repository with a grain of salt!
