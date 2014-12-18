#!/usr/bin/python

import os, time

root_dir = '/'

for current_directory, dir, files in os.walk(root_dir):
	
	for f in files:
		print ('%s %s' %(current_directory, f))