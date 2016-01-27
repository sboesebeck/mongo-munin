def doData():
    ss = getServerStatus()
    wt = ss["wiredTiger"]
    for v in value_generator(wt):
       print("wiredTiger."+v)

def doConfig():

    print "graph_title MongoDB metrix for wired tiger"
    print "graph_args --base 1000 -l 0"
    print "graph_vlabel ops / ${graph_period}"
    print "graph_category MongoDB"
    print "graph_total total"
