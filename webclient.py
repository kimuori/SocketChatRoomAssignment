'''
Course: ICS 460-02
Assignment: TCP Web Server
Filename: webclient.py
Date: 9/8/2023

This program is to act as a client side to interact with the webserver.py

@note:
    This program was tested alongside with the program, webserver.py,
    a program that acts as a server waiting for a response from this program.

    As of right now, the webserver has a fixed serverPort value of 6789.
    I have limitations from figuring out how to "send" the client's server port
    to the webserver.

@author:
    Jemina Maasin

'''
from socket import *
import sys  # used for command prompt arguments

'''
    Takes in command inputs based on this argument position:
    webclient.py <server_host> <server_port> <filename>
'''
def cmdArgs(pyName ='', serverName='', serverPort=80, site=''):
    return pyName, serverName, int(serverPort), site

pyName, serverName, serverPort, site = cmdArgs(*sys.argv)


clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = 'GET /' + site + ' HTTP/1.1'
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()
