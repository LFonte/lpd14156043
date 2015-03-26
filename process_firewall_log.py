# -*- coding:utf-8 -*-


#https://pypi.python.org/pypi/pygeoip/
#https://wiki.ubuntu.com/UncomplicatedFirewall
#python-ufw 0.34
#https://github.com/maxmind/geoip-api-python
#https://github.com/maxmind/geoip-api-python/blob/master/README.rst
#http://www.pip-installer.org/en/latest/installing.html#install-or-upgrade-pip

"""
Firewall log processing File

@author Luis Fonte
@date 20150325
"""


LOG_FILE = "ufw.log"


def showLogs():
    """
    Show logs on console
    Gets logs formatted and adds header
    """
    logsLocation = getLogsLocation()
    print "DATE\tIN_LOG\tOUT_LOG\tSRC_IP\tDST_IP\tPROTO\tPORT\tCONTINET\tCOUNTRY\tTOWN"
    for log in logsLocation: #text format
        print str(log[0])+"\t"+str(log[1])+"\t"+str(log[2])+"\t"+str(log[3])+"\t"+str(log[4])+"\t"+str(log[5])+"\t"+str(log[6])+"\t"+str(log[7])+"\t"+str(log[8])+"\t"+str(log[9])
        pass
    raw_input("Press Enter to continue...")
    pass

def getLogsLocation():
    """
    Adds geoloction to each log row

    @logs_final - Returns logs array complete and with geo location
    """
    import pygeoip
    GI = pygeoip.GeoIP("GeoIP.dat", pygeoip.MEMORY_CACHE) #connections with geoip file
    logs = getLogs() #calls method that extrat logs from firewall file
    logs_final = [] #array to store the logs
    for log in logs:
            try:
                info = GI.record_by_addr(log[3])
                logs_final.append([log[0],log[1],log[2],log[3],log[4],log[5],log[6],info["continent"],info["country_name"],info["city"],info["longitude"],info["latitude"]])             
            except:
                pass
    return logs_final
    pass
        
def getLogs():
    """
    Reads log file from firewall 

    @logsArray - Returns array with logs from file
    """
    logFile_open = open(LOG_FILE, "r") #log file from uncomplicated firewall
    logsProcess = [] #Array to store logs separated by spaces
    for line in logFile_open:
        logsProcess.append(line.split(" ")) #append with split done
    logsArray = [] #array to store file logs
    for log in logsProcess:
        date_log = log[0]+log[1]+log[2]
        for x in log:
            if x.startswith("IN="):
                in_log = x.strip("IN=")
            elif x.startswith("OUT="):
                out_log = x.strip("OUT=")
            elif x.startswith("SRC="):
                src_log = x.strip("SRC=")
            elif x.startswith("DST="):
                dst_log = x.strip("DST=")
            elif x.startswith("PROTO="):
                proto_log = x[6:]
            elif x.startswith("SPT="):
                port_log = x[4:]
        
        logsArray.append([date_log,in_log,out_log,src_log,dst_log,proto_log,port_log])#append all data formated

    return logsArray
    pass

