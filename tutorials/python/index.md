---
layout: page-no-title
title: Python
---

<header class="post-header">
    <h1 class="post-title" style="text-align:center"><i class="fab fa-python fa-fw fa-lg fa-notbold svv"></i>{{ page.title | escape }}</h1>
</header>

Python is a great language for scientific computing, most of the programming done by our group is in python. We provide below some links for learning this language, and below we offer many python code examples. You are invited to download these codes, tweak with them, break them, hack them as you wish!


Most codes focus on plotting, but other algorithms such as numerical integration and Fourier transforms can also be found. 

Some useful links for learning python:

* <a href="http://nbviewer.jupyter.org/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.ipynb" target="_blank">Python Data Science Handbook</a>
* <a href="https://learnpythonthehardway.org/book/" target="_blank">Learn Python the Hard Way</a>
* <a href="http://nbviewer.jupyter.org/gist/rpmuller/5920182" target="_blank">A Crash Course in Python for Scientists</a>
* <a href="http://swcarpentry.github.io/python-novice-inflammation/" target="_blank">Software Carpentry</a>
* <a href="http://matthiaseisen.com/fwl/py/" target="_blank">Fun with Lists</a>
* <a href="https://www.codecademy.com/learn/python" target="_blank">Python | Codecademy</a>
* <a href="http://www.scipy-lectures.org/index.html" target="_blank">Scipy Lecture Notes</a>
* <a href="https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks" target="_blank">A gallery of interesting IPython Notebooks</a>
* <a href="http://greenteapress.com/thinkpython/html/index.html" target="_blank">Think Python: How to Think Like a Computer Scientist</a>  

