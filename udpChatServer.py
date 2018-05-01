import socket
import select
import sys
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to address and ip

udpSocket.bind(('', 12345))

print("UDP server up and listening")
clientInfo=[]
while(True):
	inputStream_list = [sys.stdin, udpSocket]
	read_sockets,write_socket, error_socket = select.select(inputStream_list,[],[])
	for socks in read_sockets:
		if socks == udpSocket:
			message = udpSocket.recvfrom(1024)
			print "<received>" + str(message)
			clientInfo = message[1]
			if message[0]== 'bye':
				inputStream_list.remove(udpSocket)
				break
		else:
			buf=raw_input()
			udpSocket.sendto (buf, clientInfo)
			print "<You>" + buf
			if buf== 'bye':
				inputStream_list.remove(udpSocket)
				break
