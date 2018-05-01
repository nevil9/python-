import socket

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to address and ip

udpSocket.bind(('', 12345))

print("UDP server up and listening")

while(True):
	message = udpSocket.recvfrom(1024)
	print "received message from client:" + str (message)
	# message [0] is the message content and message[1] is address of sender

	clientMessage = message[0]
	clientAddress = message[1]

	if clientMessage == 'bye':
		continue
	# Sending a reply to client
	buf=raw_input ("Enter a message for client:")
	udpSocket.sendto(buf, clientAddress)
