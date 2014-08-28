from mpl_toolkits.basemap import Basemap, cm
import matplotlib.pyplot as plt
import netCDF4
import numpy as np
import pylab
import shapely
import scipy.ndimage
#import pydap

# open a local NetCDF file or remote OPeNDAP URL

#Lake Erie
#url = 'http://tds.glos.us/thredds/dodsC/glos/glcfs/erie/fcfmrc-2d/files/e201422912.out1.nc'
#Lake Ontario
url = 'http://tds.glos.us/thredds/dodsC/glos/glcfs/ontario/fcfmrc-2d/files/o201422912.out1.nc'
#Lake Huron
#url = 'http://tds.glos.us/thredds/dodsC/glos/glcfs/huron/fcfmrc-2d/files/h201422912.out1.nc'

nc = netCDF4.Dataset(url)

print nc.variables.keys()
print nc.variables['sigma']

#make sure the value of resolution is a lowercase L,
# for 'low', not a numeral 1
m = Basemap(projection='merc', lat_0=43, lon_0=-79,
    resolution = 'i', area_thresh = 1000.0,
    llcrnrlon=-79.82095336914062, llcrnrlat=43.14161682128906,
    urcrnrlon=-76.06649017333984, urcrnrlat=44.237491607666016)



# Get grid data
#grid   = opendap(url_grid)
G = {} # dictionary ~ Matlab struct
lons = nc.variables['lon']
lats = nc.variables['lat']
#G_z = nc.variables['depth']
G_z = nc.variables['wvh']
 
G['x'] = lons[:].squeeze()
G['y'] = lats[:].squeeze()
G['z'] = G_z[1,:,:] #.squeeze() # download only one temporal slice

# print "===="
# print len(G['z'])
# print len(scipy.ndimage.zoom(G['z'],2))

# G['z'][:] = scipy.ndimage.zoom(G['z'][:],2)

# print "===="
# print len(G['z'][:])
# #G['z'] = G_z[:].squeeze()

# G['z'] = np.ma.masked_invalid(G['z'])

ny = G['z'].shape[0]
nx = G['z'].shape[1]
lons, lats = m.makegrid(nx, ny) # get lat/lons of ny by nx evenly space grid.
# lons, lats = np.meshgrid(nx, ny)
x, y = m(lons, lats) # compute map proj coordinates.

# data = scipy.ndimage.zoom(data, 3)
m.drawcoastlines()
m.drawmapboundary(fill_color='white')
# m.fillcontinents(color='gray')
#cs2 = m.contour(x,y,G['z'],color='k')
#data = scipy.ndimage.gaussian_filter(G['z'], sigma=5.5)

cs = m.contourf(x,y,G['z'],cmp='jet',interpolation='nearest')
#plt.clabel(cs, inline=1, fontsize=10)

#lons, lats = np.meshgrid(lons, lats)


# plot grid data

plt.axis('tight')
plt.axis('equal')
plt.axis('off')
pylab.savefig('testcontours1.svg')

#plt.show()