This might be overwhelming, so I suggest you to follow this:
{% twitter https://twitter.com/jakevdp/status/906901174728536066 %}

Start by downloading <a href="https://www.anaconda.com/distribution/" target="_blank">Anaconda</a>, a package manager application that will help you get started with python in all platforms.
​
Make sure you are acquainted with ipython (interactive python, <a href="https://www.pythonanywhere.com/try-ipython/" target="_blank">try it here</a>), and with <a href="http://jupyter.org/" target="_blank">Jupyter notebook</a>.
​
I recommend <a href="https://www.sublimetext.com/" target="_blank">Sublime Text</a> for writing code, and you can install the Anaconda package to it to have a smooth IDE. [not the same anaconda as mentioned above! Yes, it's confusing, I know.]

**************************************************

## Fitzhugh-Nagumo --- Labyrinthine Patterns

<a href="http://nbviewer.jupyter.org/urls/bitbucket.org/yairmau/notebooks/raw/master/fhn_spectral.ipynb" class="button" target="_blank">Jupyter notebook</a>

Main features:
how to make a movie, time-integration methods (semi-spectral and Euler)

<iframe width="560" height="315" src="https://www.youtube.com/embed/5au-G5FuI_A" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**************************************************

## Conway's Game of Life, acorn initial condition

<a href="http://nbviewer.jupyter.org/urls/bitbucket.org/yairmau/notebooks/raw/master/life.ipynb" class="button" target="_blank">Jupyter notebook</a>

This is a (slightly) modified version of <a href="https://glowingpython.blogspot.co.il/2015/10/game-of-life-with-python.html" target="_blank">Glowing Python</a>'s code. I make it available here because it features a few nice things:

* how to make a movie using matplotlib.animation
* how to write a generator (function with yield)
* how to plot a sparce array (spy)  

Main features:
`matplotlib.animation, yield, with, matplotlib.pyplot.spy`

<iframe width="560" height="315" src="https://www.youtube.com/embed/lelsVltLZe4?rel=0" frameborder="0" allowfullscreen></iframe>

**************************************************

## Least squares fit of nonlinear function
<a href="http://nbviewer.jupyter.org/urls/bitbucket.org/yairmau/notebooks/raw/master/least-squares.ipynb" class="button" target="_blank">Jupyter notebook</a>

Main features:
`LaTeX text, scipy.optimize.curve_fit, matplotlib.patches`  
![](http://www.bitbucket.org/yairmau/notebooks/raw/master/figures/least-squares.png)

**************************************************

## Fun with histograms
<a href="http://nbviewer.jupyter.org/urls/bitbucket.org/yairmau/notebooks/raw/master/histogram.ipynb" class="button" target="_blank">Jupyter notebook</a>  

Main features:
`np.histogram, plt.hist, plt.bar, plt.barh, gridspec, least squares fit of nonlinear function, plt.hist2d`  
![](http://www.bitbucket.org/yairmau/notebooks/raw/master/figures/histogram.png)

**************************************************

## Fancy subplot grid

<a href="http://nbviewer.jupyter.org/urls/bitbucket.org/yairmau/notebooks/raw/master/subplot-grid.ipynb" class="button" target="_blank">Jupyter notebook</a>

Highly customizable subplot structure. Also, figure contains several axis configurations and labeling options.  
Main features:
`gridspec subplots; numpy-compatible heaviside; label, ticks and axis manipulations; log scale`
![](http://www.bitbucket.org/yairmau/notebooks/raw/master/figures/subplot-grid.png)

**************************************************

## Streamplot

<a href="http://nbviewer.ipython.org/urls/bitbucket.org/yairmau/notebooks/raw/master/linear-system.ipynb" class="button" target="_blank">Jupyter notebook</a>

Streamplot of a two-dimensional linear system, with eigenvectors and nullclines. Python shows LaTeX equations beautifully.  
Main features:
`meshgrid, streamplot, contour, legend, LaTeX`
![](http://www.bitbucket.org/yairmau/notebooks/raw/master/figures/linear-system.png)

**************************************************

## The time dependent Ginzburg-Landau equation

<a href="http://nbviewer.jupyter.org/urls/bitbucket.org/yairmau/notebooks/raw/master/tdgle.ipynb" class="button" target="_blank">Jupyter notebook</a>

Numerical integration of a parabolic partial differential equation, using finite differences: Euler step to advance time, and a 5-point stencil to approximate the Laplacian.  
Main features:
`imshow, colorbar, set_data`

<iframe width="560" height="315" src="https://www.youtube.com/embed/JgE9Px7zsQE" frameborder="0" allowfullscreen></iframe>

**************************************************

## The double pendulum

<a href="http://nbviewer.jupyter.org/urls/bitbucket.org/yairmau/notebooks/raw/master/double-pendulum.ipynb" class="button" target="_blank">Jupyter notebook</a>

Numerical integration of the equations of motion of the double pendulum. This time, scipy's ode itegrator was used. Nice example of how to make a movie.  
Main features:
`scipy.integrate.ode, set_data, set_aspect('equal'), remove plot, movie`

<iframe width="560" height="315" src="https://www.youtube.com/embed/-76LN_Kph7A" frameborder="0" allowfullscreen></iframe>

**************************************************

## The Hilbert curve

<a href="http://nbviewer.jupyter.org/urls/bitbucket.org/yairmau/notebooks/raw/master/hilbert-curve.ipynb" class="button" target="_blank">Jupyter notebook</a>

Construction of the Hilbert curve as a Lindenmayer system (L-system).  
Main features:
`string operations, movie`

<iframe width="560" height="315" src="https://www.youtube.com/embed/Oudyl56GPJU" frameborder="0" allowfullscreen></iframe>


**************************************************

## A hysteresis mechanism

<a href="http://nbviewer.jupyter.org/urls/bitbucket.org/yairmau/notebooks/raw/master/hysteresis.ipynb" class="button" target="_blank">Jupyter notebook</a>

Hysteresis mechanism created by the bistability of states. System goes to minimum points u in the energy functional $f=u^4-2u^2+hu$. The parameter $h$ is ramped down and up during this simulation.  
Main features:
`sympy analytical calculations, numpy dtypes, movie`

<iframe width="560" height="315" src="https://www.youtube.com/embed/xgRDhOifFow" frameborder="0" allowfullscreen></iframe>

**************************************************

## Contour plot

<a href="http://nbviewer.ipython.org/urls/bitbucket.org/yairmau/notebooks/raw/master/contours.ipynb" class="button" target="_blank">Jupyter notebook</a>

Contour plot with many customizable options. Also, a nice way to truncate a colormap so it gives the color range that you want.  
Main features:
`truncate_colormap, contour, contourf (fill), clabel (contour label)`

![](http://www.bitbucket.org/yairmau/notebooks/raw/master/figures/cont.png)

**************************************************

## Drowning person problem

<a href="http://nbviewer.ipython.org/urls/bitbucket.org/yairmau/notebooks/raw/master/sea-sand.ipynb" class="button" target="_blank">Jupyter notebook</a>

How should ​lifeguard run in order to save a drowning person in minimal time? Answer: by using Snell's law of refraction!  
This is a nice example how to use spines (x and y axis form a cross), instead of rectangular figures as usual. Also, "annotations" are used, where things can be labeled with the help of arrows.  
Main features:
`spines, matplotlib.patches.Rectangle, annotate`

![](http://www.bitbucket.org/yairmau/notebooks/raw/master/figures/sea-sand.png)

**************************************************

## This website's logo

<a href="http://nbviewer.ipython.org/urls/bitbucket.org/yairmau/notebooks/raw/master/website-logo.ipynb" class="button" target="_blank">Jupyter notebook</a>

Simple example of how to make a figure without any visible axes.  
Main features:
`set_axis_off, fill_between, matplotlib inline plot on Jupyter`

![](http://www.bitbucket.org/yairmau/notebooks/raw/master/figures/site-logo.png)

**************************************************

## Bars

<a href="http://nbviewer.ipython.org/urls/bitbucket.org/yairmau/notebooks/raw/master/bars.ipynb" class="button" target="_blank">Jupyter notebook</a>

Horizontal and vertical bars, with numeric legends. Unicode support.  
Main features:
`unicode, bar, barh, grid`

![](http://www.bitbucket.org/yairmau/notebooks/raw/master/figures/bars.png)

