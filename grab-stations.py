#!/usr/bin/env python3.3
import requests
import argparse
import sys
import logging

def get_command_line_args():
    script_desc = '''Get weather forecast station locations.
        Latitude and longitude of NOAA weather stations outputs as text.
        Gathered from the NOAA website
        (http://www.nws.noaa.gov/mdl/gfslamp/docs/stations_info.shtml).
        Requires an internet connection.'''
    outfile_param_help = '''The name of the file to write the station list to.
        Defaults to stdout if no file specified.'''
    parser = argparse.ArgumentParser(description=script_desc)
    parser.add_argument('-o', '--outfile', type=argparse.FileType('w'),
                        default=sys.stdout, help=outfile_param_help)
    return parser.parse_args()

def grab_website_text():
    '''Get raw data as HTML string from the NOAA website.'''
    url = 'http://www.nws.noaa.gov/mdl/gfslamp/docs/stations_info.shtml'
    page = requests.get(url)
    return page.text

def extract_illinois_section(text):
    '''Find Illinois data segment (in a PRE tag).
    We know (from examination) that inside of the PRE block containing ' IL '
    (with whitespace and case matching) we can find the IL station data.
    This solution isn't robust, but it's good enough for practical cases.'''
    il_start  = text.find(' IL ')
    tag_start = text.rfind('PRE', il_start-200, il_start) # look backwards
    tag_end   = text.find('PRE', il_start)
    return text[tag_start+4:tag_end-2]

def parse_station_line(line):
    '''Extract latitude and longitude of stations. We know the columns are fixed
    (which is both inconvenient and convenient). In this case, we will simply
    set the limits of the relevant columns by counting the number of columns
    over we need to go.'''
    r_stn  = (5, 9) #remember that the last index is an exclusive bound
    r_name = (10, 31)
    r_lat  = (36, 41) #we don't need the N/W designation; we know where we are
    r_lon  = (46, 51)
    stn  = line[r_stn[0]:r_stn[1]]
    name = line[r_name[0]:r_name[1]]
    lat  =  float(line[r_lat[0]:r_lat[1]])
    lon  = -float(line[r_lon[0]:r_lon[1]])
    return stn, lat, lon

if __name__=='__main__':
    args = get_command_line_args()
    text = grab_website_text()
    data = extract_illinois_section(text)
    for line in data.splitlines():
        try:
            stn, lat, lon = parse_station_line(line)
            args.outfile.write("%s\t%+6.2f\t%+6.2f\n"%(stn, lon, lat))
        except ValueError:
            logging.warning('Could not parse line: {0}'.format(line))
