# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 17:53:33 2021

@author: arkriger

basic script to reproduce the Tissot indicatrices on two Equal Area maps and one Mercator~ 
answer to Question 10  and 11 of Basic Assignment 3
"""

import matplotlib.pyplot as plt
#import cartopy
import cartopy.crs as ccrs

def plot_tissot(ax, **kwargs):
    ax.set_global()
    ax.stock_img()
    ax.coastlines()
    ax.tissot(facecolor='orange', alpha=0.5)
   
fig = plt.figure(figsize=(14, 8))

ax1 = fig.add_subplot(311, projection=ccrs.LambertAzimuthalEqualArea())
plot_tissot(ax1)
ax1.set_title('Lambert Azimuthal Equal Area', fontweight="bold")
ax2 = fig.add_subplot(312, projection=ccrs.LambertCylindrical(central_longitude=-19.0))
plot_tissot(ax2)
ax2.set_title('Lambert Cylindrical Equal Area', fontweight="bold")

ax3 = fig.add_subplot(313, projection=ccrs.Mercator(central_longitude=-19.0))
plot_tissot(ax3)
ax3.set_title('Mercator', fontweight="bold")

plt.show()