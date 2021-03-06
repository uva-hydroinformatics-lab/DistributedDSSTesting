__author__ = 'Mohamed Morsy'
import json, xmltodict
import urllib
from time import time
import xml.etree.ElementTree as ET
import xml.etree as etree

import pprint

# Study area Box (decimal WGS 1984)
northlimit = 38.076876
eastlimit = -78.412355
southlimit = 37.990639
westlimit = -78.540778

#Build the soil data request URL
polygonAreaUrl = "http://SDMDataAccess.sc.egov.usda.gov/Spatial/SDMWGS84Geographic.wfs?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature" \
                     + "&TYPENAME=MapunitPoly&FILTER=<Filter><BBOX><PropertyName>Geometry</PropertyName><Box srsName='EPSG:4326'>" \
                     + "<coordinates>%s,%s,%s,%s</coordinates>"%(westlimit, southlimit, eastlimit, northlimit) \
                     + "</Box></BBOX></Filter>&SRSNAME=EPSG:4326&OUTPUTFORMAT=GML2"

soilDataRequestUrl = "http://SDMDataAccess.sc.egov.usda.gov/Spatial/SDMWGS84Geographic.wfs?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature" \
                     + "&TYPENAME=mapunitpolyextended&FILTER=<Filter><BBOX><PropertyName>Geometry</PropertyName><Box srsName='EPSG:4326'>" \
                     + "<coordinates>%s,%s,%s,%s</coordinates>"%(westlimit, southlimit, eastlimit, northlimit) \
                     + "</Box></BBOX></Filter>&SRSNAME=EPSG:4326&OUTPUTFORMAT=GML2"

#Open the url
t0 = time ()
polyData = urllib.urlopen(polygonAreaUrl)
data = urllib.urlopen(soilDataRequestUrl)
readPolyData = polyData.read()
readData = data.read()
t1 = time()
root = ET.fromstring(readData)



# #Convert the GML respond to json
# poly_o = xmltodict.parse(readPolyData)
# poly_respond_to_json = json.dumps(poly_o)
# o = xmltodict.parse(readData)
# respond_to_json = json.dumps(o) # from '<e> <a>text</a> <a>text</a> </e>' to '{"e": {"a": ["text", "text"]}}'
# t2 = time()
# print t1-t0, t2-t1
# poly_response = json.loads(poly_respond_to_json)
# response = json.loads(respond_to_json)
#
# #open empty lists to append the data
# mukey_soildata = []
# mukey_polydata = []
# hydgrpdcd = []
# poly_area = []
#
# for i in response['wfs:FeatureCollection']['gml:featureMember']:# and
#     hydgrpdcd.append(str(i['ms:mapunitpolyextended']['ms:hydgrpdcd']))
#     mukey_soildata.append(int(i['ms:mapunitpolyextended']['ms:mukey']))#, i['ms:mapunitpoly']['ms:multiPolygon']['ms:muareaacres']
# for i in poly_response['wfs:FeatureCollection']['gml:featureMember']:
#     mukey_polydata.append(int(i['ms:mapunitpoly']['ms:mukey']))
#     poly_area.append(float(i['ms:mapunitpoly']['ms:muareaacres']))
#
# output = zip (hydgrpdcd, mukey_soildata, poly_area, mukey_polydata)
# output.sort()
#
# hyd_area=[]
# percentageOfAvailableData = []
# print "Soil hydrologic Group (%)"
# for i in range(len(output)-1):
#     if output[i][1] != output[i][3]:
#         raise ValueError("The data from the two calls are not muching")
#
#     if output[i][0] == output[i+1][0]:
#         hyd_area.append(output[i][2])
#     else:
#         print output[i][0]," ", sum(hyd_area)/sum(poly_area)*100.00, "%"
#         percentageOfAvailableData.append(sum(hyd_area)/sum(poly_area)*100.00)
#         hyd_area=[]
# print "No data for ",  100 - sum(percentageOfAvailableData), "%"
# print "Done"
