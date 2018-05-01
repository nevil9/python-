# Python program to implement client side of chat room.
import socket
import select
import sys
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
IP_address = '127.0.0.1'
Port = 12345
s.connect((IP_address, Port))
 
while True:
	# maintains a list of possible input streams
	inputStream_list = [sys.stdin, s]
	""" There are two possible input situations. Either the
	user wants to give  manual input to send to other people,
	or the server is sending a message  to be printed on the
	screen. Select returns from sockets_list, the stream that
	is reader for input. So for example, if the server wants
	to send a message, then the if condition will hold true
	below.If the user wants to send a message, the else
	condition will evaluate as true"""
	read_sockets,write_socket, error_socket = select.select(inputStream_list,[],[])
 
	for socks in read_sockets:
		if socks == s:
			message = socks.recv(2048)
			print "<received>" + message
		else:
			message = raw_input()
			s.send(message)
			print "<You>" + message
			if message == 'bye'
				s.close()
				inputStream_list.remove(s)
				break
	if s not in inputStream_list:
		break
s.close()
