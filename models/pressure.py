

import matplotlib.pyplot as plt
import matplotlib, pylab
import numpy as np
import netCDF4
import datetime
import scipy.ndimage as ndimage
import os, errno
import simplejson as json
import matplotlib.colors as col
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

	counter = 0

	print z
	print "----"
	print len(z)

	for dap in z:

		print dap

		print len(dap)

		print dap[0]

		counter = counter + 1

	exit()


	#z = 0.01*nc.variables['Pressure_reduced_to_MSL'][0]

	dictData['x'] = x[160:180]
	dictData['y'] = y[:80]

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
