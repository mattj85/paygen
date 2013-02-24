#!/usr/bin/python
#
# paygen config file

import os, socket, subprocess, re
from time import sleep
from sys import exit, platform

class details:
	authors = "Matt Jones & Jeff Markwart"
	version = "3.0.1"

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
	
def install_msf():
	if platform == 'linux2':
		
		# check apt-get is installed
		if os.path.exists('/usr/bin/apt-get'):
			PrintInfo("Debian based OS detected")
			sleep(1)
			
			# check for git
			if not os.path.exists("/usr/bin/git"):
				install_git = raw_input(PrintInfo("Git not installed. Install now? (Y/N): "))
				if install_git == 'Y' or install_git == 'y':
					PrintInfo("Installing git\n")
					subprocess.Popen("sudo apt-get install git", shell=True).wait()
				else:
					PGExit()
			else:
				PrintInfo("Git is installed. Continuing")
						
		# pull metasploit
		PrintInfo("Grabbing Metasploit")
		tools_path = os.getenv('HOME')+"/tools"
		subprocess.Popen("git clone https://github.com/rapid7/metasploit-framework.git %s/msf" % tools_path, shell=True).wait()

	else:
		PrintError("Auto MSF install is not supported on this platform")
		PGExit()

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
		while is_valid_ipv4(iface) == False:
			PrintError("Invalid IP!")
			iface = raw_input("\n[+] Enter IP: ")
			if is_valid_ipv4(iface) == True:
				return iface

# update metasploit
def update_msf():
	subprocess.Popen('ruby %s/msfupdate' % msfpath(), shell=True).wait()
	
# standard paygen exit
def PGExit():
	print "%s%s\nExiting PayGen....\n%s" % (colours.bold, colours.red, colours.reset)
	exit(1)
	
def default_wordlist():
	wordlist = os.getcwd() + "/src/wordlist/wordlist.txt"
	return wordlist

def is_valid_ipv4(ip):
    pattern = re.compile(r"""
        ^
        (?:
          # Dotted variants:
          (?:
            # Decimal 1-255 (no leading 0's)
            [3-9]\d?|2(?:5[0-5]|[0-4]?\d)?|1\d{0,2}
          |
            0x0*[0-9a-f]{1,2}  # Hexadecimal 0x0 - 0xFF (possible leading 0's)
          |
            0+[1-3]?[0-7]{0,2} # Octal 0 - 0377 (possible leading 0's)
          )
          (?:                  # Repeat 0-3 times, separated by a dot
            \.
            (?:
              [3-9]\d?|2(?:5[0-5]|[0-4]?\d)?|1\d{0,2}
            |
              0x0*[0-9a-f]{1,2}
            |
              0+[1-3]?[0-7]{0,2}
            )
          ){0,3}
        |
          0x0*[0-9a-f]{1,8}    # Hexadecimal notation, 0x0 - 0xffffffff
        |
          0+[0-3]?[0-7]{0,10}  # Octal notation, 0 - 037777777777
        |
          # Decimal notation, 1-4294967295:
          429496729[0-5]|42949672[0-8]\d|4294967[01]\d\d|429496[0-6]\d{3}|
          42949[0-5]\d{4}|4294[0-8]\d{5}|429[0-3]\d{6}|42[0-8]\d{7}|
          4[01]\d{8}|[1-3]\d{0,9}|[4-9]\d{0,8}
        )
        $
    """, re.VERBOSE | re.IGNORECASE)
    return pattern.match(ip) is not None
