#!/usr/bin/python

from src.core.main import *
import subprocess as subp
import os, sys

def createSymLinks():

	# check for msfconsole in /usr/local/bin
	if not os.path.exists("/usr/local/bin/msfconsole"):
		
		# check for root and error
		if os.getuid() != 0:
			PrintError("Path not found /usr/local/bin/msfconsole")
			PrintError("Run as root (sudo) to create symlinks")
			PGExit()
		
		# if root creat symlinks
		subp.Popen("for msf in $(ls msf*) ; do ln -s $msf /usr/local/bin ; done" % msfpath(), shell=True, stdout=subp.PIPE)
