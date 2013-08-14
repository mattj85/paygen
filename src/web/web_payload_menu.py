#!/usr/bin/python
#

import os
from src.core import main			
from src.core import menus

while 1:
	try:
		pltype = 0
		while pltype != range(1,2):
			main.clear()
			menus.web_menu()
			pltype = raw_input(" %sSelection > %s" % (main.colours.bold, main.colours.reset))

			# windows
			if pltype == '1':
				try: 
					reload(src.web.php.php)
				except: 
					import src.web.php.php

			elif pltype == '2':
				try: 
					reload(src.web.asp.asp)
				except: 
					import src.web.asp.asp

			# return to main
			break
		
	except KeyboardInterrupt:
		break
