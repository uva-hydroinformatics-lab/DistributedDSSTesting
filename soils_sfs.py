__author__ = 'Stuart Sheffield'
import urllib
import time

# Study area Box (decimal WGS 1984)
northlimit = [38.076390, 38.076359, 38.078177, 38.080728, 38.114]
eastlimit = [-78.454988, -78.453267, -78.449663, -78.433296, -78.375]
southlimit = [38.075921, 38.074737, 38.073350, 38.065115, 38.065115]
westlimit = [-78.455846, -78.455819, -78.457972, -78.459817, -78.459817]

poly_sm = ['poly_sm']
soils_sm = ['soils_sm']

poly_md = ['poly_md']
soils_md =['soils_md']

poly_lg = ['poly_lg']
soils_lg = ['soils_lg']

poly_xl = ['poly_xl']
soils_xl =['soils_xl']

poly_xxl = ['poly_xxl']
soils_xxl =['soils_xxl']

for i in range(100):
    for j in range(len(northlimit)):
    
        #Build the soil data request URL
        polygonAreaUrl = "http://SDMDataAccess.sc.egov.usda.gov/Spatial/SDMWGS84Geographic.wfs?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature" \
                         + "&TYPENAME=MapunitPoly&FILTER=<Filter><BBOX><PropertyName>Geometry</PropertyName><Box srsName='EPSG:4326'>" \
                         + "<coordinates>%s,%s,%s,%s</coordinates>"%(westlimit[j], southlimit[j], eastlimit[j], northlimit[j]) \
                         + "</Box></BBOX></Filter>&SRSNAME=EPSG:4326&OUTPUTFORMAT=GML2"
        
        soilDataRequestUrl = "http://SDMDataAccess.sc.egov.usda.gov/Spatial/SDMWGS84Geographic.wfs?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature" \
                         + "&TYPENAME=mapunitpolyextended&FILTER=<Filter><BBOX><PropertyName>Geometry</PropertyName><Box srsName='EPSG:4326'>" \
                         + "<coordinates>%s,%s,%s,%s</coordinates>"%(westlimit[j], southlimit[j], eastlimit[j], northlimit[j]) \
                         + "</Box></BBOX></Filter>&SRSNAME=EPSG:4326&OUTPUTFORMAT=GML2"
        
        #Open the url
        t0 = time.time()
        polyData = urllib.urlopen(polygonAreaUrl)
        t1= time.time()
        data = urllib.urlopen(soilDataRequestUrl)
        readPolyData = polyData.read()
        readData = data.read()
        t2 = time.time()
        
        if j == 0:
            poly_sm.append(t1-t0)
            soils_sm.append(t2-t1)
            
        if j == 1:
            poly_md.append(t1-t0)
            soils_md.append(t2-t1)
            
        if j == 2:
            poly_lg.append(t1-t0)
            soils_lg.append(t2-t1)
            
        if j == 3:
            poly_xl.append(t1-t0)
            soils_xl.append(t2-t1)

        if j == 4:
            poly_xxl.append(t1-t0)
            soils_xxl.append(t2-t1)
    
for k in range(len(poly_sm)):
    print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(poly_sm[k],soils_sm[k],poly_md[k],soils_md[k],poly_lg[k],soils_lg[k],poly_xl[k],soils_xl[k],poly_xxl[k],soils_xxl[k])
