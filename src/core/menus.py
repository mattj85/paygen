#!/usr/bin/python
#
# paygen menus

from src.core import main
import random

def pl_menu():
	print main.colours.bold + main.colours.green + """ Metasploit Payloads:""" + main.colours.reset + """
 [1] windows
 [2] linux / osx
 [3] web
 [4] java
 [5] teensy

""" + main.colours.bold + main.colours.green + """ Modules:""" + main.colours.reset + """
 [6] sqlbrute
 [7] psexec powershell injector

""" + main.colours.bold + main.colours.green + """ Other options:""" + main.colours.reset + """
 [l] start MSF listener
 [u] update metasploit

 [*] q or x to quit
"""

def win_menu():
	print main.colours.bold + main.colours.green + """ MSF Windows Payloads""" + main.colours.reset + """
	
 Please make a selection:
	
 [1] standard msf payloads
 [2] asp embeded payload
 [3] shellcode generator
 [4] xor obfuscated executable
 [5] backdoored executable
 [6] pdf embeded payload

""" +main.colours.bold + main.colours.green + """ Powershell Based""" + main.colours.reset + """
 
 [7] powershell payload (best)

 [*] Hit ^C to go back
"""

def win_menu1():
	print """ Windows """ + main.colours.bold + main.colours.red + """staged""" + main.colours.reset + """ payload generator
	
 Please select a payload:

""" + main.colours.bold + main.colours.green + """ [+] Using an encoded payload is recommended for AV evasion.
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

def arch_menu():
	print """
 Choose architecture:
	
 [1] 32bit (default)
 [2] 64bit
"""

def web_menu():
	print main.colours.bold + main.colours.green + """ MSF Web Payloads""" + main.colours.reset + """
	
 Please make a selection:
	
 [1] php embeded payload
 [2] asp embeded payload

 [*] Hit ^C to go back
"""

def linux_menu():
	print main.colours.bold + main.colours.green + """ Linux Payloads""" + main.colours.reset + """
	
 Please make a selection:
	
 [1] metasploit payloads
 [2] standard payloads
 [3] generate shellcode

 [*] Hit ^C to go back
"""

def linux_msf_menu():
	print main.colours.bold + main.colours.green + """ Linux MSF Payloads""" + main.colours.reset + """
	
 Please make a selection:
	
 [1] linux/x86/meterpreter/reverse_tcp
 [2] linux/x86/meterpreter/bind_tcp
 [3] linux/x86/shell/reverse_tcp
 [4] linux/x86/shell/bind_tcp

 [*] Hit ^C to go back
"""

def php_menu():
	print main.colours.bold + main.colours.green + """ MSF PHP Payloads""" + main.colours.reset + """
	
 Please select a payload:
	
 [1] meterpreter/reverse_tcp (staged)
 [2] meterpreter_reverse_tcp
 [3] meterpreter/reverse_tcp - base64 encoded (best/default)

 [*] Hit ^C to go back
"""

def asp_menu():
	print main.colours.bold + main.colours.green + """ ASP MSF payload generator""" + main.colours.reset + """
	
 Please select a payload:

 [1] meterpreter/reverse_tcp - encoded (default)
 [2] x64/meterpreter/reverse_tcp - encoded

 [*] Hit ^c to go back
"""

def shellcode32_menu():
	print main.colours.bold + main.colours.green + """ Metasploit shellcode generator""" + main.colours.reset + """

 [1] windows/meterpreter/reverse_tcp
 [2] windows/shell/reverse_tcp

 [*] Hit ^c to go back
"""

def shellcode64_menu():
	print main.colours.bold + main.colours.green + """ Metasploit shellcode generator""" + main.colours.reset + """

 [1] windows/x64/meterpreter/bind_tcp
 [2] windows/x64/meterpreter/reverse_https
 [3] windows/x64/meterpreter/reverse_tcp
 [4] windows/x64/shell/bind_tcp
 [5] windows/x64/shell/reverse_https
 [6] windows/x64/shell/reverse_tcp
 [7] windows/x64/shell_bind_tcp
 [8] windows/x64/shell_reverse_tcp
 [9] windows/x64/vncinject/bind_tcp
 [10] windows/x64/vncinject/reverse_https
 [11] windows/x64/vncinject/reverse_tcp

 [*] Hit ^c to go back
"""

def backdoored_menu1():
	print main.colours.bold + main.colours.green + """ Backdoored executeable generator""" + main.colours.reset + """

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
	print main.colours.bold + main.colours.green + """ Metasploit payload injection (pdf)""" + main.colours.reset + """

 ######################################################################
 # THIS WILL LAUNCH WINDOWS/FILEFORMAT/ADOBE_PDF_EMBEDDED_EXE EXPLOIT #
 # MSF WILL INJECT A PAYLOAD INTO A READABLE PDF FILE.                #
 ######################################################################
"""

def pdf_menu():
	print main.colours.bold + main.colours.green + """\n Please pick your payload to use""" + main.colours.reset + """

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
 [2] windows/x64/meterpreter/reverse_tcp
 [3] windows/meterpreter/reverse_http
 [4] windows/meterpreter/reverse_https
 [5] windows/vncinject/reverse_tcp

 [*] Hit ^c to go back
"""

def psexec_menu():
	print main.colours.bold + main.colours.green + """ PsExec Powershell injector""" + main.colours.reset + """

 Choose payload:
	
 [1] windows/meterpreter/reverse_tcp
 [2] windows/meterpreter/reverse_https (default)

 [*] Hit ^c to go back
""" 

def ps_moduleInfo():
	print main.colours.bold + main.colours.cyan + \
""" #################################################################
 # The payload requires the target to have powershell installed. #
 #################################################################
 """ + main.colours.reset

def listener_menu():
	print main.colours.bold + main.colours.green + """ Create MSF reverse_tcp listener""" + main.colours.reset + """
	
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
	print main.colours.bold + main.colours.green + """ Multi/Handler bind_tcp setup""" + main.colours.reset + """

 #########################################################
 # THIS WILL LAUNCH THE METASPLOIT MULTI/HANDLER         #
 # BIND_TCP IN A SIMPLE AND EFFICIENT WAY ENJOY!         #  
 #########################################################
"""

def bind_menu():
	print main.colours.bold + main.colours.green + """ Create MSF Bind TCP Multi/Handler""" + main.colours.reset + """

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

def sql_selection():
	print main.colours.bold + main.colours.green + """ MySQL & MSSQL Brute""" + main.colours.reset + """

 Please select database type:
	
 [1] MySQL
 [2] MSSQL

 [*] Hit ^c to go back
"""

def show_banner():
		print """ %s%s
 Version:  %s%s
 %sCodename: %s%s
 %sAuthors:  %s%s%s
    ___              ___           
   / _ \__ _ _   _  / _ \___ _ __  
  / /_)/ _` | | | |/ /_\/ _ \ '_ \ 
 / ___/ (_| | |_| / /_\  __/ | | |
 \/    \__,_|\__, \____/\___|_| |_|
             |___/
""" % (main.colours.bold, main.colours.red, main.colours.cyan, main.details.version, \
main.colours.red, main.colours.cyan, main.details.codename, main.colours.red, main.colours.cyan, \
main.details.authors, main.colours.reset)
