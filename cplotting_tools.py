# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:05:40 2020

@author: Arturo Mena López
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cmath



def colorize(f, a=0.5, log_brightness=True, log_contrast=0.4):
    
    """
    Auxiliar function for creating domain coloring plots.
    
    Given the evaluated function f, returns an array of colors
    representing the function's phase. 
    
    The resulting colors encode the module of the function as 
    the brightness.

    Arguments:

        f :: 2D numpy array of complex numbers. Evaluated 
             function to be plotted.

        a :: Float between 0 and 1. Parameter for the brightness.

        log_brightness :: Boolean. If True, the module of f is
                          represented via the brightness of the
                          colors in a logarithmic way. If False,
                          The brightness changes exponentially as
                          the module of f increases.

        log_contrast :: Float. Parameter for the brightness.
    """

    from colorsys import hls_to_rgb
    
    def logb(arg, base):
        """Return the logarithm with base b of arg."""
        return np.log(base) / np.log(base)
       
    H = (np.pi-np.arctan2(f.imag, -f.real))/(2*np.pi) # Hue.
   
    if log_brightness == False:
        L = (1-a**np.abs(f)) # Brightness.
        
    if log_brightness == True:
        L = 1-a**np.log(1+np.abs(f)**log_contrast)
        
    S = 1 # Saturation.
    
    c = np.vectorize(hls_to_rgb)(H, L, S) # --> Tuple.
    c = np.array(c)  # The array of colors c is of shape (3,n,m), but it needs to be (m,n,3).
    c = np.rot90(c.transpose(2,1,0), 1) # Change shape to (m,n,3) and rotate 90 degrees as correction.
    
    return c



def domain_coloring(x, y, f, 
                   figsize=(12,8),
                   xlabel="Re", 
                   ylabel="Im",
                   title=None,
                   grid=False,
                   cmap="hsv"):
    
    """
    Domain coloring plot. 
    
    The evaluated function f is transformed to polar form and its 
    phase is represented using colors. The module is not represented.
    
    See https://en.wikipedia.org/wiki/Domain_coloring for more 
    information.

    x, y, f are 2D arrays. f can contain complex numbers.
    figsize, xlabel, ylabel, title, grid and cmap are parameters 
    for the Matplotlib plot.
    """
    
    arg_f = np.mod(np.angle(f),2*np.pi) # np.mod ensures argument from 0 to 2*pi
    lim = np.max([x, y])

    # Prepare for using colormaps.
    norm = matplotlib.colors.Normalize(vmin=0,vmax=2*np.pi)
    c_m = cmap #twilight, hsv
    s_m = matplotlib.cm.ScalarMappable(cmap=c_m, norm=norm)
    s_m.set_array([])
    fcolors = s_m.to_rgba(arg_f)
    
    # A figure and a 3d subplot.
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    
    # Limit corrections.
    ax.set_xlim((-lim,lim))
    ax.set_ylim((-lim,lim))
    
    # Grid and title.
    ax.grid(grid)
    
    if title is not None:
        ax.set_title(title, fontsize=18, pad=20, usetex=False)
        
    ax.imshow(arg_f, cmap=cmap, extent=[-lim,lim,-lim,lim], interpolation="none", origin="lower")
   
    # Draw the colorbar.
    cbar = plt.colorbar(s_m, ticks=[0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], pad=0.1)
    cbar.ax.set_yticklabels(["$0$", "$\\frac{\\pi}{2}$", "$\\pi$", "$\\frac{3\\pi}{2}$", "$2\\pi$"], fontsize=16)
    
    plt.tight_layout()
    plt.show()



