import matplotlib.pyplot as plt
import matplotlib, pylab
import numpy as np
import netCDF4
import datetime
import scipy.ndimage as ndimage
import os, errno
import simplejson as json
import matplotlib.colors as col
import pyproj
from pyproj import Proj
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt


class cl:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def getData():

	print cl.OKBLUE+"Getting Data..."+cl.ENDC

	#url = "http://nomads.ncdc.noaa.gov/thredds/dodsC/nam218/201410/20141030/nam_218_20141030_0000_084.grb"

	#url = "http://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_hd.pl?file=gfs.t18z.mastergrb2f00&var_GUST=on&var_V-GWD=on&subregion=&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.2014100118%2Fmaster"

	#url = "http://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs.2014103112/WAFS_blended_2014103112f36.grib2"

	url = "http://nomads.ncdc.noaa.gov/thredds/dodsC/nam218/201410/20141031/nam_218_20141031_0000_000.grb"


	dictData = {}

	try:
		#Use NetCDF 4 to download the dataset into memory
		nc = netCDF4.Dataset(url)
		print cl.OKGREEN+"--------\nSuccess!\n--------"+cl.ENDC

	except RuntimeError:
		print cl.FAIL+"--------------\nFile not found\n--------------"+cl.ENDC


	#Retrieve specific variable from dataset
	x = nc.variables['x']
	y = nc.variables['y']
	z = nc.variables['Surface_wind_gust']

	#proj_attributes = nc.variables['Lambert_Conformal']
	rsphere = nc.variables['Lambert_Conformal'].earth_radius
	lat_0 = nc.variables['Lambert_Conformal'].latitude_of_projection_origin
	lon_0 = nc.variables['Lambert_Conformal'].longitude_of_central_meridian
	lat_1 = nc.variables['Lambert_Conformal'].standard_parallel

	llcrnrlat = 12.190 # (1,1)
	llcrnrlon = 360-133.459 # (1,1)
	# these are taken from the nco page
	urcrnrlat = 57.328 # (614,428)
	urcrnrlon = 360-49.420 # (614,248)

	print rsphere

	map = Basemap(projection='lcc', lat_0 = lat_0, lon_0 = lon_0,
              #lat_1 = lat_1, #lon_1 = lon_1,
              llcrnrlon = llcrnrlon, llcrnrlat = llcrnrlat,
              urcrnrlat = urcrnrlat, urcrnrlon = urcrnrlon,
              area_thresh = 1000., rsphere = rsphere, resolution='i')
	# draw coastlines, country boundaries. and states
	map.drawcoastlines()
	map.drawcountries()
	map.drawstates()
	map.drawparallels(np.arange(-80.,81.,0.5))
	map.drawmeridians(np.arange(-180.,181.,12.190))
	map.drawmapboundary(fill_color='aqua')
	# draw tissot's indicatrix to show distortion.
	# ax = plt.gca()
	# for y in np.linspace(map.ymax/20,19*map.ymax/20,9):
	#     for x in np.linspace(map.xmax/20,19*map.xmax/20,12):
	#         lon, lat = map(x,y,inverse=True)
	#         poly = map.tissot(lon,lat,1.5,100,\
	#                         facecolor='green',zorder=10,alpha=0.5)
	


	#lat, lon = 43.566893, -79.298191
	lat, lon = 12.190, 133.459
	xpt,ypt = map(lon,lat)

	print "Length of X: %d"%(len(x))
	print "Total Width: %d km"%(12.190*len(x)) #Should be 7372km (but the earth is round) #Meridians 5009 km, 4960 km
	print "Total Width: %d m"%((12.190*len(x))*1000)

	print xpt
	print "====="
	print ypt

	lonpt, latpt = map(xpt,ypt,inverse=True)

	print "++++++"

	print lonpt
	print latpt

	# exit()

	map.plot(xpt,ypt,'bo')

	plt.title("Lambert Conformal Projection")
	plt.show()
		# exit()

	# # print nc.variables['x']
	# # print x
	# # print len(x)
	# # print x[0]
	# # print y[0]

	# # print (x[0])-(x[1])


	# # dictData['x'] = x[500:502]
	# # dictData['y'] = y[400:402]
	# # dictData['z'] = z[:,400:402,500:502]
	# dictData['info'] = rsphere

	# print dictData['info','earth_radius']

	# exit()

	# print dictData['z'][0][0]
	# print dictData['x'][0]
	# print dictData['y'][0]

	# exit()

	# dictData['y'] = y[:80]

	# exit()

	# print dictData['y'][0]

	# exit()

	# dictData['z'] = z[:,:80,:80]

	# dictData['z'] = ndimage.gaussian_filter(np.ma.masked_invalid(dictData['z']),sigma=0.0005, order=0, mode="nearest", cval=0.05)

	# nc.close()

	# return dictData


data = getData()

# exit()


# setup lambert conformal basemap.
# lat_1 is first standard parallel.
# lat_2 is second standard parallel (defaults to lat_1).
# lon_0,lat_0 is central point.
# rsphere=(6378137.00,6356752.3142) specifies WGS4 ellipsoid
# area_thresh=1000 means don't plot coastline features less
# than 1000 km^2 in area.
# m = Basemap(width=12000000,height=9000000,
#             rsphere=(6378137.00,6356752.3142),\
#             resolution='l',area_thresh=1000.,projection='lcc',\
#             lat_1=25.032,lat_2=55,lat_0=50,lon_0=-107.)
# m.drawcoastlines()
# m.fillcontinents(color='coral',lake_color='aqua')
# # draw parallels and meridians.
# m.drawparallels(np.arange(-80.,81.,20.))
# m.drawmeridians(np.arange(-180.,181.,20.))
# m.drawmapboundary(fill_color='aqua')
# # draw tissot's indicatrix to show distortion.
# ax = plt.gca()
# for y in np.linspace(m.ymax/20,19*m.ymax/20,9):
#     for x in np.linspace(m.xmax/20,19*m.xmax/20,12):
#         lon, lat = m(x,y,inverse=True)
#         poly = m.tissot(lon,lat,1.5,100,\
#                         facecolor='green',zorder=10,alpha=0.5)
# plt.title("Lambert Conformal Projection")
# plt.show()