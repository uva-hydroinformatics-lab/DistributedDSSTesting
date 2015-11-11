# -*- coding: utf-8 -*-
import json
import urllib2
from pprint import pprint
from time import time

"""
Builds a url based on a comid and times how long it takes to return info
from that url.

Author: Stuart Sheffield (sfs8cq@virginia.edu)
Last modified: November 9, 2015.
"""

for i in range(10):
    t0 = time()
    
    #comid
    comid = 8566737
    
    t1 = time()

    #build the point indexing URL
    NavDelServiceUrl = "http://ofmpub.epa.gov/waters10/NavigationDelineation.Service?" \
        + "pNavigationType=DM" \
        + "&pStartComID=%s"%(comid) \
        + "&pMaxDistance=25" \
        + "&pFeatureType=CATCHMENT" \
        + "&pOutputFlag=TRUE"
    
    t2 = time()        
    #open the url
    data = urllib2.urlopen(NavDelServiceUrl)
    
    t3 = time()
    #read url into string
    readData = data.read()
    
    t4 = time()
    #load into JSON
    response = json.loads(readData) 
    
    t5 = time()
    
    print t5-t0

