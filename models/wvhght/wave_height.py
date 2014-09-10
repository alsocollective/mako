import matplotlib.pyplot as plt
import matplotlib, pylab
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.ticker as ticker
import matplotlib.colors as mcolors
import netCDF4
#import pydap
import datetime
import scipy.ndimage as ndimage

def nf(value):
	feet = value*3.28084
	return int(feet)

class cl:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# open a local NetCDF file or remote OPeNDAP URL
#url = 'http://tds.glos.us/thredds/dodsC/glos/glcfs/erie/fcfmrc-2d/files/e201400100.out1.nc'
#url = 'http://tds.glos.us/thredds/dodsC/glos/glcfs/huron/fcfmrc-2d/files/h201422712.out1.nc'

utc = datetime.datetime.utcnow() 
gmt = utc.strftime("%Y")

lakes = ["ontario","huron","erie","superior","michigan"]

for num in lakes:

	print num


# exit()

doy = datetime.datetime.now().timetuple().tm_yday

if gmt < 12:

	filename = ("h"+""+utc.strftime("%Y")+"%d"%doy+"00.out1.nc")
	lake = "huron"

elif gmt > 12:

	filename = ("h"+""+utc.strftime("%Y")+"%d"%doy+"12.out1.nc")
	lake = "huron"

#url = "http://tds.glos.us/thredds/dodsC/glos/glcfs/"+lake+"/fcfmrc-2d/files/"+filename

#FORECAST
#url = "http://tds.glos.us/thredds/dodsC/glos/glcfs/huron/fcfmrc-2d/files/h201425212.out1.nc"

#NOWCAST
url = "http://tds.glos.us/thredds/dodsC/glos/glcfs/archivecurrent/huron/ncfmrc-2d/files/h201425306.out1.nc"

# Forecast
# A201423212.out1.nc
# A, 2014, 232, 12
# lake, Y, DOY(Julian), H(GMT), .out?, Dimensions .nc (extension)

try:
	nc = netCDF4.Dataset(url)

	print cl.OKGREEN+"Success!"+cl.ENDC

except RuntimeError:

	print cl.FAIL+"---------------"
	print "File not found"
	print "---------------"+cl.ENDC

	print "Pooling for previous model"




# print nc.variables.keys()
# print '----'
#print len(nc.variables['time']),"hours" #120 hours returns UNIX Timestamp format

#print(cl.OKBLUE+datetime.datetime.fromtimestamp(int(nc.variables['time'][0])).strftime('%Y-%m-%d %H:%M:%S')+cl.ENDC + " - " + cl.OKGREEN+datetime.datetime.fromtimestamp(int(nc.variables['time'][119])).strftime('%Y-%m-%d %H:%M:%S')+cl.ENDC)

print nc.variables.keys()

print nc.variables['time'][0]

G_x = nc.variables['lon']
G_y = nc.variables['lat']
G_z = nc.variables['wvh']
G_time = nc.variables['time']

#OR THIS!
#G_z = ndimage.gaussian_filter(nc.variables['wvh'],sigma=0.25, order=0, mode="constant",cval=0.5)

G = {} # dictionary ~ Matlab struct
G['x'] = G_x[:].squeeze()
G['y'] = G_y[:].squeeze()
G['z'] = G_z[:,:,:].squeeze() # download only one temporal slice
 
# represent fillValue from data as Masked Array
# the next release of netcdf4 will return a masked array by default, handling NaNs
# correctly too (http://code.google.com/p/netcdf4-python/issues/detail?id=168)

#G['z'] = np.ma.masked_invalid(G['z'])

# OR THIS!!!!
G['z'] = ndimage.gaussian_filter(np.ma.masked_invalid(G['z']),sigma=0.25, order=0,mode="constant",cval=0.5)

sigHeight = nf(np.amax(G['z']))
print sigHeight

nc.close()

counter = 0

for dat in G['z']:

	topo = dat

	# make image
	# plt.figure(figsize=(10,10))
	# plt.imshow(topo,origin='lower')
	# plt.title(nc.title)
	# plt.savefig('../Output2/image%d.png'%counter, bbox_inches=0)
	fig = plt.figure(frameon=False)

	print datetime.datetime.fromtimestamp(G_time['time'][counter]).strftime('%Y-%m-%d %H:%M:%S')

	clevs = np.arange(0.0, 20, 0.25)	

	cs = plt.contourf(G['x'],G['y'],topo,clevs,cmp='jet')
	#plt.contourf(G['x'],G['y'],topo,origin='lower')

	cs.levels = [nf(val) for val in cs.levels]

	# plot SLP contours
	# cs = plt.contourf(G['x'],G['y'],topo,clevs,linewidths=1,cmp='jet')
	
	#CS2 = plt.contourf(G['x'],G['y'],topo,cmap='jet')
	
	#plt.clabel(cs, cs.levels, inline=1, fontsize=5)
	#plt.axis('tight')
	plt.axis('equal')
	plt.axis('off')
	fig.savefig('../output/nowcast/waves-%d-hrs.svg'%counter,bbox_inches='tight')

	plt.close()

	counter += 1

exit()
