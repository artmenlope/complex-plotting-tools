# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:40:38 2020

@author: artmenlope

Examples using the cosine function and the 
complex function from the Wikipedia Domain 
Coloring example found at 
https://en.wikipedia.org/wiki/File:Domain_coloring_x2-1_x-2-i_x-2-i_d_x2%2B2%2B2i.xcf
"""

import numpy as np
import matplotlib.pyplot as plt
import cplotting_tools as cplt



plt.close("all")

#============================== Wiki function.

N = 100
lim = 3
x, y = np.meshgrid(np.linspace(-lim,lim,N), 
                   np.linspace(-lim,lim,N))

z = x + 1j*y

f = (z**2-1)*(z-2-1j)**2/(z**2+2+2j)
pts = [-1, 1, 2+1j, 2**(3/4)*np.exp(1j*(5*np.pi/8)), 2**(3/4)*np.exp(1j*(5*np.pi/8+np.pi))]

cplt.domain_coloring(x, y, f, cmap="hsv")
# cplt.domain_coloring(x, y, f, cmap="twilight_r")

# cplt.domain_coloring_illuminated(x, y, f)
# cplt.domain_coloring_illuminated(x, y, f, log_brightness=False)

# cplt.complex_plot3D(x, y, f, log_mode=False)
# cplt.complex_plot3D(x, y, f, log_mode=True)

# cplt.plot_re_im(x, y, f, cmap="twilight", contour=False, alpha=0.9)
# cplt.plot_re_im(x, y, f, cmap="twilight", contour=True, alpha=0.9)

# cplt.complex_streamplot(x, y, f, mod_as_linewidths=True, cmap="twilight_r", density=2, scatterpoints=pts) #twilight_r

# cplt.complex_contour(x, y, f, mode="modulus", levels=np.arange(0,21,1), lw=2, cmap="coolwarm", scatterpoints=pts) # "coolwarm" imshow with "copper" contour looks good usually. "bone" imshow with "coolwarm" contour is also fine
      
#============================== cosine function.

# N = 40
# lim = 6
# x, y = np.meshgrid(np.linspace(-lim,lim,N), 
#                    np.linspace(-lim,lim,N))

# z = x + 1j*y

# f = np.cos(z)

# cplt.complex_vector_field(x, y, f, norm=False)
# cplt.complex_vector_field(x, y, f, norm=True)
# cplt.complex_vector_field(x, y, f, cmap="hsv", norm=False)
# cplt.complex_vector_field(x, y, f, cmap="hsv", norm=True)