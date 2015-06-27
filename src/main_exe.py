# -*- coding: utf-8 -*-

"""
Main File

@author Luis Fonte
@date 20150307
"""

import os
import sys
import csv
import db_userLogin

def do_Portscan():
    """
    Imports file with code to do the portscan
    """
    import portscan
    portscan.portscan()
    pass

def show_ActiveConnections():
    """
    Imports file with code to do check the connnections
    """
    import connections
    connections.presentConnections()
    pass

def do_FirewallLogProcessing():
    """
    Imports file with code to do the firewall loga processing
    """
    import process_firewall_log
    process_firewall_log.showLogs()
    pass

def options_FirewallProcessing():
    """
    Prints some submenu Firewall options and takes the user input to call the method chosen
    """
    option_choice = int(raw_input("\n--Firewall--\n 1 - Show Logs\n 2 - Generate Map \n 3 - Generate CSV \n 4 - Generate Graph \n ... \n 0 - Back \n\n Choose option number: "))
    print '\n'

    firewall_optionChoice = {0 : do_nothing,
                             1 : do_FirewallLogProcessing,
                             2 : generate_MAP,
                             3 : generate_CSV,
                             4 : generate_Graph}
    
    firewall_optionChoice[option_choice]()
    pass

def generate_MAP():
    """
    Imports files with code to generate map with info from firewall logs
    """
    import process_firewall_log
    import generate_maps
    l = process_firewall_log.getLogsLocation()
    info = process_firewall_log.log_map(l)
    generate_maps.createMap(info)
    print "||| Map generated |||"
    pass

def generate_CSV():
    """
    Imports file with code to generate csv with info from firewall logs
    """
    import process_firewall_log
    lo = process_firewall_log.getLogsLocation()
    logfl = csv.writer(open("firewall_logs.csv", "wb"))
    for l in lo:
        logfl.writerow(l)
        pass
    print "||| CSV with logs generated |||"
    pass

def generate_Graph():
    """
    Imports files with code to generate map with info from firewall logs
    Prints some options to show as a graph
    Gets input from user to title and label of the graph

    var num - number of option to graph
    var title - graph title
    var label - graph label
    """
    import process_firewall_log
    import generate_graph
    print "#1 Interface In"
    print "#2 Interface Out"            
    print "#3 Ip origin"
    print "#4 Ip destiny"
    print "#5 Protocol"
    print "#6 Continent"
    print "#7 Country"
    print "#8 City"
    num = raw_input("\nWhich one to generate?(number): ")
    title = raw_input("Graph Title: ")
    label = raw_input("Graph label: ")
    lo = process_firewall_log.getLogsLocation()
    generate_graph.makeGraf(lo, int(num), title, label)
    pass

def options_connections():
    """
    Prints some submenu Connections options and takes the user input to call the method chosen

    var option_choice - integer with value chosen by user
    var connections_optionChoice - array with functions by number
    """
    option_choice = int(raw_input("\n--Connections--\n 1 - Show Active Connections\n 2 - Generate CSV \n 3 - Generate Graph \n ... \n 0 - Back \n\n Choose option number: "))
    print '\n'

    connections_optionChoice = {0 : do_nothing,
                             1 : show_ActiveConnections,
                             2 : generate_connectionsCSV,
                             3 : generate_connectionsGraph}
    
    connections_optionChoice[option_choice]()
    pass

def generate_connectionsCSV():
    """
    Generate csv with connections info

    var con - connection open
    var cfl - opens a csv in write mode to take data
    """
    import connections
    con = connections.getConnections()
    cfl = csv.writer(open("connections.csv", "wb"))
    for c in con:
        cfl.writerow(c)
    print "||| Csv generated |||"
    pass

def generate_connectionsGraph():
    """
    Imports files with code to generate map with info from connections established
    Prints some options to show as a graph
    Gets input from user to title and label of the graph

    var num - number of option to graph
    var title - graph title
    var label - graph label
    var con - gets connections established
    """
    print "#0 Protocol"
    print "#1 Local and User"
    print "#2 Port"
    print "#3 Connection"
    print "#4 Protocol superior layer"
    print "#5 Connection State" 
    num = raw_input("\nWhich one to generate?(number): ")
    title = raw_input("Graph Title: ")
    label = raw_input("Graph label: ")
    import generate_graph
    import connections
    con = connections.getConnections()
    generate_graph.makeGraf(con, int(num), title, label)
    pass

def do_createDB():
    """
    Creates database (only used first time-not available in the program)
    """
    try:
        db_userLogin.database()
    except:
        print "Error"
        pass
    print "Database created successfully."
    raw_input("Click Enter to continue...")
    pass

def do_addUser():
    """
    Adds user to db

    var user - username entered by user
    var passw - password entered by user
    """
    print "-Username to add-"
    user = raw_input("Username: ")
    passw = raw_input("Password: ")
    db_userLogin.user_add(user, passw)
    raw_input("Click Enter to continue...")
    pass

def do_nslookup():
    """
    Do DNS Lookup with IP address given by user

    var address_to_check - stores ip given by user
    var ais - socket function to search dns info
    var ip_list - list with ips found
    """
    import socket #https://docs.python.org/2/library/socket.html
    ip_list = []
    address_to_check = raw_input("Address to check: ")
    ais = socket.getaddrinfo(address_to_check,0,0,0,0)
    for result in ais:
        ip_list.append(result[-1][0])
    ip_list = list(set(ip_list))
    print ip_list
    pass

def do_whois():
    """
    Do Whois search aboout ip address registry

    var ip_to_search - stores ip given by user
    var obj - ip whois function with ip to search
    """
    import ipwhois # from https://pypi.python.org/pypi/ipwhois
    from ipwhois import IPWhois
    import pprint #https://docs.python.org/2/library/pprint.html
    ip_to_search = str(raw_input("IP address to search for: "))
    print "\n"
    obj = IPWhois(ip_to_search)
    try:
        pprint.pprint(obj.lookup_rws())
    except:
        print "\nError."
        raw_input("\nClick Enter to continue...")
        pass
    raw_input("\nClick Enter to continue...")
    pass

def do_reverseLookup():
    """
    Gets hostname by IP address

    var address - ip address to searchS
    """
    import socket
    
    try:
        print "-Reverse Lookup-\n"
        address = raw_input("Enter the Domain name: ")
        print "\n"
        print socket.gethostbyaddr(address)
        print "\n"
        raw_input("\nClick Enter to continue...")
        pass
    except:
        print "\nError."
        raw_input("\nClick Enter to continue...")
        pass
    pass

def do_nothing():
    """
    Used on submenus, just to get back to main
    """
    pass

def do_exitProgram():
    """
    Ends and exits program
    """
    sys.exit(0)
    pass


if __name__ == "__main__":

    ok = True
    while ok:
        user = raw_input("Username: ")
        passw = raw_input("Password: ")
        if db_userLogin.login(user, passw):
            print "\nSucess."
            break
        else:
            print "\nError, try again.\n"
        os.system("clear")

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
                        2 : options_connections,
                        3 : options_FirewallProcessing,
                        4 : do_addUser,
                        5 : do_nslookup,
                        6 : do_whois,
                        7 : do_reverseLookup}

        user_choice = int(raw_input("\n--MENU--\n 1 - Portscan\n 2 - Connections \n 3 - Firewall Log Processing \n 4 - Add user to DB \n 5 - DNS Lookup \n 6 - WhoIS \n 7 - Reverse Lookup \n... \n 0 - Exit Program \n\n Choose option number: "))
        print '\n'

        menu_options[user_choice]()
        pass
    pass

