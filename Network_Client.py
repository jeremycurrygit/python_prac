#!/usr/bin/python

import socket

host = 'localhost'

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = (host, 5555)

my_sock.connect(address)

try:

	msg = b'hello! this is a test msg\n'

	my_sock.sendall(msg)

except socket.errno as e:

	print ('Socket error: ', e)

finally:

	my_sock.close()