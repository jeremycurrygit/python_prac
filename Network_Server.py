#!/usr/bin/python

import socket

size = 512

host = ''

port = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((host, port))

sock.listen(5)

c, addr = sock.accept()

data = c.recv(size)

if data:
	f = open('/tmp/server.dat', 'w')

	print ('connection received from:', addr[0])

	f.write (':')

	f.write(data.decode('utf-8'))

	f.close()

sock.close()