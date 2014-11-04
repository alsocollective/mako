

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
# import pygrib

# Multithreading would be a good bet when collecting data

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

	print nc.variables['x']
	print x
	print len(x)
	print x[0]
	print y[0]

	print (x[0])-(x[1])

	nam12km = pyproj.Proj("+proj=lcc +lat_1=20 +lat_2=60 +lat_0=40 +lon_0=-96 +x_0=0 +y_0=0 +ellps=GRS80 +datum=NAD83 +units=m +no_defs")

	# print z
	# print "----"
	# print len(z[0][410])


	#print z[0][410]

	# for dap in z:

	# 	print dap

	# 	print len(dap)

		

	# 	counter = counter + 1

	# print z[0][]

	


	#z = 0.01*nc.variables['Pressure_reduced_to_MSL'][0]

	dictData['x'] = x[500:502]
	dictData['y'] = y[400:402]
	dictData['z'] = z[:,400:402,500:502]

	print dictData['z'][0][0]
	print dictData['x'][0]
	print dictData['y'][0]

	exit()

	dictData['y'] = y[:80]

	exit()

	print dictData['y'][0]

	exit()

	dictData['z'] = z[:,:80,:80]

	dictData['z'] = ndimage.gaussian_filter(np.ma.masked_invalid(dictData['z']),sigma=0.0005, order=0, mode="nearest", cval=0.05)

	nc.close()

	return dictData



def completeLakes(x,y,z):

	print "Pressure is on..."


	fig = plt.figure(frameon=False)

	cs = fig.add_subplot(111)

	#clevs = np.arange(0.0, 5, 0.3048)
	#norm = col.BoundaryNorm(clevs, 256)

	#clevs = np.arange(-10000,11000.,100)


	cs.contour(x,y,z[0],cmap='jet')

	#plt.axis('off')

	plt.show()

	print cl.OKGREEN+"--------\nDone.\n--------"+cl.ENDC


data = getData()

# # LAKE , DAY, HOUR
# ont = getData("ontario","290","12")
# sup = getData("superior","290","12")
# hur = getData("huron","290","12")
# eri = getData("erie","290","12")
# mic = getData("michigan","290","12")


completeLakes(data['x'],data['y'],data['z'])


# lakes = [ont,sup,hur,eri,mic]

# for num in lakes:

# 	print "Writing Single Lakes..."

# 	singleLake(num)


exit()

# from mpl_toolkits.basemap import Basemap
# import numpy as np
# import matplotlib.pyplot as plt


# #http://nbviewer.ipython.org/github/scollis/tds-python-workshop/blob/master/pydap.ipynb

# ##################
# # Projection fun #
# ##################

# # get basic info from the file regarding projection attributes
# # see the following for more info on projections as described here:
# #   http://www.nco.ncep.noaa.gov/pmb/docs/on388/tableb.html#GRID218
# #   http://www.wmo.int/pages/prog/www/WDM/Guides/Guide-binary-2.html [see LAMBERT CONFORMAL SECANT OR TANGENT CONE GRIDS]
# #   http://www.unidata.ucar.edu/mailing_lists/archives/netcdf-java/2006/msg00006.html [starndard parallels in CDM]
# proj_attributes = dataset['LambertConformal_Projection'].attributes
# rsphere = proj_attributes['earth_radius']
# # lat_0	: center of desired map domain (in degrees) [Basemap]
# # CDM : 'latitude_of_projection_origin'
# # NCO : where Dx and Dy are defined
# # :
# lat_0 = proj_attributes['latitude_of_projection_origin']
# # lon_0	: center of desired map domain (in degrees) [Basemap]
# # CDM : 'longitude_of_central_meridian'
# # NCO : Lov
# #
# # Lov - The orientation of the grid; i.e., the east longitude value
# # of the meridian which is parallel to the y-axis (or columns of the
# #  grid) along which latitude increases as the y-coordinate increases.
# # (Note: The orientation longitude may, or may not, appear within a
# # particular grid.)
# #
# lon_0 = proj_attributes['longitude_of_central_meridian'] # Lov
# # lat_1, lat_2 : 1st and second parallels [Basemap]
# # CDM : 'standard_parallel' - this attr contains both 1st and 2nd
# # NCO : ??? Not sure where this shows up on the nco page
# lat_1 = proj_attributes['standard_parallel']
# # on nco page, lat_1 and lat_2 are actually the lower left corner
# # lat/lon
# # from nco page
# #   lat_1= 12.190
# #   lon_1 = 226.514 #typo on page - should be 226.541
# # So, on nco page, lat_1, lon_1 are the llcrnrlat and llcrnrlon in Basemap.
# #
# llcrnrlat = 12.190 # (1,1)
# llcrnrlon = 360-133.459 # (1,1)
# # these are taken from the nco page
# urcrnrlat = 57.328 # (614,428)
# urcrnrlon = 360-49.420 # (614,248)

