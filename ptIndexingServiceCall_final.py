# -*- coding: utf-8 -*-
import json
import urllib2
from pprint import pprint
from time import time

"""
Builds a url based on a lat/long and times how long it takes to 
return the output.

Author: Stuart Sheffield (sfs8cq@virginia.edu)
Last modified: November 9, 2015.
"""

for i in range(10):
    
    t0 = time()
    
    #Project Center
    lon = -78.6
    lat = 38.1
    
    t1 = time()
    
    #build the point indexing URL
    PtServiceUrl = "http://ofmpub.epa.gov/waters10/PointIndexing.Service?" \
        + "pGeometry=POINT(%s+%s)"%(lon, lat) \
        + "&pGeometryMod=WKT%2CSRID%3D8265" \
        + "&pResolution=3" \
        + "&pPointIndexingMethod=RAINDROP" \
        + "&pPointIndexingMaxDist=25" \
        + "&pOutputPathFlag=FALSE" \
        + "&optOutPrettyPrint=0"
    
    t2 = time()        
    #open the url
    data = urllib2.urlopen(PtServiceUrl)
    
    t3 = time()
    #read url into string
    readData = data.read()
    
    t4 = time()
    #load into JSON
    response = json.loads(readData) 
    
    t5 = time()
    #get relevant info
    comid = response['output']['ary_flowlines'][0]['comid']
    reachcode = response['output']['ary_flowlines'][0]['reachcode']
    wbdHUC12 = response['output']['ary_flowlines'][0]['wbd_huc12']
    
    t6 = time()
    
    print (t6-t0)