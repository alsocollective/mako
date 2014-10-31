

import matplotlib.pyplot as plt
import matplotlib, pylab
import numpy as np
import netCDF4
import datetime
import scipy.ndimage as ndimage
import os, errno
import simplejson as json
import matplotlib.colors as col

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

	url = "http://nomads.ncdc.noaa.gov/thredds/dodsC/nam218/201410/20141030/nam_218_20141030_0000_084.grb"

	#url = "http://dods.ndbc.noaa.gov/thredds/dodsC/data/stdmet/45003/45003h2014.nc"

	#LOCAL
	# url = "https://noaa-data/"+lake[0]+"2014"+day+hour+".out1.nc"

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
	z = nc.variables['Pressure_surface']


	#z = 0.01*nc.variables['Pressure_reduced_to_MSL'][0]

	dictData['x'] = x[:80]
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