# print('...download the data\n')

# # download and x and y coords and convert them from
# # km to m, offset for use in basemap
# x = dataset['x'][:]
# x = x * 1000
# x = x + abs(x.min())
# y = dataset['y'][:]
# y = y * 1000
# y = y + abs(y.min())

# width = x.max() - x.min()
# height = y.max() - y.min()

# # actually download the pressure data (first time step only)
# # and convert from pascals to mb
# mslp = dataset['Pressure_reduced_to_MSL_msl'].array[0,:,:] / 100.
# mslp = mslp.squeeze()
# # note: if we try to plot all of the barbs, things will get
# # very, very ugly! So, we must subset! Let's find the info
# # we need to create the subset
# x_sz = x.shape[0]
# y_sz = y.shape[0]
# stride_x = 25
# stride_y = 25
# # create a 2d array of x and y
# x_sub = x[0:x_sz:stride_x]
# y_sub = y[0:y_sz:stride_y]
# x1, y1 = np.meshgrid(x_sub, y_sub)

# # download only a subset of the u and v dataset (again, first
# # time step, and first level [10 m])
# u = dataset['u-component_of_wind_height_above_ground'].array[0,0,
#     0:y_sz:stride_y,
#     0:x_sz:stride_x]
# u = u.squeeze()

# v = dataset['v-component_of_wind_height_above_ground'].array[0,0,
#     0:y_sz:stride_y,
#     0:x_sz:stride_x]
# v = v.squeeze()

# print("next!")

# # create basemap, get lat lon of x,y min, x,y, max, then
# # create new basemap with those as the llcrnlon, etc..
# #m = Basemap(projection='lcc', lat_0 = lat_0, lon_0 = lon_0,
# #          width = width, height = height,
# #          area_thresh = 1000., rsphere = rsphere)

# #llcrnrlon, llcrnrlat = m(x.min(), y.min(), inverse=True)
# #urcrnrlon, urcrnrlat = m(x.max(), y.max(), inverse=True)

# #print m(360-133.459, 12.190)
# #print x.min(), y.min()

# # setup the basic map to be used for our plot

# fig = plt.figure(figsize=(11,8))
# fig.subplots_adjust(left = 0.05, right = 0.88)
# ax1 = fig.add_subplot(1,1,1)

# map = Basemap(projection='lcc', lat_0 = lat_0, lon_0 = lon_0,
#               #lat_1 = lat_1, #lon_1 = lon_1,
#               llcrnrlon = llcrnrlon, llcrnrlat = llcrnrlat,
#               urcrnrlat = urcrnrlat, urcrnrlon = urcrnrlon,
#               area_thresh = 1000., rsphere = rsphere, resolution='i')
# # draw coastlines, country boundaries. and states
# map.drawcoastlines()
# map.drawcountries()
# map.drawstates()
# # draw the edge of the map projection region (the projection limb)
# map.drawmapboundary()
# # draw lat/lon grid lines every 30 degrees.
# map.drawmeridians(np.arange(0, 360, 30))
# map.drawparallels(np.arange(-90, 90, 30))
# print('...plot Pressure at MSL\n')
# # render the 2d color plot of pressure at MSL
# map.pcolormesh(x, y, mslp)

# #print('...plot 10m wind barbs (knots)\n')
# # plot wind barbs - note we must subset x1, y1 to match
# # shape of u and v
# map.barbs(x1, y1, u, v)

# # plot the colorbar and give it a label
# cb = map.colorbar()
# cb.set_label("Pressure reduced to MSL (mb)", fontsize=16)

# # set the title
# ax1.set_title("NAM CONUS 12km {} {}Z Initialization".format(data_url.split('_')[-2],
#                                              data_url.split('_')[-1][0:2]))
