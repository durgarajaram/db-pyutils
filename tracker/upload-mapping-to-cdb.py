#!/usr/bin/env python
""" 
Write SciFi mapping from file
This script must, and can, be run only from a micenet computer
Reads calibrations from a file and uploads them to the CDB
For protection against unintentional uploads, the filename and the upload lines are commented out
To upload: 
          Set the appropriate filenames - _CABLING_FILENAME
          Set the appropriate timestamp (valid from) - _TIMESTAMP
"""

from cdb import CablingSuperMouse

########## Set the server names and calibration service

# cdb write server
_CDB_W_SERVER = 'http://172.16.246.25:8080'
#_CDB_W_SERVER = 'http://preprodcdb.mice.rl.ac.uk'
_CABLING_SM = CablingSuperMouse(_CDB_W_SERVER)

print "API Version: " + _CABLING_SM.get_version()
print "Server name: " + _CABLING_SM.get_name()

print _CABLING_SM

#####################################################################
########## Valid-from date ranges for the calibration

# new scifi mapping file, valid from date
_TIMESTAMP = "2017-09-14 00:00:00.0"

#####################################################################
## _DEVICE: is the trigger station
## _CABLINGFILE: is the mapping file to read for a given DEVICE
#####################################################################
_DEVICE = 'Trackers'

# set the mapping filename - after swapping waveguides Sep 14
_CABLING_FILENAME = 'scifi_mapping_20170914_1426.txt'

_CABLINGFILE = open(_CABLING_FILENAME, 'r')

# read the file
_DATA = _CABLINGFILE.read()

#print _DEVICE, _TYPE, _TIMESTAMP, _DATA

### set the calibration - uncomment below to upload
print _CABLING_SM.set_detector(_DEVICE, _TIMESTAMP, _DATA) 

# close the file
_CABLINGFILE.close()

#####################################################################
