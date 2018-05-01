import socket
import select
import sys
from thread import *

def clientthread(conn, addr):
	# sends a message to the client whose user object is conn
	conn.send("Welcome to this chatroom!")
 
	while True:
		try:
			message = conn.recv(2048)
			if message:
				"""prints the message and address of the
				user who just sent the message on the server
				terminal"""
				print "<" + addr[0] + "> " + message
 
				# Calls broadcast function to send message to all
				message_to_send = "<" + addr[0] + "> " + message
				broadcast(message_to_send, conn)
			else:
				"""message may have no content if the connection
				is broken, in this case we remove the connection"""
				remove(conn)
		        except:
				continue
 
"""Using the below function, we broadcast the message to all
clients who's object is not the same as the one sending
the message """
def broadcast(message, connection):
for conn in list_of_conns:
	if conn!=connection
		try:
			conn.send(message)
		except:
			conn.close()
 			# if the link is broken, we remove the client
			remove(conn)
 
"""The following function simply removes the object
from the list that was created at the beginning of 
the program"""
def remove(connection):
	if connection in list_of_conns:
		list_of_conns.remove(connection)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Port = 12345
"""
binds the server to specified port number.
The client must be aware of these parameters
"""
server.bind(('', Port))
 
"""
listens for 100 active connections. This number can be
increased as per convenience.
"""
server.listen(100)
 
list_of_conns = []

while True:
 
	"""Accepts a connection request and stores two parameters, 
	conn which is a socket object for that user, and addr 
	which contains the IP address of the client that just 
	connected"""
	conn, addr = server.accept()
 
	"""Maintains a list of clients for ease of broadcasting
	a message to all available people in the chatroom"""
	list_of_conns.append(conn)
 
	# prints the address of the user that just connected
	print str(addr) + " connected"
 
	# creates and individual thread for every user 
	# that connects
	start_new_thread(clientthread,(conn,addr))    
 
	conn.close()
server.close()

