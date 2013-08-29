#!/usr/bin/python
#

import os
from src.core.main import *	
from src.core import menus

while 1:
	try:
		pltype = 0
		while pltype != range(1,7):
			clear()
			menus.linux_menu()
			pltype = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))

			# windows
			if pltype == '1':
				try: 
					reload(src.linux.msf)
				except: 
					import src.linux.msf

			elif pltype == '2':
				try: 
					reload(src.linux.standard)
				except: 
					import src.linux.standard
		
			elif pltype == '3':
				try: 
					reload(src.linux.shellcode)
				except: 
					import src.linux.shellcode

			# return to main
			break
		
	except KeyboardInterrupt:
		break
