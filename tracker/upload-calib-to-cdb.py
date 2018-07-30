#!/usr/bin/env python
""" 
Write SciFi mapping from file
This script must, and can, be run only from a micenet computer
Reads calibrations from a file and uploads them to the CDB
For protection against unintentional uploads, the filename and the upload lines are commented out
To upload: 
          Set the appropriate filenames - _CALI_FILENAME for the calibration file
                                    and
                                          _BC_FILENAME for the bad channels file
          Type is either 'trackers' or 'bad_chan'
          Set the appropriate timestamp (valid from) - _TIMESTAMP
"""

from cdb import CalibrationSuperMouse

########## Set the server names and calibration service

# cdb write server
_CDB_W_SERVER = 'http://172.16.246.25:8080'
#_CDB_W_SERVER = 'http://preprodcdb.mice.rl.ac.uk'
_CALI_SM = CalibrationSuperMouse(_CDB_W_SERVER)

print "API Version: " + _CALI_SM.get_version()
print "Server name: " + _CALI_SM.get_name()

print _CALI_SM

#####################################################################
########## Valid-from date ranges for the calibration

# new scifi mapping file, valid from date
_TIMESTAMP = "2017-09-14 00:00:00.0"

#####################################################################
## _DEVICE: is the trigger station
## _CABLINGFILE: is the mapping file to read for a given DEVICE
#####################################################################
_DEVICE = 'TRACKERS'
_TYPE = 'trackers'
# set the mapping filename - after swapping waveguides Sep 14
#_CALI_FILENAME = 'scifi_calibration_20170914_1426.txt'
#_CALI_FILENAME = 'scifi_calibration_20170922_1843.txt'
_CALI_FILENAME = 'scifi_calibration_20170929_1232.txt'

_CALIFILE = open(_CALI_FILENAME, 'r')

# read the file
_DATA = _CALIFILE.read()

print '+++ Setting ', _DEVICE, _TYPE, _TIMESTAMP

### set the calibration - uncomment below to upload
print _CALI_SM.set_detector(_DEVICE, _TYPE, _TIMESTAMP, _DATA) 

# close the file
_CALIFILE.close()

#####################################################################
_DEVICE = 'TRACKERS'
_TYPE = 'bad_chan'

# set the mapping filename - after swapping waveguides Sep 14
#_BC_FILENAME = 'scifi_badchannels_20170914_1426.txt'
#_BC_FILENAME = 'scifi_bad_channels_20170922_1843.txt'
_BC_FILENAME = 'scifi_badchannels_20170929_1232.txt'

_BCFILE = open(_BC_FILENAME, 'r')

# read the file
_BC_DATA = _BCFILE.read()

print '+++ Setting ', _DEVICE, _TYPE, _TIMESTAMP

### set the calibration - uncomment below to upload
print _CALI_SM.set_detector(_DEVICE, _TYPE, _TIMESTAMP, _BC_DATA) 

# close the file
_BCFILE.close()

