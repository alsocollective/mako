import matplotlib.pyplot as plt
import matplotlib, pylab
import numpy as np
import netCDF4
import datetime
import scipy.ndimage as ndimage
import os, errno
import simplejson as json
import matplotlib.colors as col
from scipy import interpolate
from scipy.interpolate import griddata

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


url = "http://tds.glos.us/thredds/dodsC/glos/glcfs/superior/fcfmrc-2d/files/s201426312.out1.nc"

try:
	nc = netCDF4.Dataset(url)
	print cl.OKGREEN+"--------\nSuccess!\n--------"+cl.ENDC

except RuntimeError:
	print cl.FAIL+"--------------\nFile not found\n--------------"+cl.ENDC

G_x = nc.variables['lon']
G_y = nc.variables['lat']
G_z = nc.variables['wvh']

G = {} # dictionary ~ Matlab struct
# G['x'] = G_x[:]
G['y'] = G_y[:]
G['z'] = G_z[:5,:,:]

print len(nc.variables['lon'][:])



# print G_z

# print G_x
# print G_x[:]

exit()

# download only one temporal slice

# xH1 = np.amax(G['x'])
# xL1 = np.amin(G['x'])

# xH2 = np.amax(G['x'][0])
# xL2 = np.amin(G['x'][0])

# yH = np.amax(G['y'])
# yL = np.amin(G['y'])

# # G['z'] = np.linspace(nf(np.amin(G_z[:2,:,:])), nf(np.amax(G_z[:2,:,:])), num=100, endpoint=True)
# print "RAW:",len(G['z'][0])
# print "RAW:",G['z']
# print "----"
# print len(nc.variables['lon'][0])
# print len(nc.variables['lon'])
# print len(G_x[0])


# print np.amax(G_x)
# print np.amin(G_x)

# # print "O Length:",len(G_x)
# # print "Dbl Length:",(len(G_x)*2)
# # print "New Array:",np.linspace(np.amin(G_x),np.amax(G_x),num=(len(G_x)*2))

# print "O Length:",len(G_x[0])
# print "Dbl Length:",(len(G_x[0])*2)
# #print "New Array:",np.linspace(np.amin(G_x[0]),np.amax(G_x[0]),num=(len(G_x[0])*2))

# count = 0

# for raw in G_x:

# 	G_x[count] = np.linspace(np.amin(G_x),np.amax(G_x),num=(len(G_x)*2))

# 	print count

# 	count += 1

# #G_x = np.linspace(np.amin(G_x[0]),np.amax(G_x[0]),num=(len(G_x[0])*2))

# print G_x[:]
# # G['x'] = np.linspace(np.amin(G_x),np.amax(G_x),num=(len(G_x)*2))
# # G['x'][0] = np.linspace(np.amin(G_x[0]),np.amax(G_x[0]),num=(len(G_x[0])*2))

# # print G['x']

# # print "RAW:",len(G['x'][0])
# # print "RAW:",len(G['x'])
# #G['x'][0] = np.linspace(xL2,xH2,num=100)
# # nc.variables['lon'][0] = np.linspace(xL1,xH1,num=100)

# # print len(G['x'])
# # print len(G['x'][0])

# exit()