#!/usr/bin/env python3.3
import unittest
import grab_stations

class TestParsing(unittest.TestCase):

    def test_parse_line(self):
        line = ' 8   KVYS PERU                 IL   41.35N    89.15W'
        stn, lat, lon = grab_stations.parse_station_line(line)
        self.assertEqual(['KVYS', 41.35, -89.15], [stn, lat, lon])

if __name__ == '__main__':
    unittest.main()
