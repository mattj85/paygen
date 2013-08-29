#!/usr/bin/python
#

import os
from src.core import main			
from src.core import menus

while 1:
	try:
		pltype = 0
		while pltype != range(1,6):
			main.clear()
			menus.win_menu()
			pltype = raw_input(" %sSelection > %s" % (main.colours.bold, main.colours.reset))

			# windows
			if pltype == '1':
				try: 
					reload(src.windows.win_std)
				except: 
					import src.windows.win_std

			elif pltype == '2':
				try: 
					reload(src.web.asp.asp)
				except: 
					import src.web.asp.asp
		
			elif pltype == '3':
				try: 
					reload(src.windows.shellcode)
				except: 
					import src.windows.shellcode
		
			elif pltype == '4':
				try: 
					reload(src.windows.xor2exe)
				except: 
					import src.windows.xor2exe

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
					reload(src.ps.psbatfile)
				except: 
					import src.ps.psbatfile

			# return to main
			break
		
	except KeyboardInterrupt:
		break
