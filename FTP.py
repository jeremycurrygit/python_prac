#!/usr/bin/python

import ftplib

host = raw_input ('Please enter the host you want to connect : ')

f = ftplib.FTP (host)

try:

	f.login = ('username', 'password')

	print (f.getwelcome())

	print (f.dir())

	f.delete ('file1')

	print (f.dir())

	f.set_pasv(1)

	f.storbinary('STOR file2', open('file2', 'rb'))

	print (f.dir())

except Exception as e:

	print ('Exception : ', e)

finally:

	f.close()