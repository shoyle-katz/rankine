#!/usr/bin/env python3.3
import matplotlib as mpl
import matplotlib.pyplot as plt

# Load station tags from stdin.
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

import matplotlib as mpl
mpl.rcParams['figure.figsize']=[10,10]

#These are the stations we loaded above.
plt.scatter(locx, locy, c=temp, marker='D') #scatter plots the points and color-codes them by the c array

#Output the name of each station
for i in range(len(stns)):
    plt.text(locx[i]+0.04, locy[i]+0.02, stns[i])

#The borders of IL in lat/lon coordinates are located in this file and included for context.
x = []; y = []
for line in open('borders_il.txt', 'r'):
    fields = line.strip().split(' ')
    x.append(float(fields[0]))
    y.append(float(fields[1]))
plt.plot(x, y, 'k-')

plt.axis('equal')
plt.title('Weather Stations in Illinois')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
