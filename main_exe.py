#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Main File

@author Luis Fonte
@date 20150307
"""

import sys


def do_Portscan():
    import portscan
    portscan.portscan()
    pass

def show_ActiveConnections():
    print 'Active Connections'
    pass

def do_FirewallLogProcessing():
    print 'Firewall log processing'
    pass

def do_exitProgram():
    sys.exit(0)
    pass

if __name__ == "__main__":

    app_stat = True
    

    while app_stat:
        print '\n---------------------------------------------------'
        print '---------- Network Security Application -----------'
        print '---------------------------------------------------'
        print '--------------- Author: Luis Fonte ----------------'
        print '----------------- LPD MESI IPBEJA -----------------'
        print '---------------------------------------------------'
        
        menu_options = {0 : do_exitProgram,
                        1 : do_Portscan,
                        2 : show_ActiveConnections,
                        3 : do_FirewallLogProcessing}

        

        user_choice = int(raw_input("\n--MENU--\n 1 - Portscan\n 2 - Show Active Connections \n 3 - Firewall Log Processing \n ... \n 0 - Exit Program \n\n Choose option number: "))
        print '\n'

        menu_options[user_choice]()
        pass
    pass





    
