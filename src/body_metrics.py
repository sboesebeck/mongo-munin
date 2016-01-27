def doData():
    ss = getServerStatus()
    m = ss["metrics"]
    for v in value_generator(m):
       print("metrics.metrics."+v)

def doConfig():

    print "graph_title MongoDB metrics"
    print "graph_args --base 1000 -l 0"
    print "graph_vlabel ops / ${graph_period}"
    print "graph_category MongoDB"
    print "graph_total total"
