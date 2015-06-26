# -*- coding: utf-8 -*-

"""
Portscan File

@author Luis Fonte
@date 20150323
"""

import nmap

def portscan():
    """
    Does the portscan to a target IP and and ethernet ports defined by user
    """
    addresses = str(raw_input('IP to scan: '))
    ports = str(raw_input('Ports to scan: '))
    
    scanner = nmap.PortScanner()
    try:
        scanner = nmap.PortScanner()
        scanner.scan(addresses, ports)

        for targetHost in scanner.all_hosts():
            if scanner[targetHost].state() == 'up':
                print targetHost + ' is up \n'
                for targetPort in scanner[targetHost]['tcp']:
                    print 'Port ' + str(targetPort) + '/tcp ' + scanner[targetHost]['tcp'][int(targetPort)]['name'] + ' is ' + scanner[targetHost]['tcp'][int(targetPort)]['state']
                    print ''
                    pass
                pass
            pass            
    except Exception, e:
        print '[-] Something bad happened: ' + str(e)
        pass

    raw_input("...\nPress Enter to continue...")
    pass      
