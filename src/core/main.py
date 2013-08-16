#!/usr/bin/python
#
# paygen main functions

import subprocess as subp
import os, socket, re, random, string
from time import sleep
from sys import exit, platform

# details
class details:
	authors = "Matt Jones & Jeff Markwart"
	version = "3.1.1"
	codename = "Cyberdelia"

# define some colours
class colours:
	bold = '\033[1m'
	red = '\033[31m'
	green = '\033[32m'
	cyan = '\033[36m'
	reset = '\033[0;0m'

# paygen currently only for *nix systems
def system_type():
	return os.name
	
def clear():
	subp.call(["clear"])
	
def EntContinue():
	raw_input("\n Press %sENTER%s to continue" % (colours.bold, colours.reset))
	
def PrintInfo(message):
	print colours.bold + colours.green + "\n [+] %s" % message + colours.reset
	
def PrintInfo2(info, message):
	print colours.bold + colours.green + " [+] %s: " % info + colours.cyan + "%s" % message + colours.reset
	
def PrintError(message):
	print colours.bold + colours.red + "\n [!] %s" % message + colours.reset

def PrintError2(info, message):
	print colours.bold + colours.red + " [!] %s: " % info + colours.cyan + "%s" % message + colours.reset
	
def PrintFailed(message):
	print " [-] %s" % message

def msfpath():
	with open('config/paygen_config') as config:
		for line in config:
			msfmatch = re.match("MSFPATH", line)
			if msfmatch:
				msfpath = re.sub("\"", "", line)
				msfpath = re.sub("MSFPATH=", "", msfpath)
				return msfpath.rstrip()
	
def install_msf():
	if platform != 'darwin':
		
		# check apt-get is installed
		if os.path.exists('/usr/bin/apt-get'):
			PrintInfo("Debian based OS detected")
			sleep(1)
			
			# check for git
			if not os.path.exists("/usr/bin/git"):
				install_git = raw_input(PrintInfo("Git not installed. Install now? (Y/N): "))
				if install_git == 'Y' or install_git == 'y':
					PrintInfo("Installing git\n")
					subp.Popen("sudo apt-get install git", shell=True).wait()
				else:
					PGExit()
			else:
				PrintInfo("Git is installed. Continuing")
						
		# pull metasploit
		PrintInfo("Grabbing Metasploit")
		tools_path = os.getenv('HOME')+"/tools"
		subp.Popen("git clone https://github.com/rapid7/metasploit-framework.git %s/msf" % tools_path, shell=True).wait()

	else:
		PrintError("Auto MSF install is not supported on this platform")
		PGExit()

# update metasploit
def update_msf():
	proc = subp.Popen('ruby %s/msfupdate' % msfpath(), shell=True, stdout=subp.PIPE)
	output = proc.stdout.readlines()
	for line in output:
		print " [+] %s" % line.rstrip()
		
# grab ip of adapter. 
def iface_ip():	
	if platform == 'linux2':
		iface = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		iface.connect(('google.com', 0))
		iface.settimeout(2)
		iface = iface.getsockname()[0]
	else:
		iface = raw_input(" \n[+] Enter IP: ")
		while is_valid_ipv4(iface) == False:
			PrintError("Invalid IP!")
			iface = raw_input(" \n[+] Enter IP: ")
			if is_valid_ipv4(iface) == True:
				break
		
	return iface
				
def default_lport():
	with open("config/paygen_config") as config:
		for line in config:
			match = re.match("DEFAULT_LPORT=", line)
			if match:
				lport = re.sub("\"", lport)
				lport = re.sub("DEFAULT_LPORT=", lport)
				return lport.rstrip()

# standard paygen exit
def PGExit():
	PrintInfo("Exiting Paygen\n")
	exit()
	
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

def getPID():
	return os.getpid()
	
def generate_random_string(low, high):
    length = random.randint(low, high)
    letters = string.ascii_letters+string.digits
    return ''.join([random.choice(letters) for _ in range(length)])
