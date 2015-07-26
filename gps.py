# -*- coding: utf-8 -*-
from math import pow, degrees, radians, acos
from scipy import cos, sin, arctan, sqrt, arctan2

def geodetic2ecef(lat, lon, alt):
    # Constants defined by the World Geodetic System 1984 (WGS84)
    a = 6378.137
    esq = 6.69437999014 * 0.001

    """Convert geodetic coordinates to ECEF."""
    # altitude in kilo
    lat, lon = radians(lat), radians(lon)
    xi = sqrt(1 - esq * sin(lat)*sin(lat))
    x = (a / xi + alt) * cos(lat) * cos(lon)
    y = (a / xi + alt) * cos(lat) * sin(lon)
    z = (a / xi * (1 - esq) + alt) * sin(lat)
    return x, y, z
				
def ecef2geodetic(x, y, z):
    """Convert ECEF coordinates to geodetic.
    J. Zhu, "Conversion of Earth-centered Earth-fixed coordinates \
    to geodetic coordinates," IEEE Transactions on Aerospace and \
    Electronic Systems, vol. 30, pp. 957-961, 1994."""
    a = 6378.137
    b = 6356.7523142
    esq = 6.69437999014 * 0.001
    e1sq = 6.73949674228 * 0.001

    # return h in kilo
    r = sqrt(x * x + y * y)
    Esq = a * a - b * b
    F = 54 * b * b * z * z
    G = r * r + (1 - esq) * z * z - esq * Esq
    C = (esq * esq * F * r * r) / (pow(G, 3))
    S = sqrt(1 + C + sqrt(C * C + 2 * C))
    P = F / (3 * pow((S + 1 / S + 1), 2) * G * G)
    Q = sqrt(1 + 2 * esq * esq * P)
    r_0 =  -(P * esq * r) / (1 + Q) + sqrt(0.5 * a * a*(1 + 1.0 / Q) - \
        P * (1 - esq) * z * z / (Q * (1 + Q)) - 0.5 * P * r * r)
    U = sqrt(pow((r - esq * r_0), 2) + z * z)
    V = sqrt(pow((r - esq * r_0), 2) + (1 - esq) * z * z)
    Z_0 = b * b * z / (a * V)
    h = U * (1 - b * b / (a * V))
    lat = arctan((z + e1sq * Z_0) / r)
    lon = arctan2(y, x)
    return degrees(lat), degrees(lon), h

def NextPoint(lat,lon,theta,distance):
    import math
    theta = math.radians(theta)
    dx = distance*1000*math.sin(theta)
    dy = distance*1000*math.cos(theta)
    delta_longitude = dx / (111320*math.cos(math.radians(lat)))
    delta_latitude = dy / 110540
    return lat+delta_latitude, lon+delta_longitude
    
def V_Multi(m, n):
    x,y,z=(m[0],m[1],m[2])
    a,b,c=(n[0],n[1],n[2])
    
    p,q,r = (a-x,b-y,c-z)
    
    return 90-degrees(acos( (x*p+y*q+z*r)/ (sqrt(x**2+y**2+z**2)*sqrt(p**2+q**2+r**2))))