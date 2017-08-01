#!/usr/bin/env python

from __future__ import print_function
import subprocess
import os

# set project base directory structure
base = os.getcwd()   

try:
    from setuptools import setup
    setup_kwargs = {'entry_points': {'console_scripts':['processlst=processlst.processlst:main']}}
except ImportError:
    from distutils.core import setup
    setup_kwargs = {'scripts': ['bin/processlst']}
    
from processlst import __version__

#=====build DMS binaries===============================
# get Anaconda root location
p = subprocess.Popen(["conda", "info", "--root"],stdout=subprocess.PIPE)
out = p.communicate()
condaPath = out[0][:-1]

prefix  = os.environ.get('PREFIX')
processDi = os.path.abspath(os.path.join(prefix,os.pardir))
processDir = os.path.join(processDi,'work')
libEnv = os.path.join(prefix,'lib')
libDir = os.path.join(processDir,'source','lib')


#====Creating SYMBOLIC L:INKS===========

subprocess.call(["ln","-s", "%s" % os.path.join(libEnv,'libtiff.a'), 
"%s" % os.path.join(libDir,'libtiff.a')])
subprocess.call(["ln","-s", "%s" % os.path.join(libEnv,'liblzma.a'), 
"%s" % os.path.join(libDir,'liblzma.a')])
subprocess.call(["ln","-s", "%s" % os.path.join(libEnv,'libjpeg.a'), 
"%s" % os.path.join(libDir,'libjpeg.a')])
subprocess.call(["ln","-s", "%s" % os.path.join(libEnv,'libgeotiff.a'), 
"%s" % os.path.join(libDir,'libgeotiff.a')])
subprocess.call(["ln","-s", "%s" % os.path.join(libEnv,'libsz.a'), 
"%s" % os.path.join(libDir,'libsz.a')])
subprocess.call(["ln","-s", "%s" % os.path.join(libEnv,'libGctp.a'), 
"%s" % os.path.join(libDir,'libGctp.a')])
subprocess.call(["ln","-s", "%s" % os.path.join(libEnv,'libdf.a'), 
"%s" % os.path.join(libDir,'libdf.a')])
subprocess.call(["ln","-s", "%s" % os.path.join(libEnv,'libz.a'), 
"%s" % os.path.join(libDir,'libz.a')])
subprocess.call(["ln","-s", "%s" % os.path.join(libEnv,'libmfhdf.a'), 
"%s" % os.path.join(libDir,'libmfhdf.a')])
subprocess.call(["ln","-s", "%s" % os.path.join(libEnv,'libhdfeos.a'), 
"%s" % os.path.join(libDir,'libhdfeos.a')])

print ("installing Landsat_DMS...")
mkPath = os.path.join(processDir,'source','Landsat_DMS')
os.chdir(mkPath)
subprocess.call(["scons","-Q","--prefix=%s" % prefix,"install"])
subprocess.call(["scons","-c"])

#=============setup the python scripts============================

setup(
    name="projectmaslst",
    version=__version__,
    description="prepare LST data for input to pyDisALEXI",
    author="Mitchell Schull",
    author_email="mitch.schull@noaa.gov",
    url="https://github.com/bucricket/projectMASlst.git",
    packages= ['processlst'],
    py_modules=['processlst.processlst','processlst.utils',
                'processlst.lndlst_dms','processlst.landsatTools',
                'processlst.processData'],
    platforms='Posix; MacOS X; Windows',
    license='BSD 3-Clause',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        # Uses dictionary comprehensions ==> 2.7 only
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: GIS',
    ],  
    **setup_kwargs
)

