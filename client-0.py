# Import socket module
import socket


# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get IP of name
host = socket.gethostbyname('www.google.com')

# port for getting service.
port = 80


s.connect((host, port))
print("socket connected to google http server")