def domain_coloring_illuminated(x, y, f, 
                                a = 0.5,
                                log_brightness=True,
                                log_contrast=0.4,
                                figsize=(12,8),
                                xlabel="Re", 
                                ylabel="Im",
                                title=None,
                                grid=False,
                                cmap="hsv"):
    
    """
    Domain coloring plot. 
    
    The function f is transformed to polar form and its phase 
    is represented using colors. The module is represented using
    the brightness of the colors.
    
    See https://en.wikipedia.org/wiki/Domain_coloring for more 
    information.

    Arguments:

        x, y :: 2D arrays. They represent the 2D plotting space.

        f :: 2D numpy array of complex numbers. Evaluated 
             function to be plotted.

        a :: Float between 0 and 1. Parameter for the brightness.

        log_brightness :: Boolean. If True, the module of f is
                          represented via the brightness of the
                          colors in a logarithmic way. If False,
                          The brightness changes exponentially as
                          the module of f increases.

        log_contrast :: Float. Parameter for the brightness.

        figsize, xlabel, ylabel, title, grid and cmap are parameters 
        for the Matplotlib plot.
    """
    
    img = colorize(f, a, log_brightness, log_contrast)
    arg_f = np.mod(np.angle(f),2*np.pi) # np.mod ensures argument from 0 to 2*pi
    lim = np.max([x, y])

    # initializing the colormap machinery
    norm = matplotlib.colors.Normalize(vmin=0,vmax=2*np.pi)
    c_m = cmap #twilight, hsv
    s_m = matplotlib.cm.ScalarMappable(cmap=c_m, norm=norm)
    s_m.set_array([])
    fcolors = s_m.to_rgba(arg_f)
    
    # a figure and a 3d subplot
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    
    # Limit corrections
    ax.set_xlim((-lim,lim))
    ax.set_ylim((-lim,lim))
    
    # Grid and title
    ax.grid(grid)
    
    if title is not None:
        ax.set_title(title, fontsize=18, pad=20, usetex=False)
        
    #ax.contourf(x, y, arg_f, cmap="hsv", levels=50, alpha=1)
    ax.imshow(img, extent=[-lim,lim,-lim,lim], interpolation="none", origin="upper")
   
    # Draw the colorbar 
    cbar = plt.colorbar(s_m, ticks=[0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], pad=0.1)
    cbar.ax.set_yticklabels(["$0$", "$\\frac{\\pi}{2}$", "$\\pi$", "$\\frac{3\\pi}{2}$", "$2\\pi$"], fontsize=16)
    
    plt.tight_layout()
    plt.show()
    
    

def complex_plot3D(x, y, f, 
                   figsize=(12,8),
                   f_lim=10,
                   offset=0,
                   xlabel="Re", 
                   ylabel="Im", 
                   zlabel="$|f(z)|$",
                   title=None,
                   grid=True,                    
                   contour3D=False,
                   log_mode=True):
    
    """
    3D plot representing he evaluated complex function f. 
    
    f is transformed to polar form. The module is represented 
    as a 3d surface and the phase is represented as colors over
    said surface like in a domain coloring plot. In addition, 
    the module of f is represented like shadows at the bottom
    of the plot. A darker shadow indicates lower values for
    the module.

    Arguments:

        x, y :: 2D arrays. They represent the 2D plotting space.

        f :: 2D numpy array of complex numbers. Evaluated 
             function to be plotted.

        f_lim :: Float greater than 0. Set the limit of the 
                 vertical axis. Improves the visualization in 
                 case the module diverges to infinity.

        contour3D :: Boolean. If True, plot a contour over the 
                     f module's plane at the bottom of the plot.

        log_mode :: Boolean. If True, the colors of the module's 
                    representation will increase in a logarithmic 
                    way.

        offset, xlabel, ylabel, zlabel, title and grid are parameters 
        for Matplotlib.
    """
    
    if log_mode == True:
        abs_f = np.log2(np.abs(f)+1)
    if log_mode == False:
        abs_f = np.abs(f)
        
    arg_f = np.mod(np.angle(f),2*np.pi) # np.mod ensures argument from 0 to 2*pi
    lim = np.max([x, y])

    # initializing the colormap machinery
    norm = matplotlib.colors.Normalize(vmin=0,vmax=2*np.pi)
    c_m = matplotlib.cm.hsv #twilight, hsv
    s_m = matplotlib.cm.ScalarMappable(cmap=c_m, norm=norm)
    s_m.set_array([])
    fcolors = s_m.to_rgba(arg_f)
    
    # a figure and a 3d subplot
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    ax.set_zlabel(zlabel, fontsize=14, labelpad=10)
    
    # Limit corrections
    abs_f[abs_f > f_lim] = f_lim
    lim = 0.96*lim
    ax.set_xlim((-lim,lim))
    ax.set_ylim((-lim,lim))
    ax.set_zlim((0,f_lim))
    
    # Grid and title
    ax.grid(grid)
    
    if title is not None:
        ax.set_title(title, fontsize=18, pad=20, usetex=False)
        
    # make the bottom pane transparent
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    
    # Plot the modulus' surface with the argument as color.
    ax.plot_surface(x, y, abs_f, linewidth=0, alpha=0.7,
                    cstride=1, rstride=1,
                    facecolors=fcolors)
    
    if contour3D == True:
        ax.contour3D(x, y, abs_f, alpha=0.5, colors='black', levels=20)
    
    ax.contourf(x, y, np.log2(abs_f+1), zdir='z', offset=offset  , cmap="gist_yarg_r", levels=50, alpha=1)
   
    # Draw the colorbar 
    cbar = plt.colorbar(s_m, ticks=[0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], pad=0.1)
    cbar.ax.set_yticklabels(["$0$", "$\\frac{\\pi}{2}$", "$\\pi$", "$\\frac{3\\pi}{2}$", "$2\\pi$"], fontsize=16)
    
    plt.tight_layout()
    plt.show()



