"""
This is a script to list the existing list of calibrations in the CDB

_tstart and _tend control the start/end dates between which we query the CDB

_devicelist is a list of devices (detectors) queries

All tracker calibrations are under the "TRACKERS" device
TOF calibrations are under the name of the primary trigger detector
.. i.e. the timewalk, trigger, t0 calibrations for TOF1-triggered data is under "TOF1" device
"""

import cdb

_server = "http://cdb.mice.rl.ac.uk"

_cali = cdb.Calibration(_server)

_tstart = '2013-05-01 00:00:00'
_tend = '2018-05-01 00:00:00'

print 'LIST OF DEVICES: ',_cali.list_devices()
ids = _cali.get_ids(_tstart, _tend)


_devicelist = ['TOF1', 'TRACKERS']
print type(ids)
#for k, v in sorted(ids.iteritems(), key=lambda x: int(x)):
calidict = {}
for _id, _vali in sorted(ids.iteritems()):
    thisDevice = _vali['device']
    vFrom = _vali['valid_from']
    if thisDevice not in _devicelist:
        continue
    print _id, _vali, vFrom, thisDevice
    vtup = _id, thisDevice
    calidict[vFrom] = vtup
    print
print
print len(calidict), ' Calibrations'
print
for k, v in sorted(calidict.iteritems()):
    print '%10s ID:%4s valid_from:%s' % (v[1],v[0],k)

