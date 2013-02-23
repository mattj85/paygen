#!/usr/bin/python
#
# Advanced payload generator for metasploit framework
#
# Matt Jones & Jeff Markwart

import os
from src import menus
from src.main import *
from sys import exit
from time import sleep

# check msf path is valid
if not os.path.isdir(msfpath()):
	PrintError("Cannot find metasploit. Please check set your installation path in src/main.py")
	PrintError("To install run: sudo python paygen.py --install-msf\n")
	exit(1)

# exit PG if not a *nix system
if system_type() != 'posix':
	PrintError("Sorry PayGen is currently for *nix only systems\n")
	exit(1)
else:
	while 1:
		# banner
		clear()
		menus.show_banner()
		install_msf()

		try:
			# display menu and grab user selections
			menus.pl_menu()
			selection = raw_input("%sSelection > %s" % (colours.bold, colours.reset))
								
			# payloads section
			# windows
			if selection == '1':
				try: 
					reload(src.platforms.win_payload_choice)
				except: 
					import src.platforms.win_payload_choice
		
			# php
			elif selection == '2':
				try: 
					reload(src.platforms.php)
				except: 
					import src.platforms.php
				
			# exploit section
			# ms08_067
			elif selection == '3':
				try: 
					reload(src.exploits.ms08067.ms08067)
				except: 
					import src.exploits.ms08067.ms08067

			# exploit section 
			# samba trans2open
			elif selection == '4':
				try:
					reload(src.exploits.samba.samba)
				except:
					import src.exploits.samba.samba

			# check ms12_020 vuln
			elif selection == '5':
				try:
					reload(src.exploits.ms12020.ms12020)
				except:
					import src.exploits.ms12020.ms12020
							
			# post exploitation
			# launch keimpx
			elif selection == '6':
				try: 
					reload(src.tools.keimpx.getinfo)
				except: 
					import src.tools.keimpx.getinfo
					
			# launch sql brute
			elif selection == '7':
				try: 
					reload(src.tools.sqlbrute.sqlbrute)
				except: 
					import src.tools.sqlbrute.sqlbrute
		
			# other options
			# launch msf listener
			elif selection == 'l' or selection == 'L':
				try: 
					reload(src.listener)
				except: 
					import src.listener
		
			# basic portscan
			elif selection == 'p' or selection == 'P':
				try: 
					reload(src.portscan)
				except: 
					import src.portscan
			
			# nmap scanner
			elif selection == 'n' or selection == 'N':
				try:
					reload(src.nmap)
				except:
					import src.nmap

			# update msf
			elif selection == 'u' or selection == 'U':
				PrintInfo("Updating metasploit. Please wait.")
				update_msf()
				try:
					libnotify(title="Finished",message="MSF update complete")
				except:
					pass
				
				EntContinue()
		
			# exit paygen
			elif selection == 'Q' or selection == 'q' or selection == 'X' or selection =='x':
				PGExit()
		
			else:
				PrintError("Please make a selection")
				sleep(3)					
				#PGExit()
	
		except KeyboardInterrupt:
			print "\n"
			PGExit()