def plot_re_im(x, y, f, 
               figsize=(14,7),
               alpha=1,
               # f_lims=None,
               title=None,
               grid=True,                    
               contour=False,
               cmap="viridis",
               synchronize_rotations=False):

    """
    Plot the real and the imaginary parts of the function 
    f in separated subplots as surfaces. The surfaces can 
    also be projected into a filled contour plot at the 
    bottom of the vertical axis.
    
    Arguments:

        x, y :: 2D arrays. They represent the 2D plotting 
                space.

        f :: 2D numpy array of complex numbers. Evaluated 
             function to be plotted.

        synchronize_rotations :: Boolean. If True, when using
                                 the Matplotlib's interactive
                                 plotting window and rotating
                                 a subplot, both subplots will 
                                 synchronize the rotation.

        figsize, alpha, title, grid, contour and cmap are 
        parameters for Matplotlib.
    """
    
    lim = np.max([x, y])
    
    # A figure and a 3d subplot
    fig = plt.figure(figsize=figsize)
    ax_re = fig.add_subplot(121, projection="3d")
    ax_im = fig.add_subplot(122, projection="3d")
    
    ax_re.set_xlabel("Re", fontsize=14)
    ax_re.set_ylabel("Im", fontsize=14)
    ax_re.set_title("Re $f(z)$", fontsize=18)
    
    ax_im.set_xlabel("Re", fontsize=14)
    ax_im.set_ylabel("Im", fontsize=14)
    ax_im.set_title("Im $f(z)$", fontsize=18)
    
    ax_re.set_xlim((-lim,lim))
    ax_re.set_ylim((-lim,lim))
    
    ax_im.set_xlim((-lim,lim))
    ax_im.set_ylim((-lim,lim))
    
    # Grid and title
    ax_re.grid(grid)
    ax_im.grid(grid)
    
    if title is not None:
        fig.suptitle(title, fontsize=18, usetex=False)
        
    # Plot function components.
    ax_re.plot_surface(x, y, f.real, linewidth=0, alpha=alpha,
                       cstride=1, rstride=1,
                       cmap=cmap)
    
    ax_im.plot_surface(x, y, f.imag, linewidth=0, alpha=alpha,
                       cstride=1, rstride=1,
                       cmap=cmap)
    
    if contour == True:
        ax_re.contourf(x, y, f.real, zdir='z', offset=ax_re.get_zlim()[0], cmap=cmap, levels=50, alpha=1)
        ax_im.contourf(x, y, f.imag, zdir='z', offset=ax_im.get_zlim()[0], cmap=cmap, levels=50, alpha=1)
    
    if synchronize_rotations == True:
        
        def on_move(event):
            if event.inaxes == ax_re:
                ax_im.view_init(elev=ax_re.elev, azim=ax_re.azim)
            elif event.inaxes == ax_im:
                ax_re.view_init(elev=ax_im.elev, azim=ax_im.azim)
            else:
                return
            fig.canvas.draw_idle()
    
        fig.canvas.mpl_connect('motion_notify_event', on_move)
        
    plt.tight_layout()
    plt.show()
    
    
    
