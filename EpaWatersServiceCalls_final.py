# -*- coding: utf-8 -*-
import json
import urllib2
from pprint import pprint
import time

"""
Author: Stuart Sheffield (sfs8cq@virginia.edu)
Last modified: November 9, 2015.
"""
print (time.strftime("%c"))

for i in range(10):
    print "Run %s"%(i+1)
    
    t0 = time.time()
    
    #Project Center
    lon = -78.6
    lat = 38.1
    
    t1 = time.time()
    
    #build the point indexing URL
    PtServiceUrl = "http://ofmpub.epa.gov/waters10/PointIndexing.Service?" \
        + "pGeometry=POINT(%s+%s)"%(lon, lat) \
        + "&pGeometryMod=WKT%2CSRID%3D8265" \
        + "&pResolution=3" \
        + "&pPointIndexingMethod=RAINDROP" \
        + "&pPointIndexingMaxDist=25" \
        + "&pOutputPathFlag=FALSE" \
        + "&optOutPrettyPrint=0"
    
    t2 = time.time()        
    #open the url
    data = urllib2.urlopen(PtServiceUrl)
    
    t3 = time.time()
    #read url into string
    readData = data.read()
    
    t4 = time.time()
    #load into JSON
    response = json.loads(readData) 
    
    t5 = time.time()
    #get relevant info
    comid = response['output']['ary_flowlines'][0]['comid']
    reachcode = response['output']['ary_flowlines'][0]['reachcode']
    wbdHUC12 = response['output']['ary_flowlines'][0]['wbd_huc12']
    
    t6 = time.time()
    
    print (t6-t0)
    
    t7 = time.time()

    #build the point indexing URL
    UsDsServiceUrl = "http://ofmpub.epa.gov/waters10/UpstreamDownStream.Service?" \
        + "pNavigationType=DM" \
        + "&pStartComid=%s"%(comid) \
        + "&pStopDistancekm=25" \
        + "&pTraversalSummary=TRUE" \
        + "&pFlowlinelist=TRUE" \
        + "&pEventList=303D" \
        + "&optOutPrettyPrint=0"
    
    t8 = time.time()        
    #open the url
    data = urllib2.urlopen(UsDsServiceUrl)
    
    t9 = time.time()
    #read url into string
    readData = data.read()
    
    t10 = time.time()
    #load into JSON
    response = json.loads(readData) 
    
    t11 =time. time()
    
    print t11-t7
    t12 = time.time()

    #build the point indexing URL
    NavDelServiceUrl = "http://ofmpub.epa.gov/waters10/NavigationDelineation.Service?" \
        + "pNavigationType=DM" \
        + "&pStartComID=%s"%(comid) \
        + "&pMaxDistance=25" \
        + "&pFeatureType=CATCHMENT" \
        + "&pOutputFlag=TRUE"
    
    t13 = time.time()        
    #open the url
    data = urllib2.urlopen(NavDelServiceUrl)
    
    t14 = time.time()
    #read url into string
    readData = data.read()
    
    t15 = time.time()
    #load into JSON
    response = json.loads(readData) 
    
    t16 = time.time()
    
    print t16-t12
    print t16-t0
print time.strftime("%c")
