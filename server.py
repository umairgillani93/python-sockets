"""
SERVER FILE:
    - Create socket
    - Bind the socket
    - Listen for the connection from client
    - Accept the connection and create call send_commands() function for converstion between server and client
    - Define send_commands()
    - Create main() and call all the functions in main()

"""

import socket
import sys


def create_socket():

    try:

        global host
        global port
        global s

        host = ''
        port = 9999

        s = socket.socket()

    except socket.error as error:
        print('Socket creation error: ' + str(error))

def bind_socket():

    try:

        global host
        global port
        global s


        s.bind((host,port))
        print('Binding the port: ' + str(port) + '\n' + 'Listening for the connection..')
        s.listen(5)

    except socket.error as error:
        print('Socket binding error:' + '\n' + 'Retrying..')
        bind_socket()


def socket_accept():

    conn, address = s.accept()
    print('Connection has been established: ' + 'IP Address: ' + address[0] + ' | port: ' + str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):

    while True:

        cmd = input()

        if cmd == 'quit':
            conn.close()
            s.clsoe()
            sys.exit()

        if len(str.encode(cmd)) > 0:     ## if something is being written in server's console
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')  ## receive client's response and convert in standart string (utf-80)
            print(client_response, end = '')


def main():

    create_socket()
    bind_socket()
    socket_accept()

if __name__ == '__main__':
    main()