def complex_vector_field(x, y, f,
                         figsize=(12,8),
                         title=None,
                         grid=False,
                         cmap=None,
                         dark_background=False,
                         norm=False):
    
    """
    Plot the complex function f as a 2D vector field.
    The plotted vectors have the form (Real(f), Imag(f)). 
    In polar form, the argument of the function f can
    be represented using a colormap in addition to the
    already visualized orientation of the vectors.

    Arguments:

        x, y :: 2D arrays. They represent the 2D plotting 
                space.

        f :: 2D numpy array of complex numbers. Evaluated 
             function to be plotted.

        dark_background :: Boolean. If True, sets the axis 
                           background color to black.

        norm :: Boolean. If True, normalizes the vectors.

        figsize, title, grid and cmap are parameters for 
        Matplotlib.
    """

    # Vector normalization.
    if norm == True:
        r = np.sqrt(f.real**2+f.imag**2)
        f = f.real/r + 1j*f.imag/r
    
    # Create the figure and axis.
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    
    # Colormap.
    if cmap is None:
        
        ax.quiver(x, y, np.real(f), np.imag(f),  
                  color='blue', 
                  pivot="middle", 
                  norm=True, 
                  headwidth=6, 
                  headlength=7)
        
    if cmap is not None:
        
        arg_f = np.mod(np.angle(f),2*np.pi)
        
        norm = matplotlib.colors.Normalize(vmin=0,vmax=2*np.pi)
        c_m = cmap # "twilight", "hsv", ...
        s_m = matplotlib.cm.ScalarMappable(cmap=c_m, norm=norm)
        s_m.set_array([])
        
        # Plot the vectors.
        ax.quiver(x, y, np.real(f), np.imag(f), arg_f, 
                  cmap=cmap,
                  pivot="middle",
                  headwidth=6, 
                  headlength=7)

        # Add a colorbar.
        cbar = plt.colorbar(s_m, ticks=[0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], pad=0.1)
        cbar.ax.set_yticklabels(["$0$", "$\\frac{\\pi}{2}$", "$\\pi$", "$\\frac{3\\pi}{2}$", "$2\\pi$"], fontsize=16)
    
    # Axis labels.
    ax.set_xlabel("Re", fontsize=14)
    ax.set_ylabel("Im", fontsize=14)
    
    # Grid and title
    ax.grid(grid)
    
    if title is not None:
        ax.set_title(title, fontsize=18, pad=20, usetex=False)
        
    # Dark background.
    if dark_background == True:
        ax.set_facecolor('black')
        
    plt.tight_layout()
    plt.show()



