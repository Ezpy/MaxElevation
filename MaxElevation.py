# -*- coding: utf-8 -*-

import simplejson
import urllib
import pylab
import gps

ELEVATION_BASE_URL = 'https://maps.googleapis.com/maps/api/elevation/json'

def DrawPlot(x,y):
    pylab.plot(x,y)
    pylab.show()

def getElevation(path,samples,startgps,**elvtn_args):
    elvtn_args.update({
        'path': path,
        'samples': samples,
        # If you do not have api key, comment this part out.
        'key': MY_KEY
      })
    url = ELEVATION_BASE_URL + '?' + urllib.urlencode(elvtn_args)
    response = simplejson.load(urllib.urlopen(url))
    
    startlat = float(startgps[0])
    startlon = float(startgps[1])
    startalt = float(startgps[2])*0.001
    
    start_xyz = gps.geodetic2ecef(startlat,startlon,startalt)

    max_theta = -180
    max_el_point = ()
    
    first = True

    for resultset in response['results']:
        if first == False:
            lat = resultset['location']['lat']
            lon = resultset['location']['lng']
            alt = resultset['elevation']*0.001
    
            x, y, z = gps.geodetic2ecef(lat,lon,alt)
            
            theta = gps.V_Multi(start_xyz, (x,y,z))
            
            if theta > max_theta:
                max_theta = theta
                max_el_point = (lat,lon,alt)
        else:
            first = False
                
    return max_el_point, max_theta

if __name__ == '__main__':
    startlat = raw_input('First Point Latitude: ').strip()
    startlon = raw_input('First Point Longitude: ').strip()
    startalt = raw_input('First Point Altitude(m): ').strip()
    
    deg = float(raw_input('Start Deg: ').strip())
    EndDeg = float(raw_input('End Deg: ').strip())
    DegDelta = float(raw_input('Deg delta: ').strip())
    
    if raw_input('Save as csv ? (y/n): ').strip().lower() == 'y':
        SaveThis = True
    else:
        SaveThis = False
    
    # For drawing graph
    deg_list = []
    ele_list = []
    
    if SaveThis:
        w = open('MaxElevation.csv', 'w')
    
    while deg < EndDeg:
        # 200 km away from the first point
        endlat, endlon = gps.NextPoint(float(startlat),float(startlon),deg,200)
    
        startStr = "%s,%s" % (startlat.strip(), startlon.strip())
        endStr = "%s,%s" % (str(endlat).strip(), str(endlon).strip())
    
        pathStr = startStr + "|" + endStr

        a = getElevation(pathStr,500,(startlat,startlon,startalt))
        
        print '%s,%s,%s,%s,%s' % (str(deg), str(a[0][0]), str(a[0][1]), str(a[0][2]), str(a[1]))
        
        if SaveThis:        
            w.write('%s,%s,%s,%s,%s\n' % (str(deg), str(a[0][0]), str(a[0][1]), str(a[0][2]), str(a[1])))

        deg_list.append(deg)
        ele_list.append(a[1])
        deg += DegDelta
        
    if SaveThis:
        w.close()
    DrawPlot(deg_list, ele_list)