#!/usr/bin/python

#compress and decompress a string

import zlib

s = 'hello Bob ! hello Smith ! hello Jacob ! \n'

t = zlib.compress(s)

print 'Compress text is = ' , t

print 'Decompressed text is = ', zlib.decompress(t)