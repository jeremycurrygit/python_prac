#!/usr/bin/python

#steganography

import stepic, Image

i = Image.open('/tmp/torbuntu.png')

i.show()

steg = stepic.encode(i, 'Hello Bob! How are you doing?')

steg.save('/tmp/steg.jpg', 'JPEG')

i1= Image.open('/tmp/steg.jpg')

i1.show()