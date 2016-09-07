import urllib
import time
import xml.etree.ElementTree as ET

__author__ = 'Mohamed Morsy'

# Study area Box (decimal WGS 1984)
northlimit = [38.0768999916]
eastlimit = [-78.4468410457]
southlimit = [38.0736828558]
westlimit = [-78.4530307805]

poly_sm = ['poly_sm']
soils_sm = ['soils_sm']

# i = how many times you want to run the same trial

for i in range(1):

        # Build the soil data request URL
        polygonAreaUrl = "http://SDMDataAccess.sc.egov.usda.gov/Spatial/SDMWGS84Geographic.wfs?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature" \
                         + "&TYPENAME=MapunitPoly&FILTER=<Filter><BBOX><PropertyName>Geometry</PropertyName><Box srsName='EPSG:4326'>" \
                         + "<coordinates>%s,%s,%s,%s</coordinates>"%(westlimit[j], southlimit[j], eastlimit[j], northlimit[j]) \
                         + "</Box></BBOX></Filter>&SRSNAME=EPSG:4326&OUTPUTFORMAT=GML2"

        soilDataRequestUrl = "http://SDMDataAccess.sc.egov.usda.gov/Spatial/SDMWGS84Geographic.wfs?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature" \
                         + "&TYPENAME=mapunitpolyextended&FILTER=<Filter><BBOX><PropertyName>Geometry</PropertyName><Box srsName='EPSG:4326'>" \
                         + "<coordinates>%s,%s,%s,%s</coordinates>"%(westlimit[j], southlimit[j], eastlimit[j], northlimit[j]) \
                         + "</Box></BBOX></Filter>&SRSNAME=EPSG:4326&OUTPUTFORMAT=GML2"

        # Open the url
        t0 = time.time()
        polyData = urllib.urlopen(polygonAreaUrl)
        t1 = time.time()
        data = urllib.urlopen(soilDataRequestUrl)
        readPolyData = polyData.read()
        readData = data.read()
        t2 = time.time()
        root = ET.fromstring(readData)

        print len(readPolyData)
        print len(readData)

        poly_sm.append(t1-t0)
        soils_sm.append(t2-t1)

for k in range(len(poly_sm)):
    print '%s,%s' % (poly_sm[k], soils_sm[k])
