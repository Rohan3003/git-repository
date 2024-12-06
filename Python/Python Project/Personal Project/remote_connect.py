# code to connect to a laptop using python

import socket
import sys

HOST = '
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as err:
    print('Bind failed. Error Code : ' .format(err))

s.listen(10)
print('Socket now listening')

conn, addr = s.accept()
print('Connected with ' + addr[0] + ':' + str(addr[1]))

data = conn.recv(1024)
conn.sendall(data)

conn.close()
s.close()

// q: what is a socket?
// a: a socket is an endpoint of a two-way communication link between two programs running on the network. 
// A socket is bound to a port number so that the TCP layer can identify the application that data is destined to be sent to. 
// An endpoint is a combination of an IP address and a port number. Every TCP connection can be uniquely identified by its two endpoints. That way you can have multiple connections between your host and the server.
// q: what is a port?
// q: what is a host?
// q: what is a socket.error?
// q: what is a socket.AF_INET?
// a: 