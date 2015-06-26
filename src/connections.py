#!/usr/bin/python
# -*- coding: utf-8 -*-

#https://docs.python.org/3.3/library/os.html#os.system

"""
Connections File

@author Luis Fonte
@date 20150323
"""

import os

def presentConnections():
    """
    Presents connections on console
    Lines and collums structured
    """
    con = getConnections() #calls the method that 
    print "PROTOCOL\tLOCALUSER\tPORT\tCONNECTION\tPROTO\tSTATE"
    for x in con: #structures data in lines and cols
        if len(x[3]) <= 15:
            print x[0]+"\t\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+x[4]+"\t"+x[5]
            pass
        else:
            print x[0]+"\t\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+x[4]+"\t"+x[5]
            pass
        pass
    
    raw_input("Press Enter to continue...")
    pass


def getConnections():
    """
    Returns array with connections
    Calls a method that "asks" to system for connections established
    Adds the top row with titles to the connection data

    @connections_array - returns array with logs
    """
    con = processConnections()
    connections_array = []
    for x in con:
        c = []
        treatcon = x[0].split(" ")
        treatcon = filter(lambda x: x != "", treatcon)
        c.append(treatcon[0])#PROTOCOL
        a = treatcon[3].split(":")
        c.append(a[0])#LOCALUSER
        c.append(a[1])#PORT
        a = treatcon[4].split(":")
        c.append(a[0])#CONNECTION
        c.append(a[1])#PROTO
        c.append(treatcon[5].strip("\n"))
        connections_array.append(c)
        pass
    return connections_array


def processConnections():
    """
    Calls system with os.system for connections
    Stores data in file and the in array
    
    @connections_array - returns the connections data
    """
    os.system("netstat -t -u > connections.txt")
    connections_array = []
    fl = open("connections.txt", "r")
    while 1:
        line = fl.readline()
        if not line:
            break
        connections_array.append([line])
    connections_array.pop(0) #remove first two lines from array
    connections_array.pop(0)
    return connections_array