def complex_streamplot(x, y, f,
                       figsize=(12,8),
                       title=None,
                       grid=False,
                       color="blue",
                       cmap=None,
                       dark_background=False,
                       mod_as_linewidths=False,
                       density=1,
                       scatterpoints=[],
                       pointsize=70,  # The default is 20.
                       pointcolor="black", 
                       pointalpha=1, 
                       pointedgecolors="black", 
                       pointlw=1.5, 
                       pointmarker="o"):
    
    """
    Plot the complex function f as a 2D streamplot.
    It is similar to a vector field plot where the 
    plotted vectors have the form (Real(f), Imag(f)). 
    In polar form, the argument of the function f can
    be represented using a colormap in addition to the
    already visualized orientation of the stream vectors.
    The module of f can be represented as the thickness 
    of the lines of the stream if mod_as_linewidths is 
    set to be True. Scatterpoints can also be added to
    the plot.

    Arguments:

        x, y :: 2D arrays. They represent the 2D plotting 
                space.

        f :: 2D numpy array of complex numbers. Evaluated 
             function to be plotted.

        dark_background :: Boolean. If True, sets the axis 
                           background color to black.

        mod_as_linewidths :: Boolean. If True, the module 
                             of f is represented as the 
                             thickness of the lines of the 
                             stream.

        figsize, title, grid, color, cmap and density are 
        parameters for Matplotlib.

        scatterpoints :: List of complex numbers. The points 
                         contained in this list will be 
                         plotted as scatterpoints.

        pointsize, pointcolor, pointalpha, pointedgecolors, 
        pointlw and pointmarker are parameters defining the 
        properties of the scatter points. These parameters 
        are passed to Matplotlib.
    """

    # Create the figure and the axis.
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    
    # Colormap.
    if cmap is None:
        
        if mod_as_linewidths == False:
            
            ax.streamplot(x, y, np.real(f), np.imag(f), color=color, density=density)
            
        if mod_as_linewidths == True:
            
            abs_f = np.log2(np.abs(f)+1)
            abs_f = abs_f/np.max(abs_f)
            ax.streamplot(x, y, np.real(f), np.imag(f), color=color, linewidth=7*abs_f, density=density)
        
    if cmap is not None:
        
        arg_f = np.mod(np.angle(f),2*np.pi)
        
        norm = matplotlib.colors.Normalize(vmin=0,vmax=2*np.pi)
        c_m = cmap #twilight, hsv
        s_m = matplotlib.cm.ScalarMappable(cmap=c_m, norm=norm)
        s_m.set_array([])
        
        if mod_as_linewidths == False:
            
            ax.streamplot(x, y, np.real(f), np.imag(f), color=arg_f, cmap=cmap, density=density)
            
        if mod_as_linewidths == True:
            
            abs_f = np.log2(np.abs(f)+1)
            abs_f = abs_f/np.max(abs_f)
            ax.streamplot(x, y, np.real(f), np.imag(f), color=arg_f, cmap=cmap, linewidth=7*abs_f, density=density)

        cbar = plt.colorbar(s_m, ticks=[0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], pad=0.1)
        cbar.ax.set_yticklabels(["$0$", "$\\frac{\\pi}{2}$", "$\\pi$", "$\\frac{3\\pi}{2}$", "$2\\pi$"], fontsize=16)
        
    # Plot the scatterpoints. 
    if len(scatterpoints) != 0:
        scatterpoints = np.asarray(scatterpoints)
        ax.scatter(scatterpoints.real, scatterpoints.imag, 
                   s=pointsize, 
                   color=pointcolor, 
                   alpha=pointalpha, 
                   edgecolors=pointedgecolors, 
                   linewidths=pointlw, 
                   marker=pointmarker,
                   zorder=100)
    
    # Axis labels.
    ax.set_xlabel("Re", fontsize=14)
    ax.set_ylabel("Im", fontsize=14)
    
    # Grid and title
    ax.grid(grid)
    
    # Title.
    if title is not None:
        ax.set_title(title, fontsize=18, pad=20, usetex=False)
    
    # Set the axis background color to black.
    if dark_background == True:
        ax.set_facecolor('black')
        
    plt.tight_layout()
    plt.show()



