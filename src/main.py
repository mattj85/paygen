#!/usr/bin/python
#
# paygen config file

import os, socket, subprocess
from sys import exit, platform

class details:
	authors = "Matt Jones & Jeff Markwart"
	version = "3.0"

# get system type
# paygen currently only for *nix systems
def system_type():
	return os.name
	
def clear():
	subprocess.Popen("clear", shell=True).wait()
	
def EntContinue():
	raw_input("\nPress %sENTER%s to continue" % (colours.bold, colours.reset))
	
def PrintInfo(message):
	print colours.bold + colours.green + "\n[+] %s" % message + colours.reset
	
def PrintError(message):
	print colours.bold + colours.red + "\n[!] %s" % message + colours.reset
	
def PrintFailed(message):
	print "[-] %s" % message

# define some colours
class colours:
	bold = '\033[1m'
	red = '\033[31m'
	green = '\033[32m'
	reset = '\033[0;0m'
		
# define path to msf installation
def msfpath():
	# uncomment the following section for static msf path
	# msfpath = ''

	# little fix to save re-editing after every check in/out
	if os.getenv('HOME') != '/root':
		msfpath = '%s/tools/msf' % os.getenv('HOME')
	else:
		# for backtrack
		msfpath = '/opt/metasploit/msf3'
	
	# return path
	return msfpath
	
# define local ip for mult handler
# you can leave this as 0.0.0.0 if you wish
def localip():
	localip = '0.0.0.0'
	return localip

# grab ip of adapter. 
# ripped from SET. Thanks Dave!
def iface_ip():
	if platform != 'darwin':
		iface = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		iface.connect(('google.com', 0))
		iface.settimeout(2)
		iface = iface.getsockname()[0]
		return iface
	else:
		iface = raw_input("\n[+] Enter IP: ")
		return iface

# update metasploit
def update_msf():
	subprocess.Popen('svn up %s' % msfpath(), shell=True).wait()
	
# standard paygen exit
def PGExit():
	print "%s%s\nExiting PayGen....\n%s" % (colours.bold, colours.red, colours.reset)
	exit(1)
	
def default_wordlist():
	wordlist = os.getcwd() + "/src/wordlist/wordlist.txt"
	return wordlist
