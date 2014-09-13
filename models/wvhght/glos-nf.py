import matplotlib.pyplot as plt
import matplotlib, pylab
import numpy as np
import netCDF4
import datetime
import scipy.ndimage as ndimage
import os, errno
import simplejson as json

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

url = "https://tds.glos.us/thredds/dodsC/glos/glcfs/huron/fcfmrc-2d/files/h201425012.out1.nc"

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
G['z'] = G_z[:,:,:].squeeze() # download only one temporal slice
G['t'] = G_time[:].squeeze()

nc.close()

G['z'] = ndimage.gaussian_filter(np.ma.masked_invalid(G['z']),sigma=0.25, order=0,mode="constant",cval=0.5)

counter = 0

out = {
	'hours':[],
	'wvh':[],
	'paths':[],
	'age':[]
}

for dat in G['z']:

	topo = dat

	fig = plt.figure(frameon=False)

	date = (datetime.datetime.fromtimestamp(G['t'][counter]).strftime('%m-%d-%y'))
	day = (datetime.datetime.fromtimestamp(G['t'][counter]).timetuple().tm_yday)
	time = (datetime.datetime.fromtimestamp(G['t'][counter]).strftime('%H'))

	clevs = np.arange(0.0, 20, 0.25)
	cs = plt.contourf(G['x'],G['y'],topo,clevs,cmp='jet')
	cs.levels = [nf(val) for val in cs.levels]

	plt.axis('equal')
	plt.axis('off')

	wvhModel = "%d-"%day +time+"_wv_"+date+".svg"

	fig.savefig('../output/ontario/%d/'%dayof +wvhModel, bbox_inches='tight')

	print '../output/ontario/%d/'%dayof +wvhModel

	out['hours'].append(int(G['t'][counter]))
	out['wvh'].append(nf(np.amax(G['z'][counter])))
	out['paths'].append(str("/models/output/ontario/%d/"%dayof +wvhModel))
	out['age'].append(str(day))

	plt.close()

	counter += 1

json.dump(out, glosJson, indent=4)

exit()