def complex_contour(x, y, f, 
                    mode="real",
                    figsize=(8,8),
                    levels=20,
                    xlabel="Re", 
                    ylabel="Im",
                    clabels=True,
                    title=None,
                    usetex=False,
                    grid=False,
                    axis=True,
                    cmap="viridis",
                    ls="solid",
                    lw=1,
                    scatterpoints=[],
                    pointsize=70,  # The default is 20.
                    pointcolor="black", 
                    pointalpha=1, 
                    pointedgecolors="black", 
                    pointlw=1.5, 
                    pointmarker="o",
                    dark_background=False,
                    imshow=False,
                    imcmap="coolwarm"):
        
    """
    Plot either the real or the imaginary part of f (or 
    both) as a contour plot. Scatterpoints can also be 
    added to the plot.

    Arguments:

        x, y :: 2D arrays. They represent the 2D plotting 
                space.

        f :: 2D numpy array of complex numbers. Evaluated 
             function to be plotted.

        mode :: "real", "imag", "modulus" or "both". 
                Choose between plotting the contour of 
                either the real part of f, the imaginary 
                part or both.

        figsize, levels, xlabel, ylabel, clabels, title, 
        usetex, grid, axis, cmap ls and lw are parameters 
        for Matplotlib. levels can be either a list or an 
        integer.

        scatterpoints :: List of complex numbers. The points 
                         contained in this list will be 
                         plotted as scatterpoints.

        pointsize, pointcolor, pointalpha, pointedgecolors, 
        pointlw and pointmarker are parameters defining the 
        properties of the scatter points. These parameters 
        are passed to Matplotlib.

        dark_background :: Boolean. If True, sets the axis 
                           background color to black.

        imshow :: Boolean. If True, shows the module of f as 
                  an imshow plot. Only works if mode!="both".

        imcmap :: String. Colormap for the imshow plot (only 
                  used if imshow=True and mode!="both").
    """
    
    # Get the limit for the plot.
    lim = np.max([x, y])  

    # Create the figure and the axis.
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.set_xlabel(xlabel, fontsize=14, usetex=usetex)
    ax.set_ylabel(ylabel, fontsize=14, usetex=usetex)
    
    # Limit corrections
    ax.set_xlim((-lim,lim))
    ax.set_ylim((-lim,lim))
    
    # Decide whether the subplot's axis is shown or not.
    ax.axis(axis)
    # If grid=True sets the grid to be displayed.
    ax.grid(grid)
    
    # Set the default title of the plot.
    if title is None:
        if mode == "real":
            title = "Contour of Re $f(z)$"
        if mode == "imag":
            title = "Contour of Im $f(z)$"
        if mode == "both":
            title = "Contour of Re $f(z)$ & Im $f(z)$"
        if mode == "modulus":
            title = "Contour of $|f(z)|$"
    
    ax.set_title(title, fontsize=18, pad=20, usetex=usetex)
    
    # Mode of the plot.
    if mode != "both":
        
        if mode == "imag":
            f2 = f.imag    
        if mode == "real":
            f2 = f.real
        if mode == "modulus":
            f2 = np.abs(f)
        
        # Plot the contourf.
        cont = ax.contour(x, y, f2, levels=levels, linestyles=ls, linewidths=lw, cmap=cmap)
        # cont = ax.contourf(x, y, np.array(np.abs(f2), dtype=float), levels=levels, cmap=cmap)
        
        # Labels for the contour lines.
        if clabels == True:
            ax.clabel(cont, fontsize=9, inline=1)
            
        if imshow == True:
            ax.imshow(np.array(f2, dtype=float), cmap=imcmap, extent=[-lim,lim,-lim,lim], interpolation="none", origin="lower") #cmap="GnBu" #force float type in f
        
    if mode == "both":
        
        cont_re = ax.contour(x, y, f.real, levels=levels, linestyles=ls, linewidths=lw, colors="C3") #C0 = default red
        if clabels == True:
            ax.clabel(cont_re, fontsize=9, inline=1)
        
        cont_im = ax.contour(x, y, f.imag, levels=levels, linestyles=ls, linewidths=lw, colors="C0") #C3 = default blue
        if clabels == True:
            ax.clabel(cont_im, fontsize=9, inline=1)
    
    # Plot the scatterpoints.
    if len(scatterpoints) != 0:
        scatterpoints = np.asarray(scatterpoints)
        ax.scatter(scatterpoints.real, scatterpoints.imag, 
                   s=pointsize, 
                   color=pointcolor, 
                   alpha=pointalpha, 
                   edgecolors=pointedgecolors, 
                   linewidths=pointlw, 
                   marker=pointmarker,
                   zorder=100)
    
    # Dark background.
    if dark_background == True:
        ax.set_facecolor('black')
        
    plt.tight_layout()
    plt.show()