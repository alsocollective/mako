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