# Chat Room Socket Programming
This program was a part of my college course assignment to implement a UDP protocol in a chat room.

## About UDP Chat Room Socket
2 programs must run together: `chatserver.py` and `chatclient.py`.
This program was tested using a Linux machine and terminal to run the program.

First, run the `chatserver.py` in the terminal. There is no need to put port number.
On the Command Line, type `python chatserver.py`. This will start the program to start listening for clients.
* NOTE: Interpreter may vary (e.g. 'py', 'python2', 'python3', etc. ) so type the first part according to your machine.

Second, run the `chatclient.py`. There are specific instructions to type the arguemnt.
On the Command Line, the instructions follows: `python chatclient.py [IP address] [port num =/= 9999] [username]`. 
If this format is incorrectly formatted, it will end the program.
* NOTE: The chatserver.py currently reserves port number 9999. 
* NOTE: It is best to type the IP Address such as `127.0.0.1`, for example.
* EXAMPLE OF THE CMD LINE: `python chatclient 127.0.0.1 7890 iLoveHunting123`

You can create multiple instances of `chatclient.py` as long as the client instance does not occupy
the port number already reserved by another client!

<u>Information of the Command Lines ('PM', 'DM', 'EX'):</u>
* For the client to exit the chat room, type "EX" or "ex". This will disconnect the client from the server.
* PM (Public Message) allows clients to broadcast their messages to other clients. 
The client can simply choose to type any message without declaring 'PM'. 
The server will still treat that message as PM by default.
* DM (Direct Message) is a private message between client and another client. The client will be asked to type
the username of the client they want to interact with.

<u>Additional Notes and Reflections:</u>
The DM works accordingly to send the message to the appropriate receiver's address. However
my implementation shows that it sent the DM to the receiver's address three times.

This program currently does not implement the login and password feature and saving 
credentials to a file.

The chatserver.py instructions was asked to put a port argument. In my implementation, I
put a condition that a client should not match with the server's reserved port number, 9999.

This assignment was referenced from this video for UDP skeleton reference: https://youtu.be/3qlhbez-RPI?si=g67BgdWa8CAqGzvF


# Additonal Notes
There are other chat room implementation using TCP. This protocol has not been implemented as of right now.

There can be additonal functions such as storing username and password. This feature has not been implemented.

There are other files in here that are copies, skepeton code, and redundant. I do not have time to get around it to polish this project and remove the files. Please take this repository with a grain of salt!
