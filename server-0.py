#!/usr/bin/python           
# This is server.py file

# Import socket module
import socket               


# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         

# Reserve a port for your service.
port = 12345   

# Bind to the port, permit connections from any node in network             
s.bind(('', port))    


# Now wait for client connection.
s.listen(5)   
              
while True:
	# Establish connection with client.
	c, addr = s.accept()     	

	print 'Got connection from', addr
	c.send('Thank you for connecting\n')
	
	# Close the connection
	c.close()                

