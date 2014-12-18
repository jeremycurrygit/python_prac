#! /usr/bin/python

# Android Data Extractor Python Script

# Authors: Sahil Sharma

# An automated python script which extracts data from android phone.

#Date: Nov., 10, 2012

import csv
import sys
import sqlite3
import os
import logging

class AndroidExtractor():


#SMS Fetching Function


	def process_sms(self, imagefilepath, destfolderpath):
		logger.debug("Entered Fucntion Process SMS")

		imagefilepath = imagefilepath.rstrip('/')

		destfolderpath = destfolderpath.rstrip('/')

		dbfilepath = imagefilepath + "/data/data/com.android.providers.telephony/databases/mmssms.db"
		
		if os.path.exists(dbfilepath):

			if not os.path.lexists(destfolderpath):
		
				os.mkdir(destfolderpath)
				logger.info("Output Folder Created")
			
			# open database connection.(check return value after every db value)
			db = sqlite3.connect(dbfilepath)

			# prepare a cursor object using cursor() method.
			cursor = db.cursor()

			# preparing a sql query to read data from database.
			sql = "select address as PhoneNumber , datetime(date/1000,'unixepoch','localtime') as Localtime , body as Body  from sms"

			try:
				# execute sql query using execute() method.
				cursor.execute(sql)

				# fetch a single row using fetchone() method.
				data = cursor.fetchall()
		
				#Writing ouput to CSV File
				csv_writer = csv.writer(open(destfolderpath + "/sms.csv", "wt"))
		
				# write headers
				csv_writer.writerow([i[0] for i in cursor.description])
			
				csv_writer.writerows(data)

				# this will close the CSV file
				del csv_writer

			except sqlite3.OperationalError, err:
				logger.error( "Error: " + err)
		
			#disconnect from database
			db.close()

		else:
			logger.error("Cannnot Process SMS because " + dbfilepath + " not found ")
			
		

#Call Log Fetching Function

	def process_call(self, imagefilepath, destfolderpath):
		logger.debug("Entered Function Process CALLS")		
		
		imagefilepath = imagefilepath.rstrip('/')

		destfolderpath = destfolderpath.rstrip('/')

		dbfilepath = imagefilepath + "/data/data/com.android.providers.contacts/databases/contacts2.db"
		
	
		if os.path.exists(dbfilepath):
		
			if not os.path.lexists(destfolderpath):
		
				os.mkdir(destfolderpath)
			
			
			# open database connection.(check return value after every db value)
			db = sqlite3.connect(dbfilepath)

			# prepare a cursor object using cursor() method.
			cursor = db.cursor()

			# preparing a sql query to read data from database.
			sql = "select formatted_number as PhoneNumber , datetime(date/1000,'unixepoch','localtime') as LocalTime , duration as CallDuration ,  name as Name from calls"

			try:
				# execute sql query using execute() method.
				cursor.execute(sql)

				# fetch a single row using fetchone() method.
				data = cursor.fetchall()
			
				#Writing ouput to CSV File
				csv_writer = csv.writer(open(destfolderpath + "/calls.csv", "wt"))
			
				# write headers
				csv_writer.writerow([i[0] for i in cursor.description])
				
				csv_writer.writerows(data)

				# this will close the CSV file
				del csv_writer

			except sqlite3.OperationalError, err:
				logger.error( "Error: %s ", err)
		
			#disconnect from database
			db.close()
		else:
			logger.error("Cannnot Process CALLS LOG because " + dbfilepath + " not found ")


# Contacts Fetching Function

	def process_contacts(self, imagefilepath, destfolderpath):
		logger.debug("Entered Function Process CONTACTS")		

		imagefilepath = imagefilepath.rstrip('/')

		destfolderpath = destfolderpath.rstrip('/')

		dbfilepath = imagefilepath + "/data/data/com.android.providers.contacts/databases/contacts2.db"


		if os.path.exists(dbfilepath):

			if not os.path.lexists(destfolderpath):
		
				os.mkdir(destfolderpath)
			
			
			# open database connection.(check return value after every db value)
			db = sqlite3.connect(dbfilepath)

			# prepare a cursor object using cursor() method.
			cursor = db.cursor()

			# preparing a sql query to read data from database.
			sql = "select data1 as Contact from data"

			try:
				# execute sql query using execute() method.
				cursor.execute(sql)

				# fetch a single row using fetchone() method.
				data = cursor.fetchall()
		
				#Writing ouput to CSV File
				csv_writer = csv.writer(open(destfolderpath + "/contacts.csv", "wt"))
		
				# write headers
				csv_writer.writerow([i[0] for i in cursor.description])
			
				csv_writer.writerows(data)

				# this will close the CSV file
				del csv_writer

			except sqlite3.OperationalError, err:
				logger.error( "Error: %s ", err)
		
			#disconnect from database
			db.close()
		
		else:
			logger.error("Cannnot Process CONTACTS because " + dbfilepath + " not found ")


