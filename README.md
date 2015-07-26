# MaxElevation
Calculate max elevation around the given place

[Requirement]
- simplejson python library
- pylab python library
- scipy python library
- internet to access google map api

[Procedure]
1. Get a point (latitude, longitude, altitude)
2. From a to b degrees, get another point which is 200km far away from given point.
3. Get altitude from given point to calculated point. (outputs 200 samples)
4. Calculate elevation and get a maximum value.
5. Save each maximum elevation value and its latitude and longitude.

[Screenshot]

![alt tag](https://github.com/Ezpy/MaxElevation/blob/master/Screenshot.png)
