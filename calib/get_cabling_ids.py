"""
This is a script to list the existing list of cabling maps in the CDB

_tstart and _tend control the start/end dates between which we query the CDB

_devicelist is a list of devices (detectors) queries

All tracker maps are under the "TRACKERS" device
TOF maps are stored under "TOF0", "TOF1", "TOF2" devices
The overall DAQ map is under the "DAQ" device
"""

import cdb

# CDB read server 
_server = "http://cdb.mice.rl.ac.uk"

# Cabling service
_cab= cdb.Cabling(_server)

# Start, End range for retrieval
_tstart = '2013-05-01 00:00:00'
_tend = '2018-05-01 00:00:00'

print 'LIST OF DEVICES: ',_cab.list_devices()

# device list. Will get maps for each detector in list
_devices = ['TRACKERS', 'DAQ', 'TOF1', 'TOF2']

#######################################################

# get the list of IDs
# returns a dictionary key=ID, value = a dictionary for that ID with device name, valid, creation dates as values
ids = _cab.get_ids(_tstart, _tend)

cabdict = {}
for _id, _vali in sorted(ids.iteritems()):
    thisDevice = _vali['device']
    valiFrom = _vali['valid_from']
    if thisDevice not in _devices:
        continue
    vtup = _id, thisDevice
    cabdict[valiFrom] = vtup
print
print len(cabdict), _devices, ' Cabling maps'
print
for k, v in sorted(cabdict.iteritems()):
    print '%10s ID:%4s %s' % (v[1], v[0], k)
