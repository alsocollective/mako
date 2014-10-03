import matplotlib.pyplot as plt
import matplotlib, pylab
import numpy as np
import netCDF4
import datetime
import scipy.ndimage as ndimage
import os, errno
import simplejson as json
import matplotlib.colors as col

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

class cl:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

utc = datetime.datetime.utcnow() 
gmt = utc.strftime("%Y")

lakes = ["ontario","huron","erie","superior","michigan"]

# for num in lakes:

# 	#### These should be functions!

# 	doy = datetime.datetime.now().timetuple().tm_yday

# 	if gmt < 12:
# 		filename = (num[0]+""+utc.strftime("%Y")+"%d"%doy+"00.out1.nc")
# 		furl = "https://tds.glos.us/thredds/dodsC/glos/glcfs/"+num+"/fcfmrc-2d/files/"+filename

# 	elif gmt > 12:
# 		filename = (num[0]+""+utc.strftime("%Y")+"%d"%doy+"12.out1.nc")
# 		furl = "https://tds.glos.us/thredds/dodsC/glos/glcfs/"+num+"/fcfmrc-2d/files/"+filename

#FORECAST - TestData
#url = "../../testdata/tds.glos.us/thredds/dodsC/glos/glcfs/ontario/fcfmrc-2d/files/o201425012.out1.nc"

url = "http://tds.glos.us/thredds/dodsC/glos/glcfs/superior/fcfmrc-2d/files/s201426312.out1.nc"

#NOWCAST - TestData
#url = "../../testdata/tds.glos.us/thredds/dodsC/glos/glcfs/archivecurrent/ontario/ncfmrc-2d/files/o201425018.out1.nc"

try:
	nc = netCDF4.Dataset(url)
	print cl.OKGREEN+"--------\nSuccess!\n--------"+cl.ENDC

except RuntimeError:
	print cl.FAIL+"--------------\nFile not found\n--------------"+cl.ENDC

dayof = nc.validtime_DOY.split(",")
dayof = int(dayof[0])

mkdir_p("../output/ontario/%d"%dayof)
glosJson = open("../output/ontario/%d"%dayof+"/o-%d.json"%dayof,"w")

G_x = nc.variables['lon']
G_y = nc.variables['lat']
G_z = nc.variables['wvh']
G_time = nc.variables['time']

G = {} # dictionary ~ Matlab struct
G['x'] = G_x[:].squeeze()
G['y'] = G_y[:].squeeze()
G['z'] = G_z[:1,:,:].squeeze() # download only one temporal slice
G['t'] = G_time[:].squeeze()

nc.close()

#high = nf(np.amax(G['z']))
#print high

#G['z'] = ndimage.gaussian_filter(np.ma.masked_invalid(G['z']),sigma=0.25, order=0,mode="constant",cval=0.5)

counter = 0

# make image
#plt.figure(figsize=(10,10))
plt.imshow(G['z'],origin='lower') 
#plt.title(nc.title)
plt.savefig('image.png', bbox_inches=0)

exit()
