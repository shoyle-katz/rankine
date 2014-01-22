rankine
=======

A demonstration of some principles of scientific data processing in
Python for Software Carpentry (SWC) at UIUC.

## Usage

	$ python grab-stations.py > stations.txt
	$ python grab-forecast.py < stations.txt > forecast.txt
	$ python plot-forecast.py < forecast.txt

Urbana is 40.1097° N, 88.2042° W

	$ python interp-forecast.py --lat=40.1 --lon=88.2 < forecast.txt
