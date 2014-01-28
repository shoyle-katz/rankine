#!/usr/bin/env python3.3
import requests
import argparse

parser = argparse.ArgumentParser(description='''
	Get weather forecast station locations.
	Latitude and longitude of NOAA weather stations outputs as text.
	Gathered from the NOAA website
	(http://www.nws.noaa.gov/mdl/gfslamp/docs/stations_info.shtml).
	Requires an internet connection.''')

args = parser.parse_args()
#   Load raw data as HTML string.
r = requests.get('http://www.nws.noaa.gov/mdl/gfslamp/docs/stations_info.shtml')

#   Find Illinois data segment (in a PRE tag).  We know (from examination) that
#   inside of the PRE block containing ' IL ' (with whitespace and case
#   matching) we can find the IL station data.  This solution isn't robust, but
#   it's good enough for practical cases.
il_start  = r.text.find(' IL ')
tag_start = r.text.rfind('PRE', il_start-200, il_start)
# The string.rfind() function looks backwards from an index.
tag_end   = r.text.find('PRE', il_start)
data = r.text[tag_start+4:tag_end-2]
#print(data)

#   Extract latitude and longitude of stations.  We know the columns are fixed
#   (which is both inconvenient and convenient).  In this case, we will simply
#   set the limits of the relevant columns by counting the number of columns
#   over we need to go.
r_stn  = (5, 9) #remember that the last index is an exclusive bound
r_name = (10, 31)
r_lat  = (36, 41) #we don't need the N/W designation; we know where we are
r_lon  = (46, 51)
for line in data.split('\n'):
    stn  = line[r_stn[0]:r_stn[1]]
    name = line[r_name[0]:r_name[1]]
    try:
        lat  =  float(line[r_lat[0]:r_lat[1]])
        lon  = -float(line[r_lon[0]:r_lon[1]])
    except ValueError:
        # skip rows with invalid data
        continue
    print("%s\t%+6.2f\t%+6.2f"%(stn, lon, lat))

