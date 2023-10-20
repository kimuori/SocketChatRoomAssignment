## UDP Chat Room

2 programs must run together: `chatserver.py` and `chatclient.py`.

First, run the `chatserver.py` first. There is no need to put port number.
On the Command Line, type `python chatserver.py`. This will start the program to start listening for clients.
* NOTE: Interpreter may vary (e.g. 'py', 'python2', 'python3', etc. ) so type the first part according to your machine.

Second, run the `chatclient.py`. There are specific instructions to type the arguemnt.
On the Command Line, the instructions follows: `python chatclient.py [IP address] [port num =/= 9999] [username]`. 
If this format is incorrectly formatted, it will end the program.
* NOTE: The chatserver.py currently reserves port number 9999. 
* NOTE: It is best to type the IP Address such as `127.0.0.1`.
* EXAMPLE OF THE CMD LINE: `python chatclient 127.0.0.1 7890 Jemina`

You can create multiple instances of `chatclient.py` as long as the client instance does not occupy
the port number already reserved by another client.

For the client to exit the chat room, type "EX" or "ex".

As of right now, this program has not implemented the public and private messaging...