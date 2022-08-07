[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/artmenlope/complex-plotting-tools/blob/master/LICENSE.md)
![Last Commit](https://img.shields.io/github/last-commit/artmenlope/complex-plotting-tools)

# complex-plotting-tools
Module for plotting complex-valued functions of complex variable using different methods.

## Table of contents

- [Examples gallery](#Examples-gallery)
  - [Examples 1](#Examples-1)
  - [Examples 2](#Examples-2)

## Examples gallery

A script for generating the following examples can be found at [`examples.py`](examples.py).

To use this module just place the script [`cplotting_tools.py`](cplotting_tools.py) in your working directory. It can be imported like this:

```python
import cplotting_tools as cplt
```

### Examples 1 

In this first set of examples the test function is the following one:

$$
f(z) = \dfrac{(z^2-1)(z-2-i)^2}{z^2+2+2i}
$$

We start defining the variables and parameters for these first examples:

```python
import numpy as np

N = 100
lim = 3
x, y = np.meshgrid(np.linspace(-lim,lim,N), 
                   np.linspace(-lim,lim,N))
z = x + 1j*y
```

The code of the function <img src="https://render.githubusercontent.com/render/math?math=f">, `f`, and its set of poles and zeros, `pts`, looks like this:

```python
f = (z**2-1)*(z-2-1j)**2/(z**2+2+2j)
pts = [-1, 1, 2+1j, 2**(3/4)*np.exp(1j*(5*np.pi/8)), 2**(3/4)*np.exp(1j*(5*np.pi/8+np.pi))]
```

Then, we can use the functions defined in [`cplotting_tools.py`](cplotting_tools.py) to generate, for example, the following plots:

![](cplotting-images/domain_coloring.png) <br> `cplt.domain_coloring(x, y, f, cmap="hsv")` |  ![](cplotting-images/domain_coloring_cmap.png) <br> `cplt.domain_coloring(x, y, f, cmap="twilight_r")`
| :-------------: | :-------------: |
![](cplotting-images/domain_coloring_illum.png) <br> **`cplt.domain_coloring_illuminated(x, y, f, log_brightness=False)`** |  ![](cplotting-images/domain_coloring_illum_logbrightness.png) <br> **`cplt.domain_coloring_illuminated(x, y, f)`**
![](cplotting-images/plot3D_logmodeFalse.png)  <br> **`cplt.complex_plot3D(x, y, f, log_mode=False)`** |  ![](cplotting-images/plot3D.png) <br> **`cplt.complex_plot3D(x, y, f, log_mode=True)`**
![](cplotting-images/re_im.png) <br> **`cplt.plot_re_im(x, y, f, cmap="twilight", contour=False, alpha=0.9)`** |  ![](cplotting-images/re_im_contour.png) <br> **`cplt.plot_re_im(x, y, f, cmap="twilight", contour=True, alpha=0.9)`**
![](cplotting-images/streamplot.png) <br> **`cplt.complex_streamplot(x, y, f, mod_as_linewidths=False, cmap="twilight_r", density=2, scatterpoints=pts)`** |  ![](cplotting-images/streamplot_modulus_lines.png) <br> **`cplt.complex_streamplot(x, y, f, mod_as_linewidths=True, cmap="twilight_r", density=2, scatterpoints=pts)`**
![](cplotting-images/real_contour.png) <br> **`cplt.complex_contour(x, y, f, mode="real", levels=np.arange(0,21,1), lw=2, cmap="coolwarm", scatterpoints=pts)`** |  ![](cplotting-images/imag_contour.png) <br> **`cplt.complex_contour(x, y, f, mode="imag", levels=np.arange(0,21,1), lw=2, cmap="coolwarm", scatterpoints=pts)`**
![](cplotting-images/mod_contour.png) <br> **`cplt.complex_contour(x, y, f, mode="modulus", levels=np.arange(0,21,1), lw=2, cmap="coolwarm", scatterpoints=pts)`** |  ![](cplotting-images/both_contour.png) <br> **`cplt.complex_contour(x, y, f, mode="both", levels=np.arange(0,21,1), lw=2, cmap="coolwarm", scatterpoints=pts)`**
      
     
### Examples 2 

In this second set of examples the test function is:

$$
f(z)=\cos z
$$

As we did in the first set of examples, we start defining the variables, the parameters and the function:

```python
N = 40
lim = 6
x, y = np.meshgrid(np.linspace(-lim,lim,N), 
                    np.linspace(-lim,lim,N))
z = x + 1j*y
f = np.cos(z)
```
Then, we could obtain the following plots:

![](cplotting-images/vector_cos.png) <br> `cplt.complex_vector_field(x, y, f, norm=False)`  |  ![](cplotting-images/vector_cmap_cos.png) <br> `cplt.complex_vector_field(x, y, f, cmap="hsv", norm=False)`
| :-------------: | :-------------: |
![](cplotting-images/vector_normalized_cos.png) <br> **`cplt.complex_vector_field(x, y, f, norm=True)`** |  ![](cplotting-images/vector_cmap_normalized_cos.png) <br> **`cplt.complex_vector_field(x, y, f, cmap="hsv", norm=True)`**

<br>

---

If you are a beginner with complex functions you might also find useful: ["Plotting Complex Variable Functions"](https://artmenlope.github.io/plotting-complex-variable-functions/).

I would also like to recommend an online interactive book by Juan Carlos Ponce Campuzano called ["COMPLEX ANALYSIS - A Visual and Interactive Introduction"](https://complex-analysis.com/).

