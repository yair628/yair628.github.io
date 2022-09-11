---
layout: page-no-title-toc
title: Time Series Analysis
address: '[home](/)/[teaching](/teaching)/timeseries'
before: <span class="iconify svv" data-icon="bi:clock-history"></span>
toc: true
---

<!-- <header class="post-header">
    <h1 class="post-title" style="text-align:center"><span class="iconify" data-icon="whh:solarsystem" data-inline="false"></span>
{{ page.title | escape }}</h1>
</header> -->

## <span class="iconify" data-icon="healthicons:factory-worker"></span> In Construction

This course does not exist yet, but I already started uploading the course material, it's all very rough.  
Enjoy :)

### Basic time series analysis

<button class="my_button_small" onclick="window.open('https://yairmau.github.io/website/jupyter/2020/03/01/basic-tsa.html', '_blank');">Lecture</button>
Graphs, NaN, Missing data, Outliers, resampling, filling missing data, smoothing (moving average, SavGol).  
Data for this lecture: [file1](https://github.com/yairmau/website/tree/master/archive/timeseries/test_elad.csv), [file2](https://github.com/yairmau/website/tree/master/archive/timeseries/test_peleg.csv).

### Seasonal decomposition

Split a periodic time series into three components: `trend`, `seasonal` (periodic) and `residual` (all the rest!)

![](https://yairmau.github.io/website/archive/timeseries/seasonal-decomposition-CO2.png)

<button class="my_button_small" onclick="window.open('https://yairmau.github.io/website/jupyter/2020/03/01/seasonal-decomposition.html', '_blank');">Lecture</button>

### Convolution

![](https://yairmau.github.io/website/archive/timeseries/square_150.png)

Learn about running averages, how to smooth a curve, and what the heck a kernel is :)

<button class="my_button_small" onclick="window.open('https://yairmau.github.io/website/markdown/2022/09/08/convolution.html', '_blank');">Lecture</button>
