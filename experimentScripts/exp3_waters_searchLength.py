# -*- coding: utf-8 -*-
import json
import urllib2
import time
"""
Author: Stuart Sheffield (sfs8cq@virginia.edu)
"""
ptIndex1 = ['ptIndex1']
ptIndex5 = ['ptIndex5']
ptIndex10 = ['ptIndex10']
ptIndex25 = ['ptIndex25']
ptIndex50 = ['ptIndex50']

usDs1 = ['usDs1']
usDs5 = ['usDs5']
usDs10 = ['usDs10']
usDs25 = ['usDs25']
usDs50 = ['usDs50']

totalTime1 = ['totalTime1']
totalTime5 = ['totalTime5']
totalTime10 = ['totalTime10']
totalTime25 = ['totalTime25']
totalTime50 = ['totalTime50']

searchLength = [1, 5, 10, 25, 50]

# i = how many times you want to run the same trial
for i in range(1):
    for j in range(len(searchLength)):
        t0 = time.time()

        # Project Center
        lat = 38.0819
        lon = -78.473836

        # build the point indexing URL
        PtServiceUrl = "http://ofmpub.epa.gov/waters10/PointIndexing.Service?" \
            + "pGeometry=POINT(%s+%s)" % (lon, lat) \
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

        # build the US/DS indexing URL
        UsDsServiceUrl = "http://ofmpub.epa.gov/waters10/UpstreamDownStream.Service?" \
            + "pNavigationType=DM" \
            + "&pStartComid=%s" % comid \
            + "&pStopDistancekm=%s" % (searchLength[j]) \
            + "&pTraversalSummary=TRUE" \
            + "&pFlowlinelist=TRUE" \
            + "&pEventList=303D" \
            + "&optOutPrettyPrint=0"

        # open the url
        url1 = urllib2.urlopen(UsDsServiceUrl, timeout=10000).read()
        response1 = json.loads(url1)

        t2 = time.time()

        if j == 0:
            ptIndex1.append(t1-t0)
            usDs1.append(t2-t1)
            totalTime1.append(t2-t0)

        if j == 1:
            ptIndex5.append(t1-t0)
            usDs5.append(t2-t1)
            totalTime5.append(t2-t0)

        if j == 2:
            ptIndex10.append(t1-t0)
            usDs10.append(t2-t1)
            totalTime10.append(t2-t0)

        if j == 3:
            ptIndex25.append(t1-t0)
            usDs25.append(t2-t1)
            totalTime25.append(t2-t0)

        if j == 4:
            ptIndex50.append(t1-t0)
            usDs50.append(t2-t1)
            totalTime50.append(t2-t0)

for i in range(len(ptIndex1)):
    print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' \
          % (ptIndex1[i], ptIndex5[i], ptIndex10[i], ptIndex25[i], ptIndex50[i],
             usDs1[i], usDs5[i], usDs10[i], usDs25[i], usDs50[i],
             totalTime1[i], totalTime5[i], totalTime10[i], totalTime25[i], totalTime50[i])
