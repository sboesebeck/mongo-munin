def doData():
    ss = getServerStatus()
    m = ss["globalLock"]
    for v in value_generator(m):
       print("globalLock."+v)

def doConfig():

    print "graph_title MongoDB global locks"
    print "graph_args --base 1000 -l 0"
    print "graph_vlabel ops / ${graph_period}"
    print "graph_category MongoDB"
    print "graph_total total"
