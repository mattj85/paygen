#!/usr/bin/python
#
# paygen menus
from src import main
import random

def pl_menu():
	print main.colours.bold + main.colours.green + """Payloads:""" + main.colours.reset + """
[1] windows
[2] php

""" + main.colours.bold + main.colours.green + """Common Exploits:""" + main.colours.reset + """
[3] exploit ms08_067 vulnerability
[4] exploit samba trans2open (linux)
[5] exploit ms12_020 vulnerability (RDP DoS)

""" + main.colours.bold + main.colours.green + """Post exploitation:""" + main.colours.reset + """
[6] launch keimpx
[7] launch sql brute

""" + main.colours.bold + main.colours.green + """Other options:""" + main.colours.reset + """
[l] start MSF listener
[n] nmap scanner
[u] update metasploit

[*] q or x to quit
"""

def win_menu():
	print main.colours.bold + main.colours.green + """Windows MSF payload generator""" + main.colours.reset + """
	
Please make a selection:
	
[1] standard msf payloads
[2] asp embeded payload
[3] shellcode generator
[4] shellcode generator (xor encryption)
[5] backdoored executable
[6] pdf embeded payload

""" +main.colours.bold + main.colours.green + """Powershell:""" + main.colours.reset + """
[7] powershell payload (best)
[8] Reverse / bind shell

[*] Hit ^C to go back
"""

def win_menu1():
	print """Windows MSF """ + main.colours.bold + main.colours.red + """staged""" + main.colours.reset + """ payload generator
	
Please select a payload:

""" + main.colours.bold + main.colours.green + """[+] Using an encoded payload is recommended for AV evasion.
    None encoded payloads are fine for internal testing.""" + main.colours.reset + """
	
[1] meterpreter/reverse_tcp
[2] meterpreter/bind_tcp
[3] shell/reverse_tcp
[4] shell/bind_tcp

[*] Hit ^c to go back
"""

def win_enc_menu():
	print """
Choose encoding type:
	
[1] multi-encoding (default)
[2] no-encoding
"""

# linux payloads currently disabled
def lin_menu():
	print main.colours.bold + main.colours.green + """Linux MSF payload generator""" + main.colours.reset + """
	
Please select a payload:
	
[1] meterpreter/reverse_tcp
[2] meterpreter/bind_tcp
[3] shell/reverse_tcp
[4] shell/bind_tcp

[*] Hit ^C to go back
"""

def php_menu():
	print main.colours.bold + main.colours.green + """PHP MSF payload generator""" + main.colours.reset + """
	
Please select a payload:
	
[1] meterpreter/reverse_tcp (staged)
[2] meterpreter_reverse_tcp
[3] meterpreter/reverse_tcp - base64 encoded (best/default)

[*] Hit ^C to go back
"""

def asp_menu():
	print main.colours.bold + main.colours.green + """ASP MSF payload generator""" + main.colours.reset + """

################################################################################
# THIS ALLOWS YOU TO GENERATE AN ENCODED REVERSE METERPRETER PAYLOAD EMBEDED   #
# IN AN ASP DOCUMENT. TO ACTIVATE THIS PAYLOAD YOU NEED TO OF PREVIOUSLY       #
# COMPROMISED A WINDOWS BASED WEBSERVER. START YOUR MULTI HANDLER, UPLOAD THE  #
# PAYLOAD AND NAVIGATE TO THE ASP PAGE IN YOUR WEB BROWERS. ONCE THE EMBDED    #
# PAYLOAD IS EXECUTED YOU WILL HAVE A SEXY SESSION WAITING FOR YOU.            #
################################################################################
	
Please select a payload: """ + main.colours.bold + main.colours.green + """

[+] This creates an asp payload encoded with shikata_ga_nai """ + main.colours.reset + """
	
[1] meterpreter/reverse_tcp - encoded (default)
[2] x64/meterpreter/reverse_tcp - encoded

[*] Hit ^c to go back
"""

def shellcode_menu():
	print main.colours.bold + main.colours.green + """Metasploit shellcode generator""" + main.colours.reset + """

[1] windows/meterpreter/reverse_tcp
[2] windows/shell/reverse_tcp

[*] Hit ^c to go back
"""

def backdoored_menu1():
	print main.colours.bold + main.colours.green + """Backdoored executeable generator""" + main.colours.reset + """

Choose payload:

[1] windows/meterpreter/reverse_tcp (default)
[2] windows/shell/reverse_tcp

[*] Hit ^c to go back
"""

def backdoored_menu2():
	print """
Choose payload type:

[1] standard MSF executeable
[2] powershell executeable (default)
"""

def pdf_title():
	print main.colours.bold + main.colours.green + """Metasploit payload injection (pdf)""" + main.colours.reset + """

######################################################################
# THIS WILL LAUNCH WINDOWS/FILEFORMAT/ADOBE_PDF_EMBEDDED_EXE EXPLOIT #
# MSF WILL INJECT A PAYLOAD INTO A READABLE PDF FILE.                #
######################################################################
"""

def pdf_menu():
	print main.colours.bold + main.colours.green + """\nPlease pick your payload to use""" + main.colours.reset + """

Choose payload:

[1] windows/meterpreter/reverse_tcp (default)
[2] windows/shell/reverse_tcp
[3] windows/x64/meterpreter/reverse_tcp
[4] windows/x64/shell/reverse_tcp

[*] Hit ^c to go back
"""

