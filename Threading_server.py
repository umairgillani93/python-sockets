"""
Server file using Threading
created by: UG_PYTHON

"""


import socket
from time import time

host = '0.0.0.0'
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
print('listeing on host: {} | port: {} '.format(host,port))

def handle_client(client_socket):

    request = client_socket.recv(1024)

    server_str = client_socket.send(str.encode('ACK!'))

    client_response_str = client.socket(recv(1024)).decode('utf-8')
    print(client_response_str)

    client_socket.close()


while True:

    client, address = s.accept()

    print('connection established.. \nhost: {} | port: {} '.format(address[0], str(address[1])))

    client_handler = threading.Thread(handle_client,client)
    client_handler.start()
