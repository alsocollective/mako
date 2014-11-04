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

#lakes = ["ontario","huron","erie","superior","michigan"]

lakes = ["erie"]

furl = "http://tds.glos.us/thredds/dodsC/glos/glcfs/huron/fcfmrc-2d/files/h201430412.out1.nc"

# for num in lakes:

# # 	#### These should be functions!

# 	doy = datetime.datetime.now().timetuple().tm_yday

# 	if gmt < 12:
# 		filename = (num[0]+""+utc.strftime("%Y")+"%d"%doy+"00.out1.nc")
# 		furl = "https://tds.glos.us/thredds/dodsC/glos/glcfs/"+num+"/fcfmrc-2d/files/"+filename

# 	elif gmt > 12:
# 		filename = (num[0]+""+utc.strftime("%Y")+"%d"%doy+"12.out1.nc")
# 		furl = "https://tds.glos.us/thredds/dodsC/glos/glcfs/"+num+"/fcfmrc-2d/files/"+filename

try:
	nc = netCDF4.Dataset(furl)
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
G['x'] = G_x[:].squeeze() #WHAT IS SQUEEZE?
G['y'] = G_y[:].squeeze()
G['z'] = G_z[:,:,:].squeeze() # download only one temporal slice
G['t'] = G_time[:].squeeze()

nc.close()

high = nf(np.amax(G['z']))

print high

G['z'] = ndimage.gaussian_filter(np.ma.masked_invalid(G['z']),sigma=0.0005, order=0, mode="nearest", cval=0.05)

counter = 0

out = {
	'hours':[],
	'wvh':[],
	'paths':[],
	'age':[]
}



#ERIE


#MICHIGAN


for dat in G['z']:

	topo = dat

	date = (datetime.datetime.fromtimestamp(G['t'][counter]).strftime('%m-%d-%y'))
	day = (datetime.datetime.fromtimestamp(G['t'][counter]).timetuple().tm_yday)
	time = (datetime.datetime.fromtimestamp(G['t'][counter]).strftime('%H'))

	#fig = plt.figure(frameon=False)

	#ONTARIO
	#fig = plt.figure(figsize=(7.195, 2.841), dpi=30, frameon=False)

	#SUPERIOR
	#fig = plt.figure(figsize=(6.195, 2.941), dpi=30, frameon=False)

	#HURON
	fig = plt.figure(figsize=(3.2*2, 2.941*2), dpi=72, frameon=False)

	#ERIE
	#fig = plt.figure(figsize=(3.941, 1.741), dpi=30, frameon=False)

	#MICHIGAN
	#fig = plt.figure(figsize=(2.441, 4.195), dpi=30, frameon=False)
	

	clevs = np.arange(0.0, 10, 0.05)
	#clevs = np.arange(0.0, 5, 0.01)

	norm = col.BoundaryNorm(clevs, 256)

	#cs = plt.contourf(G['x'],G['y'],topo,clevs,cmap='bone',norm=norm, vmin=0, vmax=9.14400)
	
	cs = plt.contour(G['x'],G['y'],topo,clevs,cmap='jet', linewidths=0.5)

	#fig.spines['top'].set_visible(False)
	
	#cs = plt.contourf(G['x'],G['y'],topo,cmap="jet")
	#plt.clim(0.0,20)
	cs.levels = [nf(val) for val in cs.levels]
	#plt.clabel(cs, fontsize=9, inline=1)

	#plt.axis('equal')
	plt.axis('off')

	cs.set_clim([0, 5])

	#cbar = plt.colorbar(cs, ticks=clevs)
	#cbar.set_xticklabels(['Low', 'Medium', 'High'])# horizontal colorbar

	#plt.colorbar()

	#wvhModel = "%d-"%day +time+"_wv_"+date+".svg"
	#wvhModel = "%d-"%counter +"%d"%nf(np.amax(G['z'][counter]))+".png"

	wvhModel = "%d-.png"%counter

	fig.savefig('../output/ontario/%d/'%dayof +wvhModel, bbox_inches='tight',transparent=True,pad_inches=0)

	print '../output/ontario/%d/'%dayof +wvhModel

	out['hours'].append(int(G['t'][counter]))
	out['wvh'].append(nf(np.amax(G['z'][counter])))
	out['paths'].append(str("/models/output/ontario/%d/"%dayof +wvhModel))
	out['age'].append(str(day))

	plt.close()

	counter += 1

json.dump(out, glosJson, indent=4)

exit()
