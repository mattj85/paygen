#!/usr/bin/python
#
# 14/03/2012
# this is a holder page until I get chance to properly integrate keimpx
# into paygen.

import os, sys	
import subprocess
from time import sleep
from src.main import *
from getpass import getpass

while 1:
	try:
		clear()
		
		try:
			import impacket1
		except ImportError:
			PrintError("You need to install Python Impacket library first\n(sudo apt-get install python-impacket)")
			
			EntContinue()
			break

		# get path to keimpx
		def path():
			path = os.getcwd()
			return path

		# display keimpx info
		print """
##########################################################################
# This product includes software developed by CORE Security Technologies #
# (http://www.coresecurity.com), Python Impacket library                 #
#                                                                        #
# keimpx 0.2                                                             #
# by Bernardo Damele A. G. <bernardo.damele@gmail.com>                   #
##########################################################################
"""
		sleep(2)

		# get some target info
		target = raw_input("Enter target IP: ")
		username = raw_input("Enter a username: ")
		password = getpass("Enter a password: ")
		sleep(1)

		# new line
		print "\n"
		# run keimpx
		subprocess.Popen("python %s/src/tools/keimpx/keimpx.py -t %s -U %s -P %s" % (path(), target, username, password), shell=True).wait()

		# return to main
		break
	except KeyboardInterrupt:
		break
