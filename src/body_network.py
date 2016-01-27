
name = "network"


def doData():
    print name + ".bytesIn.value " + str( getServerStatus()["network"]["bytesIn"] )
    print name + ".bytesOut.value " + str( getServerStatus()["network"]["bytesOut"] )
    print name + ".numRequests.value " + str( getServerStatus()["network"]["numRequests"] )

def doConfig():

    print "graph_title MongoDB current network stats"
    print "graph_args --base 1000 -l 0"
    print "graph_vlabel network"
    print "graph_category MongoDB"

    print name + ".label " + name





