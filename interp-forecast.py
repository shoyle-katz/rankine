#!/usr/bin/env python3.3

# Distance formula
from math import sqrt
def dist(pt1, pt2):
    """Calculate the Euclidean distance between two points."""
    return sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)

# Load station data from stdin.
import sys
stns = []
locx = []
locy = []
temp = []
for line in sys.stdin:
    elems = line.split()
    stns.append(elems[0]) #station name
    locx.append(float(elems[1]))
    locy.append(float(elems[2]))
    temp.append(float(elems[3]))

for (i, stn) in enumerate(stns):
    print("%s\t%+6.2f\t%+6.2f\t%+3.0f"%(stn, locx[i], locy[i], temp[i]))

# Parse command-line arguments for latitude and longitude.
import getopt,sys
options, args = getopt.getopt(sys.argv[1:], '', ['lat=', 'lon='])
for option, value in options:
    if option in ('--lat'):
        ptx = float(value)
    elif option in ('--lon'):
        pty = float(value)
    else:
        sys.exit('Invalid command-line usage encountered.')

# Set up the interpolation
pt = (pty, ptx)

# Find the three nearest neighbors of the point we are at.
#   Get a list of all neighbors from this point.  Store them by distance and index.
dists = []
for i in range(0, len(locx)):
    loc = (locx[i], locy[i])
    dists.append((dist(loc, pt), i))

#   Sort the list to take the nearest three sites.
dists.sort()

# Interpolate the points.
# Use a simple 3-nearest-neighbor weighted average rather than triangulation.
wts = [0]*3
wts[0] = 1/(dists[0][0] ** 2)
wts[1] = 1/(dists[1][0] ** 2)
wts[2] = 1/(dists[2][0] ** 2)
T_pt = (wts[0]*temp[dists[0][1]] + wts[1]*temp[dists[1][1]] + wts[2]*temp[dists[2][1]]) / sum(wts)

print("%s\t%+6.2f\t%+6.2f\t%+3.0f"%('user', pt[0], pt[1], T_pt))

