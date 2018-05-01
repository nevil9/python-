#!/usr/bin/python           
# This is client.py file


# Import socket module
# Import socket module
import socket     
          
# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         


# Reserve a port for your service.
port = 12345    

# connect with server running on localhost            
s.connect(("127.0.0.1", port)) 

buf = raw_input('Enter a message to send: ')
s.send(buf)
print s.recv(1024)


