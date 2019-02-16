"""
client program, using Threading in Python
created by: UG_PYTHON

"""

import socket
from time import time

host = '192.168.1.2'
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))

server_response = s.recv(1024)


server_str = server_response.decode('utf-8')

client_response = s.send(str.encode('Hi server! Thanks for accepting my request'))

print(server_str)
