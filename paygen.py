#!/usr/bin/python
#
# Advanced payload generator
#
# Matt Jones & Jeff Markwart

import os
from src.core import menus
from src.core.main import *
from sys import exit, argv
from time import sleep

# exit PG if not a *nix system
if system_type() != 'posix':
    PrintError("Sorry PayGen is currently for *nix only systems\n")
    exit(1)

# check for msf install
if not os.path.exists(msfpath()):
    try:
        if argv[1] == "--install-msf":
            install_msf()
    except IndexError:
        PrintError("Cannot find metasploit. Please check set your installation path in src/main.py")
        PrintError("To install run: sudo python paygen.py --install-msf\n")
        exit(1)
else:
    while 1:
        # check for $ create output dir
        if not os.path.exists("output/"):
            os.makedirs("output/")

        # banner
        clear()
        menus.show_banner()

        try:
            # display menu and grab user selections
            menus.pl_menu()
            selection = raw_input("%sSelection > %s" % (colours.bold, colours.reset))

            # payloads section
            # windows
            if selection == '1':
                try:
                    reload(src.windows.win_payload_choice)
                except:
                    import src.windows.win_payload_choice

            # php
            elif selection == '3':
                try:
                    reload(src.php.php)
                except:
                    import src.php.php

            # post exploitation
            # launch sql brute
            elif selection == '4':
                try:
                    reload(src.tools.sqlbrute.sqlbrute)
                except:
                    import src.tools.sqlbrute.sqlbrute

            # other options
            # launch msf listener
            elif selection == 'l' or selection == 'L':
                try:
                    reload(src.listener)
                except:
                    import src.listener

            # basic portscan
            elif selection == 'p' or selection == 'P':
                try:
                    reload(src.portscan)
                except:
                    import src.portscan

            # nmap scanner
            elif selection == 'n' or selection == 'N':
                try:
                    reload(src.nmap)
                except:
                    import src.nmap

            # update msf
            elif selection == 'u' or selection == 'U':
                PrintInfo("Updating metasploit. Please wait.")
                update_msf()
                try:
                    libnotify(title="Finished",message="MSF update complete")
                except:
                    pass

                EntContinue()

            # exit paygen
            elif selection == 'Q' or selection == 'q' or selection == 'X' or selection =='x':
                PGExit()

            else:
                PrintError("Please make a selection")
                sleep(2)
                #PGExit()

        except KeyboardInterrupt:
            print "\n"
            PGExit()
