# -*- coding: utf-8 -*-
import json
import urllib2
import time
import speedtestUpdate

"""
Author: Stuart Sheffield (sfs8cq@virginia.edu)
Last modified: November 9, 2015.
"""
speed = ['speed']
ptIndex = ['ptIndex']
usDs = ['usDs']
navDel = ['navDel']
totalTime = ['total']

print (time.strftime("%c"))
for i in range(100):
    speed.append(speedtestUpdate.speedtest())
    t0 = time.time()
    
    #Project Center
    lat = 38.0819
    lon = -78.473836
    
    #build the point indexing URL
    PtServiceUrl = "http://ofmpub.epa.gov/waters10/PointIndexing.Service?" \
        + "pGeometry=POINT(%s+%s)"%(lon, lat) \
        + "&pGeometryMod=WKT%2CSRID%3D8265" \
        + "&pResolution=3" \
        + "&pPointIndexingMethod=RAINDROP" \
        + "&pPointIndexingMaxDist=25" \
        + "&pOutputPathFlag=FALSE" \
        + "&optOutPrettyPrint=0"
      
    #open the url
    response = json.loads(urllib2.urlopen(PtServiceUrl, timeout=10000).read())

    #get relevant info
    comid = response['output']['ary_flowlines'][0]['comid']
    
    t1 = time.time()
    
    ptIndex.append(t1-t0)
    
    t2 = time.time()

    #build the point indexing URL
    UsDsServiceUrl = "http://ofmpub.epa.gov/waters10/UpstreamDownStream.Service?" \
        + "pNavigationType=DM" \
        + "&pStartComid=%s"%(comid) \
        + "&pStopDistancekm=25" \
        + "&pTraversalSummary=TRUE" \
        + "&pFlowlinelist=TRUE" \
        + "&pEventList=303D" \
        + "&optOutPrettyPrint=0"
            
    #open the url
    response1 = json.loads(urllib2.urlopen(UsDsServiceUrl, timeout=10000).read())
    
    t3 = time.time()
    
    usDs.append(t3-t2)
    
    t4 = time.time()

    #build the point indexing URL
    NavDelServiceUrl = "http://ofmpub.epa.gov/waters10/NavigationDelineation.Service?" \
        + "pNavigationType=DM" \
        + "&pStartComID=%s"%(comid) \
        + "&pMaxDistance=25" \
        + "&pFeatureType=CATCHMENT" \
        + "&pOutputFlag=TRUE"
       
    #open the url
    response2 = json.loads(urllib2.urlopen(NavDelServiceUrl, timeout=1000).read())

    t5 = time.time()  

    navDel.append(t5-t4)
    totalTime.append(t5-t0)

for i in range(len(speed)):
    print '%s,%s,%s,%s,%s'%(speed[i],ptIndex[i],usDs[i],navDel[i],totalTime[i])
    

