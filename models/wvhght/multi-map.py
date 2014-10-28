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

utc = datetime.datetime.utcnow() 
gmt = utc.strftime("%Y")



# FUNCTIONS

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def nf(value):
	feet = value*3.28084
	return int(feet)

def getData(lakeName, dayOfYear, hourGMT):

	url = "https://tds.glos.us/thredds/dodsC/glos/glcfs/%s/fcfmrc-2d/files/%s2014%s%s.out1.nc"%(lakeName,lakeName[0],dayOfYear,hourGMT)

	#url = "https://noaa-data/"+lake[0]+"2014"+day+hour+".out1.nc"

	dictData = {}

	try:
		#Use NetCDF 4 to download the dataset into memory
		nc = netCDF4.Dataset(url)
		print cl.OKGREEN+"-------------------\n"+lakeName+" Success!\n-------------------"+cl.ENDC

	except RuntimeError:
		print cl.FAIL+"--------------\nFile not found\n--------------"+cl.ENDC


	#Retrieve specific variable from dataset
	x = nc.variables['lon']
	y = nc.variables['lat']
	z = nc.variables['wvh']
	t = nc.variables['time']

	dictData['x'] = x[:].squeeze()
	dictData['y'] = y[:].squeeze()
	dictData['z'] = z[:,:,:].squeeze()
	dictData['t'] = t[:].squeeze()

	dictData['z'] = ndimage.gaussian_filter(np.ma.masked_invalid(dictData['z']),sigma=0.0005, order=0, mode="nearest", cval=0.05)

	nc.close()

	return dictData


def completeLakes(ont,sup,hur,eri,mic):

	counter = 0

	print "Writing Combined Lakes..."

	for topo in ont['z']:

		fig = plt.figure(frameon=False)

		cs = fig.add_subplot(111)

		clevs = np.arange(0.0, 5, 0.3048)
		norm = col.BoundaryNorm(clevs, 256)

		cs.contourf(ont['x'],ont['y'],ont['z'][counter],clevs,cmap='jet',norm=norm, vmin=0, vmax=9.14400)
		cs.contourf(sup['x'],sup['y'],sup['z'][counter],clevs,cmap='jet',norm=norm, vmin=0, vmax=9.14400)
		cs.contourf(hur['x'],hur['y'],hur['z'][counter],clevs,cmap='jet',norm=norm, vmin=0, vmax=9.14400)
		cs.contourf(eri['x'],eri['y'],eri['z'][counter],clevs,cmap='jet',norm=norm, vmin=0, vmax=9.14400)
		cs.contourf(mic['x'],mic['y'],mic['z'][counter],clevs,cmap='jet',norm=norm, vmin=0, vmax=9.14400)

		plt.axis('off')

		#cs.set_clim([0, 5])

		wvhModel = "%d-tst.png"%counter

		fig.savefig('../output/ontario/'+wvhModel, bbox_inches='tight',transparent=True,pad_inches=0)

		print wvhModel

		plt.close()

		counter += 1

	print cl.OKGREEN+"--------\nDone.\n--------"+cl.ENDC


def singleLake(lake):

	print lake

	print "this was called but nothing happend"

	# Folders
	# Maybe a JSON
	# PNG needs to be optimized

	# get lake name
	# make lake folder




# LAKE , DAY, HOUR
ont = getData("ontario","290","12")
sup = getData("superior","290","12")
hur = getData("huron","290","12")
eri = getData("erie","290","12")
mic = getData("michigan","290","12")


completeLakes(ont,sup,hur,eri,mic)


# lakes = [ont,sup]

# for num in lakes:

#  	print "Writing Single Lakes..."

#  	singleLake(num)


exit()