#Browser History Function

	def process_browser(self, imagefilepath, destfolderpath):
		logger.debug("Entered Function Process BROWSER")		

		imagefilepath = imagefilepath.rstrip('/')

		destfolderpath = destfolderpath.rstrip('/')

		dbfilepath = imagefilepath + "/data/data/com.android.browser/databases/browser2.db"


		if os.path.exists(dbfilepath):
	
			if not os.path.lexists(destfolderpath):
		
				os.mkdir(destfolderpath)
			
			
			# open database connection.(check return value after every db value)
			db = sqlite3.connect(dbfilepath)

			# prepare a cursor object using cursor() method.
			cursor = db.cursor()

			# preparing a sql query to read data from database.
			sql = "select title as Name , url as Link , datetime(date/1000,'unixepoch','localtime') as LocalTime , visits as Visits from history"

			try:
				# execute sql query using execute() method.
				cursor.execute(sql)

				# fetch a single row using fetchone() method.
				data = cursor.fetchall()
		
				#Writing ouput to CSV File
				csv_writer = csv.writer(open(destfolderpath + "/browser_history.csv", "wt"))
		
				# write headers
				csv_writer.writerow([i[0] for i in cursor.description])
			
				csv_writer.writerows(data)

				# this will close the CSV file
				del csv_writer

			except sqlite3.OperationalError, err:
				logger.error( "Error: %s ", err)
		
			#disconnect from database
			db.close()
		
		else:
			logger.error("Cannnot Process BROWSER because " + dbfilepath + " not found ")



#GPS Function

	
	def process_gps(self, imagefilepath, destfolderpath):
		logger.debug("Entered Function Process GPS")		

		imagefilepath = imagefilepath.rstrip('/')

		destfolderpath = destfolderpath.rstrip('/')

		dbfilepath = imagefilepath + "/data/data/com.google.android.apps.maps/databases/search_history.db"
		
		if os.path.exists(dbfilepath):

			if not os.path.lexists(destfolderpath):
		
				os.mkdir(destfolderpath)
			
			
			# open database connection.(check return value after every db value)
			db = sqlite3.connect(dbfilepath)

			# prepare a cursor object using cursor() method.
			cursor = db.cursor()

			# preparing a sql query to read data from database.
			sql = "select data1 as Name , displayQuery as SearchedPlace , latitude as Latitude , longitude as Longitude from suggestions"

			try:
				# execute sql query using execute() method.
				cursor.execute(sql)

				# fetch a single row using fetchone() method.
				data = cursor.fetchall()
		
				#Writing ouput to CSV File
				csv_writer = csv.writer(open(destfolderpath + "/gps_history.csv", "wt"))
		
				# write headers
				csv_writer.writerow([i[0] for i in cursor.description])
			
				csv_writer.writerows(data)

				# this will close the CSV file
				del csv_writer

			except sqlite3.OperationalError, err:
				logger.error( "Error: %s ", err)
		
			#disconnect from database
			db.close()
	
		else:
			logger.error("Cannnot Process GPS because " + dbfilepath + " not found ")



if __name__ == "__main__":
    msg = AndroidExtractor()
    calls = AndroidExtractor()
    contacts = AndroidExtractor()
    browser = AndroidExtractor()
    gps = AndroidExtractor()    
    logger = logging.getLogger('test')
    hdlr = logging.FileHandler('/tmp/android_error.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.DEBUG)
    if (len(sys.argv) == 3):
         msg.process_sms(sys.argv[1], sys.argv[2])
	 calls.process_call(sys.argv[1], sys.argv[2])
	 contacts.process_contacts(sys.argv[1], sys.argv[2])
	 browser.process_browser(sys.argv[1], sys.argv[2])
 	 gps.process_gps(sys.argv[1], sys.argv[2])
    else:
        logger.error("not enough Parameters")
        print "Not Enough Parameters"
