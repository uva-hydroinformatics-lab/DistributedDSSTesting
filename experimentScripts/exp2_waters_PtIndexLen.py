# -*- coding: utf-8 -*-
import json
import urllib2
import time
"""
Author: Stuart Sheffield (sfs8cq@virginia.edu)
"""

ptIndexHalfkm = ['ptIndexHalfkm']
ptIndex1km = ['ptIndex1km']
ptIndex2km = ['ptIndex2km']
ptIndex3km = ['ptIndex3km']
ptIndex4km = ['ptIndex4km']

usDsHalfkm = ['usDsHalfkm']
usDs1km = ['usDs1km']
usDs2km = ['usDs2km']
usDs3km = ['usDs3km']
usDs4km = ['usDs4km']

navDelHalfkm = ['navDelHalfkm']
navDel1km = ['navDel1km']
navDel2km = ['navDel2km']
navDel3km = ['navDel3km']
navDel4km = ['navDel4km']

totalTimeHalfkm = ['totalTimeHalfkm']
totalTime1km = ['totalTime1km']
totalTime2km = ['totalTime2km']
totalTime3km = ['totalTime3km']
totalTime4km = ['totalTime4km']


# Project Center
lat_list = [38.094955, 38.092861, 38.090722, 38.082042, 38.089676]
lon_list = [-78.449287, -78.454319, -78.460392, -78.470678, -78.478274]

# i = how many times you want to run the same trial

for i in range(1):
    for j in range(len(lat_list)):
        
        t0 = time.time()
        
        # build the point indexing URL
        PtServiceUrl = "http://ofmpub.epa.gov/waters10/PointIndexing.Service?" \
            + "pGeometry=POINT(%s+%s)" % (lon_list[j], lat_list[j]) \
            + "&pGeometryMod=WKT%2CSRID%3D8265" \
            + "&pResolution=3" \
            + "&pPointIndexingMethod=RAINDROP" \
            + "&pPointIndexingMaxDist=2" \
            + "&pOutputPathFlag=FALSE" \
            + "&optOutPrettyPrint=0"
          
        # open the url
        url = urllib2.urlopen(PtServiceUrl, timeout=10000).read()
        response = json.loads(url)

        # get relevant info
        comid = response['output']['ary_flowlines'][0]['comid']
        
        t1 = time.time()
        if j == 0:
            ptIndexHalfkm.append(t1-t0)
        if j == 1:
            ptIndex1km.append(t1-t0)
        if j == 2:
            ptIndex2km.append(t1-t0)
        if j == 3:
            ptIndex3km.append(t1-t0)
        if j == 4:
            ptIndex4km.append(t1-t0)
        
        t2 = time.time()
    
        # build the us/ds indexing URL
        UsDsServiceUrl = "http://ofmpub.epa.gov/waters10/UpstreamDownStream.Service?" \
            + "pNavigationType=UM" \
            + "&pStartComid=%s" % comid \
            + "&pStopDistancekm=25" \
            + "&pTraversalSummary=TRUE" \
            + "&pFlowlinelist=TRUE" \
            + "&pEventList=303D" \
            + "&optOutPrettyPrint=0"
                
        # open the url
        url1 = urllib2.urlopen(UsDsServiceUrl, timeout=10000).read()
        response1 = json.loads(url1)

        t3 = time.time()
        
        if j == 0:
            usDsHalfkm.append(t3-t2)
        if j == 1:
            usDs1km.append(t3-t2)
        if j == 2:
            usDs2km.append(t3-t2)
        if j == 3:
            usDs3km.append(t3-t2)
        if j == 4:
            usDs4km.append(t3-t2)
        
        t4 = time.time()
    
        # build the navigation delineation URL
        NavDelServiceUrl = "http://ofmpub.epa.gov/waters10/NavigationDelineation.Service?" \
            + "pNavigationType=UM" \
            + "&pStartComID=%s" % comid \
            + "&pMaxDistance=25" \
            + "&pFeatureType=CATCHMENT" \
            + "&pOutputFlag=TRUE"
           
        # open the url
        url2 = urllib2.urlopen(NavDelServiceUrl, timeout=1000).read()
        response2 = json.loads(url2)
    
        t5 = time.time()  
    
        if j == 0:
            navDelHalfkm.append(t5-t4)
        if j == 1:
            navDel1km.append(t5-t4)
        if j == 2:
            navDel2km.append(t5-t4)
        if j == 3:
            navDel3km.append(t5-t4)
        if j == 4:
            navDel4km.append(t5-t4)
           
        if j == 0:
            totalTimeHalfkm.append(t5-t0)
        if j == 1:
            totalTime1km.append(t5-t0)
        if j == 2:
            totalTime2km.append(t5-t0)
        if j == 3:
            totalTime3km.append(t5-t0)
        if j == 4:
            totalTime4km.append(t5-t0)

for i in range(len(ptIndexHalfkm)):
    print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' \
          % (ptIndexHalfkm[i], ptIndex1km[i], ptIndex2km[i], ptIndex3km[i], ptIndex4km[i], usDsHalfkm[i],
             usDs1km[i], usDs2km[i], usDs3km[i], usDs4km[i], navDelHalfkm[i], navDel1km[i], navDel2km[i],
             navDel3km[i], navDel4km[i], totalTimeHalfkm[i], totalTime1km[i], totalTime2km[i],
             totalTime3km[i], totalTime4km[i])
    

