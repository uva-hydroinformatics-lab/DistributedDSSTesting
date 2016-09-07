# -*- coding: utf-8 -*-
import json
import urllib2
import time

"""
Author: Stuart Sheffield (sfs8cq@virginia.edu)

xs: ~200 acres
s: ~800 acres
m: ~2500 acres
l: ~25000 acres
xl: ~110,000 acres

"""

wshedDel_xs = ['polygon_xs']
basinChar_xs = ['basinChar_xs']
wshedDel_s = ['polygon_s']
basinChar_s = ['basinChar_s']
wshedDel_m = ['polygon_m']
basinChar_m = ['basinChar_m']
wshedDel_l = ['polygon_l']
basinChar_l = ['basinChar_l']
wshedDel_xl = ['polygon_xl']
basinChar_xl = ['basinChar_xl']

lat = [38.0862, 38.0798, 38.065651, 38.045636, 38.135228]
lon = [-78.5723, -78.5654, -78.479944, -78.45918, -78.394378]

# i = how many times you want to run the same trial
for i in range(1):
    for j in range(len(lat)):
        delineateUrl = "http://streamstatsags.cr.usgs.gov/streamstatsservices/watershed.json?" \
            + "rcode=VA" \
            + "&xlocation=%s" % lon[j] \
            + "&ylocation=%s" % lat[j] \
            + "&crs=4326&includeparameters=false&includeflowtypes=false" \
            + "&includefeatures=true&simplify=true"

        t1 = time.time()

        response1 = urllib2.urlopen(delineateUrl, timeout=10000).read()

        t2 = time.time()

        data1 = json.loads(response1)

        wspace = data1['workspaceID']

        basinUrl = "http://streamstatsags.cr.usgs.gov/streamstatsservices/parameters.json?" \
            + "rcode=VA" \
            + "&workspaceID=%s" % wspace \
            + "&includeparameters=DRNAREA,PRECIP,LC11IMP,MINBELEV,LC11DEV,LC11WATER," \
              "LC11WETLND,LC11FORSHB,LC11CRPHAY,LC11GRASS,LC11BARE"

        response2 = urllib2.urlopen(basinUrl, timeout=10000).read()

        data2 = json.loads(response2)
        t3 = time.time()

        print 'delineate %s ' % len(response1)
        print 'basin char %s ' % len(response2)

        if j == 0:
            wshedDel_xs.append(t2-t1)
            basinChar_xs.append(t3-t2)
        if j == 1:
            wshedDel_s.append(t2-t1)
            basinChar_s.append(t3-t2)
        if j == 2:
            wshedDel_m.append(t2-t1)
            basinChar_m.append(t3-t2)
        if j == 3:
            wshedDel_l.append(t2-t1)
            basinChar_l.append(t3-t2)
        if j == 4:
            wshedDel_xl.append(t2-t1)
            basinChar_xl.append(t3-t2)


for i in range(len(wshedDel_xs)):
    print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' \
       % (wshedDel_xs[i], basinChar_xs[i], wshedDel_s[i], basinChar_s[i], wshedDel_m[i], basinChar_m[i],
          wshedDel_l[i], basinChar_l[i], wshedDel_xl[i], basinChar_xl[i])
