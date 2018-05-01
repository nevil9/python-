#!/usr/bin/python           
# This is client.py file

import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
# Create a socket object

#host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect(("127.0.0.1", port))
While True:
	buf = raw_input('Enter a message to send: ')
	s.send(buf)
	if buf == 'bye':
		break
	msg= s.recv(1024)
	print 'received ' + msg
	if msg == 'bye':
		break

