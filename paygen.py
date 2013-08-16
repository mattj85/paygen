#!/usr/bin/python
#
# Advanced payload generator

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
        # check for & create output dir
        if not os.path.exists("output/"):
            os.makedirs("output/")

        # banner
        clear()
        menus.show_banner()

        try:
            # display menu and grab user selections
            menus.pl_menu()
            selection = raw_input(" %sSelection > %s" % (colours.bold, colours.reset))

            # payloads section
            # windows
            if selection == '1':
                try:
                    reload(src.windows.win_payload_menu)
                except:
                    import src.windows.win_payload_menu

			# *nix
            elif selection == '2':
                try:
                    reload(src.linux.linux_msf)
                except:
                    import src.linux.linux_msf

            # php
            elif selection == '3':
                try:
                    reload(src.web.web_payload_menu)
                except:
                    import src.web.web_payload_menu

            elif selection == '4':
                try:
					reload(src.java.java)
                except:
                    import src.java.java

            elif selection == '5':
                try:
					reload(src.teensy.teensy)
                except:
                    import src.teensy.teensy

            # post exploitation
            # launch sql brute
            elif selection == '6':
                try:
                    reload(src.modules.sql.sqlbrute)
                except:
                    import src.modules.sql.sqlbrute

            # other options
            # launch msf listener
            elif selection == 'l' or selection == 'L':
                try:
                    reload(src.misc.listener)
                except:
                    import src.misc.listener

            # update msf
            elif selection == 'u' or selection == 'U':
                PrintInfo("Updating metasploit. Please wait.")
                update_msf()
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
