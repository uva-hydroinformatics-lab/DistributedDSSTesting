import time

from pydap.client import open_url
from pydap.exceptions import ServerError
import datetime as dt

__author__ = 'Mohamed Morsy'


def getData(current_dt, delta_T):
    dtime_fix = current_dt + dt.timedelta(hours=delta_T)
    date = dt.datetime.strftime(dtime_fix, "%Y%m%d")
    fc_hour = dt.datetime.strftime(dtime_fix, "%H")
    hour = str(fc_hour)
    url = 'http://nomads.ncep.noaa.gov:9090/dods/hrrr/hrrr%s/hrrr_sfc_%sz' % (date, hour)
    try:
        # Open the url
        t0 = time.time()
        dataset = open_url(url)
        if len(dataset.keys()) > 0:
            return t0, dataset, url, date, hour
        else:
            # print "Back up method - Failed to open : %s" % url
            return getData(current_dt, delta_T - 1)
    except ServerError:
        # print "Failed to open : %s" % url
        return getData(current_dt, delta_T - 1)


time_precip = ['time']

# i = how many times you want to run the same trial
for i in range(25):
    # Get newest available HRRR dataset by trying (current datetime - delta time) until
    # a dataset is available for that hour. This corrects for inconsistent posting
    # of HRRR datasets to repository
    utc_datetime = dt.datetime.utcnow()
    # print "Open a connection to HRRR to retrieve forecast rainfall data.............\n"
    # get newest available dataset
    t0, dataset, url, date, hour = getData(utc_datetime, delta_T=0)
    # print ("Retrieving forecast data from: %s " % url)

    # select desired forecast product from grid, grid dimensions are time, lat, lon
    # apcpsfc = "surface total precipitation" [mm]
    # source: http://www.nco.ncep.noaa.gov/pmb/products/hrrr/hrrr.t00z.wrfsfcf00.grib2.shtml
    var = "apcpsfc"
    precip = dataset[var]
    t1 = time.time()
    # print ("Dataset open")
    time_precip.append(t1-t0)


for k in range(len(time_precip)):
    print '%s' \
        % (time_precip[k])


