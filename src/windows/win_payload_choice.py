#!/usr/bin/python
#

import os
from src.core import main			
from src.core import menus

while 1:
	try:
		pltype = 0
		while pltype != range(1,5):
			main.clear()
			menus.win_menu()
			pltype = raw_input("%sSelection > %s" % (main.colours.bold, main.colours.reset))

			# windows
			if pltype == '1':
				try: 
					reload(src.windows.windows)
				except: 
					import src.windows.windows

			elif pltype == '2':
				try: 
					reload(src.windows.asp)
				except: 
					import src.windows.asp
		
			elif pltype == '3':
				try: 
					reload(src.windows.windows_shellcode)
				except: 
					import src.windows.windows_shellcode
		
			elif pltype == '4':
				try: 
					reload(src.windows.windows_shelltoxor)
				except: 
					import src.windows.windows_shelltoxor

			elif pltype == '5':
				try: 
					reload(src.misc.backdoored_exe)
				except: 
					import src.misc.backdoored_exe
					
			elif pltype == '6':
				try: 
					reload(src.misc.pdfbackdoor)
				except: 
					import src.misc.pdfbackdoor
					
			# powershell based payloads
			elif pltype == '7':
				try: 
					reload(src.powershell.powershell)
				except: 
					import src.powershell.powershell

			# return to main
			break
		
	except KeyboardInterrupt:
		break
