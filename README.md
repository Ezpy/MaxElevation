# MaxElevation
Calculate max elevation around the given place

[Requirement]
- simplejson python library
- pylab python library
- scipy python library
- internet to access google map api

[Procedure]
- Get a point A (latitude, longitude, altitude)
- From a to b degrees, get B (latitude, longitude) which is 200km far away from given point.
- Get 200 samples (latitude,longitude,altitude) from A to B.
- Calculate elevation for A to each samples above and get a maximum value.
- Save each maximum elevation value and its latitude and longitude.

[Screenshot]

![alt tag](https://github.com/Ezpy/MaxElevation/blob/master/Screenshot.png)
