#!/usr/bin/python
#

import os
from src import main			
from src import menus

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
					reload(src.platforms.windows)
				except: 
					import src.platforms.windows

			elif pltype == '2':
				try: 
					reload(src.platforms.asp)
				except: 
					import src.platforms.asp
		
			elif pltype == '3':
				try: 
					reload(src.platforms.windows_shellcode)
				except: 
					import src.platforms.windows_shellcode
		
			elif pltype == '4':
				try: 
					reload(src.platforms.windows_shelltoxor)
				except: 
					import src.platforms.windows_shelltoxor

			elif pltype == '5':
				try: 
					reload(src.platforms.backdoored_exe)
				except: 
					import src.platforms.backdoored_exe
					
			elif pltype == '6':
				try: 
					reload(src.platforms.pdfbackdoor)
				except: 
					import src.platforms.pdfbackdoor
					
			# arduino based payloads
			elif pltype == '7':
				try: 
					reload(src.platforms.powershell)
				except: 
					import src.platforms.powershell

			# return to main
			break
		
	except KeyboardInterrupt:
		break
