#!/usr/bin/python
#
# nmap scanner
#
## Comments ##
# nmap scanner instead of using python socket server, it's up to you if you want to remove basic port scan option
# I understand with basic port scan it will remain all python, but I find it pointless to use.
# I set this up so I can utilize quick nmap scans to see what services are open.
# You can ultimatly set this up any way you want. this is just a template - jmarkwart

import subprocess as subp
from main import EntContinue, clear
from time import sleep


while 1:
    try:
        clear()
        target = 0
        while target == 0:
            target = raw_input("Please enter the target IP / CIDR range: ") # IP/CIDR range to scan

        # options for nmap
        stealth = "-sS"
        OS = "-O"
        scanOut = subp.Popen(["nmap", "-PN", "-sC", "-T5", "%s", "%s", "%s"] % (target, stealth, OS), stdout=subp.PIPE)
        for lines in scanOut.stdout:
            print "[+]", lines

        sleep(1)
        EntContinue()

        # back to main
        break
    except KeyboardInterrupt:
        break
