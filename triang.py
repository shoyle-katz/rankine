#!/usr/bin/env python
"""
This module provides convenience functions for triangulating data using the Delaunay method.
The actual calculations are carried out with SciPy' Delaunay method.
It was inspired by Jason LaPorte's Javascript "delaunay" code at GitHub:  https://github.com/ironwallaby/delaunay, released by him into the public domain.

"""

from __future__ import division
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

def triangulate_points(points):
    """Triangulate a set of data.  Possible formats include 'list', 'pairs' and ''."""
    points = np.array(points)
    tri = Delaunay(points)
    return tri

def plot_triangulated_points(points,triangles):
    points = np.array(points)
    plt.triplot(points[:,0], points[:,1], triangles.vertices.copy(), 'k-')
    plt.plot(points[:,0], points[:,1], 'b.')
    plt.show()