def powershell_menu():
	print """
Choose payload:
	
[1] windows/meterpreter/reverse_tcp (default)
[2] windows/64/meterpreter/reverse_tcp
[3] windows/meterpreter/reverse_http
[4] windows/meterpreter/reverse_https
[5] windows/vncinject/reverse_tcp

[*] Hit ^c to go back
"""

def listener_menu():
	print main.colours.bold + main.colours.green + """Create MSF reverse_tcp listener""" + main.colours.reset + """
	
Please select a payload:

[1] windows/x64/meterpreter/reverse_tcp	
[2] windows/meterpreter/reverse_tcp
[3] windows/x64/shell/reverse_tcp
[4] windows/shell/reverse_tcp
[5] php/meterpreter/reverse_tcp
[6] linux/x64/meterpreter/reverse_tcp
[7] linux/x86/shell/reverse_tcp
[8] windows/vncinject/reverse_tcp

[*] Hit ^c to go back
"""

def bind_title():
	print main.colours.bold + main.colours.green + """Multi/Handler bind_tcp setup""" + main.colours.reset + """

#########################################################
# THIS WILL LAUNCH THE METASPLOIT MULTI/HANDLER         #
# BIND_TCP IN A SIMPLE AND EFFICIENT WAY ENJOY!         #  
#########################################################
"""

def bind_menu():
	print main.colours.bold + main.colours.green + """Create MSF Bind TCP Multi/Handler""" + main.colours.reset + """

Please select a payload:
[1] windows/meterpreter/bind_tcp
[2] windows/shell/bind_tcp (best)
[3] linux/x86/meterpreter/bind_tcp
[4] linux/x86/shell/bind_tcp
[5] php/meterpreter/bind_tcp
[6] windows/x64/shell/bind_tcp
[7] windows/x64/meterpreter/bind_tcp

[*] Hit ^c to go back
"""

def ms08_067_title():
	print main.colours.bold + main.colours.green + """Exploit MS08-067 Vulnerability
""" + main.colours.reset + """
##########################################################################
# THIS WILL LAUNCH THE METASPLOIT MS08-067 EXPLOIT AGAINST A SPECIFIED   #
# TARGET AND GIVE YOU A REVERSE SHELL OR METERPRETER SESSION DEPENDING   #
# ON YOUR PAYLOAD SELECTION.                                             #
##########################################################################
"""

def ms08_067_menu():
	print """
Please select a payload:
	
[1] windows/meterpreter/reverse_tcp
[2] windows/shell/reverse_tcp
[3] windows/meterpreter/bind_tcp
[4] windows/shell/bind_tcp

[*] Hit ^c to go back
"""

def samba_title():
	print main.colours.bold + main.colours.green + """Exploit Samba trans2open Vulnerability
""" + main.colours.reset + """
####################################################################
# THIS WILL LAUNCH THE LINUX SAMBA TRANS2OPEN EXPLOIT AGAINST A    #     
# SPECIFIED TARGET RETURNING A BIND OR REVERSE SHELL.              #       
####################################################################
"""

def samba_menu():
	print """
Please select a payload:
	
[1] linux/x86/shell/reverse_tcp (good)  
[2] linux/x86/shell/bind_tcp (best)
[3] linux/x86/meterpreter/reverse_tcp (poor) 
[4] linux/x86/meterpreter/bind_tcp

[*] Hit ^c to go back
"""

def sql_selection():
	print main.colours.bold + main.colours.green + """MySQL & MSSQL Brute""" + main.colours.reset + """

Please select database type:
	
[1] MySQL
[2] MSSQL

[*] Hit ^c to go back
"""

def show_banner():
	banner = random.randrange(1,6)
	if banner == 1:
		print """%s%sv%s - %s%s
 ____              ____            
|  _ \ __ _ _   _ / ___| ___ _ __  
| |_) / _` | | | | |  _ / _ \ '_ \ 
|  __/ (_| | |_| | |_| |  __/ | | |
|_|   \__,_|\__, |\____|\___|_| |_|
            |___/  SQLBrute Edition
""" % (main.colours.bold, main.colours.red, main.details.version, main.details.authors, main.colours.reset)

	if banner == 2:
		print """%s%sv%s - %s%s  
  _____  _______ __   __  ______ _______ __   _
 |_____] |_____|   \_/   |  ____ |______ | \  |
 |       |     |    |    |_____| |______ |  \_|
                               SQLBrute Edition
""" % (main.colours.bold, main.colours.red, main.details.version, main.details.authors, main.colours.reset)

	if banner == 3:
		print """%s%sv%s - %s%s
 ____ ____ ____ ____ ____ ____ 
||P |||a |||y |||G |||e |||n ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
               SQLBrute Edition
""" % (main.colours.bold, main.colours.red, main.details.version, main.details.authors, main.colours.reset)

	if banner == 4:
		print """%s%sv%s - %s%s
   ___              ___           
  / _ \__ _ _   _  / _ \___ _ __  
 / /_)/ _` | | | |/ /_\/ _ \ '_ \ 
/ ___/ (_| | |_| / /_\  __/ | | |
\/    \__,_|\__, \____/\___|_| |_|
            |___/ SQLBrute Edition
""" % (main.colours.bold, main.colours.red, main.details.version, main.details.authors, main.colours.reset)

	if banner == 5:
		print """%s%sv%s - %s%s
 ____   __   _  _  ___  ____  _  _ 
(  _ \ /__\ ( \/ )/ __)( ___)( \( )
 )___//(__)\ \  /( (_-. )__)  )  ( 
(__) (__)(__)(__) \___/(____)(_)\_)
                   SQLBrute Edition
""" % (main.colours.bold, main.colours.red, main.details.version, main.details.authors, main.colours.reset)
