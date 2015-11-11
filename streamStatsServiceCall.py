# -*- coding: utf-8 -*-
import json
import urllib2
from pprint import pprint
from time import time

"""
Author: Stuart Sheffield (sfs8cq@virginia.edu)
Last modified: November 9, 2015.
"""
t0 = time()

#Project Center
rcode = 'VA'
lon = -78.6
lat = 38.1

t1 = time()

#build the point indexing URL
ssUrl = "http://igskbthivmss201/streamstatsservices/watershed.json?" \
    + "rcode=%s"%(rcode) \
    + "&xlocation=%s"%(lon) \
    + "&ylocation=%s"%(lat) \
    + "&crs=4326" \
    + "&includeparameters=false" \
    + "&includeflowtypes=false" \
    + "&includefeatures=false" \
    + "&simplify=true"

print ssUrl
t2 = time()        
#open the url
data = urllib2.urlopen(ssUrl)

t3 = time()
#read url into string
readData = data.read()

t4 = time()
#load into JSON
response = json.loads(readData) 

t5 = time()
#get relevant info
print response

t6 = time()