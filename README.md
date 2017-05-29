== Updates May 28 2017 ==

=== Resources ===
http://polar.ncep.noaa.gov/waves/examples/usingpython.shtml





mako
====

Peaks, troughs, and sunsets.

Required Packages
=====

MOST requirements will not install via "requirements.txt" and must be installed manually. It's quite a process, and we have outlined it below:

Use "requirements.txt" first to install the easy dependencies.

matplotlib

Old Instructions
=====

== Install Plots ==

* Matplotlib
* Numpy
* NetCDF
? h5py
? cython
? nose
? scipy


== Other ==

* SVGCompress
* shapely


virtualenv== install that

Homebrew

*Change tap: brew tap homebrew/science
* brew install hdf5 !! This is a hard one sometimes

1. GNU Fortran is now provided as part of GCC, and can be installed with: brew install gcc
*More info: https://gcc.gnu.org/

3) Install non-python dependencies (and pil) via homebrew:
brew install
git
gfortran (now GCC)
python
geos
graphviz
hdf5
jasper
netcdf (different from pip?)
pil (pillow)
proj
udunits
pkg-config


VIRTUAL ENVIRONMENT

USE THIS INSTALL RECIPE

Install instructions for OSX 10.8 (Mountain Lion)
=================================================

1) Install Xcode (available from Mac App Store) or the Xcode commandline tools (available from https://developer.apple.com/resources/). If you install Xcode ensure you have also installed the commandline tools by launching Xcode then going to Preferences, selecting the Downloads tab and clicking the 'Install' button for 'Command Line Tools'.

2) Install homebrew package manager (http://mxcl.github.com/homebrew/):
ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"
brew doctor
brew update

3) Install non-python dependencies (and pil) via homebrew:
brew install
git
gfortran (now GCC)
python
geos
graphviz
hdf5
jasper
netcdf (different from pip?)
pil (pillow)
proj
udunits

4) Create a python virtual environment (these instructions use the name 'scitools'):
curl -O -L https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.11.5.tar.gz
tar -zxvf virtualenv-1.11.5.tar.gz
python virtualenv-1.11.5/virtualenv.py scitools

5) Activate the new virtual environment (all that follows must be done in the activated virtual environment):
source scitools/bin/activate

nose==1.3.3
cython==0.20.2
pyshp==1.0.2
shapely==1.3.3
pep8==1.5.7
mock==1.0.1
sphinx==1.2.2
numpy==1.8.2 or 1.8.2
matplotlib==1.3.1
scipy==0.14.0
h5py==2.3.1 *Not sure
netcdf4


6) Install python dependencies into the new virtual environment:
pip install nose cython pyshp shapely pil pep8 mock pyke sphinx
pip install numpy
pip install netCDF4
pip install scipy
pip install matplotlib

pip install owslib
pip install biggus

7) Install GRIB API (optional):

i) Download and unpack:
curl -O  -L https://software.ecmwf.int/wiki/download/attachments/3473437/grib_api-1.9.18.tar.gz
tar -xvf grib_api-1.9.18.tar.gz
cd grib_api-1.9.18

ii) Apply patch for building (patch file is along side this install.txt file):
patch -p1 < ../grib_api-1.9.18_osx10.8.patch

iii) Create a link to python-config in the virtual environment:
ln -s /usr/local/bin/python-config ~/scitools/bin

v) Build and install to virtual environment:
./configure --prefix=$HOME/scitools --enable-python
make
make install
cd ..

vi) Add .pth file to virtualenv's site-packages so that 'import gribapi' works:
echo grib_api > ~/scitools/lib/python2.7/site-packages/gribapi.pth

8) Install PP packing library (optional):

i) Download and unpack:
curl -O -L https://puma.nerc.ac.uk/trac/UM_TOOLS/raw-attachment/wiki/unpack/unpack-030712.tgz
tar -xvf unpack-030712.tgz
cd unpack-030712

ii) Apply patch for building:
patch -p1 < ../unpack-030712_osx10.8.patch

ii) Build and install into virtual environment:
cd libmo_unpack
./make_library
./distribute.sh ~/scitools
cd ../..

9) Install Cartopy:
git clone https://github.com/SciTools/cartopy.git
cd cartopy
python setup.py install
cd ..

10) Install Iris:
git clone https://github.com/SciTools/iris.git
cd iris
python setup.py --with-unpack build_ext -I$HOME/scitools/include -L$HOME/scitools/lib install
cd ..


= Research Notes =

=== Research and Calculations on Data Structure ===

