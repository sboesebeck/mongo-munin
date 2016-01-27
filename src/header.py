
import urllib2
import sys
import os  
import pymongo

def getServerStatus():
    if 'MONGO_DB_URI' in os.environ:
      c = pymongo.MongoClient(os.environ['MONGO_DB_URI'])
    else:
      c = pymongo.MongoClient()

    return c.admin.command('serverStatus', workingSet=True)

def value_generator(dict):
      for k, v in dict.items():
            if type(v) == type(dict):
                 for id_val in value_generator(v):
                       yield str(k)+"."+id_val
            else:
                 yield str(k).replace(" ","_").replace("/","-").replace("(","_").replace(")","_")+".value "+str(v)

