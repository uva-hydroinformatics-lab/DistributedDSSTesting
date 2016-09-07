# -*- coding: utf-8 -*-
import json
import urllib2
import time
"""
Author: Stuart Sheffield (sfs8cq@virginia.edu)
"""
ptIndex = ['ptIndex']
usDs = ['usDs']
navDel = ['navDel']
total = ['total']

# Project Center
lat = 38.0819
lon = -78.473836

# i = how many times you want to run the same trial

for i in range(1):
        t0 = time.time()
        
        # build the point indexing URL
        PtServiceUrl = "http://ofmpub.epa.gov/waters10/PointIndexing.Service?" \
            + "pGeometry=POINT(%s+%s)" % (lon, lat) \
            + "&pGeometryMod=WKT%2CSRID%3D8265" \
            + "&pResolution=3" \
            + "&pPointIndexingMethod=RAINDROP" \
            + "&pPointIndexingMaxDist=2" \
            + "&pOutputPathFlag=FALSE" \
            + "&optOutPrettyPrint=0"

        print PtServiceUrl
          
        # open the url
        url = urllib2.urlopen(PtServiceUrl, timeout=10000).read()
        response = json.loads(url)

        print len(url)
    
        # get relevant info
        comid = response['output']['ary_flowlines'][0]['comid']
        
        t1 = time.time()

        ptIndex.append(t1-t0)

        t2 = time.time()
    
        # build US/DS URL
        UsDsServiceUrl = "http://ofmpub.epa.gov/waters10/UpstreamDownStream.Service?" \
            + "pNavigationType=DM" \
            + "&pStartComid=%s" % comid \
            + "&pStopDistancekm=25" \
            + "&pTraversalSummary=TRUE" \
            + "&pFlowlinelist=TRUE" \
            + "&pEventList=303D" \
            + "&optOutPrettyPrint=0"
                
        # open the url
        url1 = urllib2.urlopen(UsDsServiceUrl, timeout=10000).read()
        response1 = json.loads(url1)

        print len(url1)
        
        t3 = time.time()

        usDs.append(t3-t2)

        t4 = time.time()
    
        # build the navigation delineation URL
        NavDelServiceUrl = "http://ofmpub.epa.gov/waters10/NavigationDelineation.Service?" \
            + "pNavigationType=DM" \
            + "&pStartComID=%s" % comid \
            + "&pMaxDistance=25" \
            + "&pFeatureType=CATCHMENT" \
            + "&pOutputFlag=TRUE"
           
        # open the url
        url2 = urllib2.urlopen(NavDelServiceUrl, timeout=1000).read()
        response2 = json.loads(url2)

        print len(url2)
    
        t5 = time.time()  

        navDel.append(t5-t4)
        total.append(t5-t0)

for i in range(len(ptIndex)):
    print '%s,%s,%s,%s' \
          % (ptIndex[i], usDs[i], navDel[i], total[i])