Grid {
     ARRAY:
        Float32 v_wind[time1 = 1][isobaric2 = 39][y = 428][x = 614];
     MAPS:
        Int32 time1[time1 = 1];
        Float64 isobaric2[isobaric2 = 39];
        Float64 y[y = 428];
        Float64 x[x = 614];
    } v_wind;

lat, lon
top left 44.226479, -81.737386
bottom left 44.089533, -81.832143
bottom right 44.054506, -81.413289
top right 44.312032, -81.374837

NAM 12km
WRAMS 8km Great Lakes (Premium)
GFS 0.5 Deg
NAM 5km
CMC 0.6 Deg
WRF 5km

Huron Lat: 45, Lon: -82, Alt: 175 m

http://www.windguru.cz/int/historie.php?model=nam

http://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_hd.pl?dir=%2Fgfs.2014100118%2Fmaster

== Links ==
http://nomads.ncdc.noaa.gov/data.php?name=access#hires_weather_datasets
http://nomads.ncdc.noaa.gov/cgi-bin/ncdc-ui/review-confirmed.pl?req_id=7079&action=Confirm+Request&order_email=symon%40alsocollective.com
http://nomads.ncdc.noaa.gov/thredds/dodsC/nam218/201410/20141031/nam_218_20141031_0000_000.grb.html
http://nomads.ncdc.noaa.gov/thredds/dodsC/nam218/201410/20141030/nam_218_20141030_0000_084.grb.html
http://forecast.weather.gov/MapClick.php?lat=36.472940694658405&lon=-94.32668914468752&site=all&smap=1#.VFK7sfTF-IA
http://forecast.weather.gov/MapClick.php?lat=46.74723&lon=-89.34593220339&unit=0&lg=english&FcstType=digital
http://graphical.weather.gov/sectors/uppermissvly.php?element=MaxT
http://forecast.weather.gov/MapClick.php?lat=46.74723&lon=-89.34593220339&unit=0&lg=english&FcstType=dwml
http://dods.ndbc.noaa.gov/thredds/dodsC/data/stdmet/45003/45003h2014.nc.html
http://forecast.weather.gov/MapClick.php?w3=sfcwind&w3u=2&w13u=0&w16u=1&pqpfhr=6&psnwhr=6&AheadHour=10&Submit=Submit&FcstType=digital&textField1=46.74723&textField2=-89.34593&site=all&unit=0&dd=&bw=


== Weather API Comparison ==
http://michaelwelburn.com/2011/11/02/comparing-weather-apis/

# NOAA Buoy = WSW 13.0 kt ()		| WSW 24.076km
# Weather Underground = WSW 9mph	| WSW 14.48km 4.82803
# Wind Alert = 15 mph WSW			| WSW 24.14km
# Weather Network = W 13km			| W 13km
# Open Weather						| W 9.36km

# Other ?
#http://darkskyapp.com/



== Meh ==
http://www.windfinder.com/help#forecast
http://www.windfinder.com/help#forecast
http://www.windalert.com/map#43.688,-78.285,8,1,52779,2

http://www.ndbc.noaa.gov/
http://www.ndbc.noaa.gov/station_page.php?station=45008
http://www.ndbc.noaa.gov/station_history.php?station=45008
http://www.hotswell.com/


== Science Sources ==

http://nomads.ncdc.noaa.gov/data.php?name=access#hires_weather_datasets
http://nomads.ncdc.noaa.gov/thredds/dodsC/nam218/201410/20141031/nam_218_20141031_0000_000.grb.html

http://www.nco.ncep.noaa.gov/pmb/docs/on388/tableb.html#GRID218

== Website ==

https://shop.sitka.ca/login.php?action=create_account#
http://www.finisterreuk.com/cws/wetsuit.html
http://www.muttonheadstore.com/pages/mountainhigh
http://www.filson.com/
http://hypebeast.com/2014/10/facebook-unveils-its-10-year-plan
http://www.samuji.com/t/categories/fall-2014
http://www.stonefoxbride.com/
http://pitchzine.com/NICOLAS-POLLI
http://www.theinertia.com/category/travel/
http://www.canopycanopycanopy.com/contents/dog_years
http://www.hoodbyair.com/store

http://www.randco.com/collective/
http://leximiller.com/pages/lookbook
http://www.arriere-garde.com/
https://www.theline.com/
http://gainconference.aiga.org/
http://overclothing.com/
http://firmamento.com/
http://mkshft.org/
http://needsupply.com/