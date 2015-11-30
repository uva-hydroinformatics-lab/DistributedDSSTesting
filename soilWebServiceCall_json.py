__author__ = 'Mohamed Morsy'
import json, xmltodict
import urllib2, urllib
from owslib.fes import *
from owslib.etree import etree
from owslib.wfs import WebFeatureService
import pprint
from time import time


import networkx as nx

from xml.etree import ElementTree as ET

# Study area Box (decimal WGS 1984)
northlimit = 38.076876
eastlimit = -78.412355
southlimit = 37.990639
westlimit = -78.540778

#Build the soil data request URL
soilDataRequestUrl = "http://SDMDataAccess.sc.egov.usda.gov/Spatial/SDMWGS84Geographic.wfs?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature" \
                     + "&TYPENAME=mapunitpolyextended&FILTER=<Filter><BBOX><PropertyName>Geometry</PropertyName><Box srsName='EPSG:4326'>" \
                     + "<coordinates>%s,%s,%s,%s</coordinates>"%(westlimit, southlimit, eastlimit, northlimit) \
                     + "</Box></BBOX></Filter>&SRSNAME=EPSG:4326&OUTPUTFORMAT=GML2"
print soilDataRequestUrl
#Open the url
t0 = time ()
data = urllib.urlopen(soilDataRequestUrl)
readData = data.read()
t1 = time()
o = xmltodict.parse(readData)
respond_to_json = json.dumps(o) # from '<e> <a>text</a> <a>text</a> </e>' to '{"e": {"a": ["text", "text"]}}'
t2 = time()

print t1-t0, t2-t1
response = json.loads(respond_to_json)
#pprint.pprint (response)
# comid = response['wfs:FeatureCollection']['gml:featureMember'][0]['ms:mapunitpolyextended'] thid line is working
for i in response['wfs:FeatureCollection']['gml:featureMember']:
    print i['ms:mapunitpolyextended']['ms:hydgrpdcd']
# filter = PropertyIsLike(propertyname='gml:featureMember', literal='gml:featureMember', wildCard='*')
#
#
# filterxml = etree.tostring(filter.toXML()).decode("utf-8")
#
# readData = data.read(filter=filterxml)

# G = nx.read_gml(readData)

# xml = """
# <?xml version='1.0' encoding='UTF-8'?>
# <!DOCTYPE xgdresponse SYSTEM 'xgdresponse.dtd'>
# <xgdresponse version='1.0'>
#   <transid>2771709</transid>
#   <errorcode>0</errorcode>
#   <response>
#     <result>
#       <element>666</element>
#       <errorcode>0</errorcode>
#       <value>SOMETHING IMPORTANT!</value>
#     </result>
#   </response>
# </xgdresponse>
# """.strip()




# o = xmltodict.parse(readData)
# json_data = json.dumps(o) # '{"e": {"a": ["text", "text"]}}'
# with open('data.txt', 'w') as outfile:
#     json.dump(json_data, outfile, sort_keys = True, indent = 4,ensure_ascii=False)
#print data


