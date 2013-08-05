#!/usr/bin/python

import subprocess as subp

def updatePG():
	print "[+] Updating Paygen. Please wait..."
	subp.call(["git","pull"])

if __name__ == '__main__':
	updatePG()
