import sys
from cdb import Calibration


_CDB_R = "http://cdb.mice.rl.ac.uk"
_CDB_W = "http://172.16.246.25:8080"

_cali = Calibration(_CDB_R)

print _cali
_dev = 'TOF1'
_date = '2016-09-01 00:00:00'

_tstart = '2015-01-01 00:00:00'
_tend = '2016-11-01 00:00:00'
ids = _cali.get_ids(_tstart, _tend)
print type(ids)
for k,v in ids.iteritems():
    if v['device'] != 'TOF1':
        continue
    print k, v

#for _type in [ 'tw', 'trigger', 't0' ]:
#    _fn = _dev + "_" + _type + ".txt"
#    sys.stdout = open(_fn, 'w')
#    print _cali.get_calibration_for_date(_dev, _date, _type)
#
#    _fn = _dev + "_" + _type + "_current.txt"
#    sys.stdout = open(_fn, 'w')
#    print _cali.get_current_calibration(_dev, _type)

#_type = 'tw'
#_fn = _dev + "_" + _type + ".txt"
#sys.stdout = open(_fn, 'w')
#print _cali.get_calibration_for_date(_dev, _date, _type)
#
#_type = 'trigger'
#_fn = _dev + "_" + _type + ".txt"
#sys.stdout = open(_fn, 'w')
#print _cali.get_calibration_for_date(_dev, _date, _type)
#
#_type = 't0'
#_fn = _dev + "_" + _type + ".txt"
#sys.stdout = open(_fn, 'w')
#print _cali.get_calibration_for_date(_dev, _date, _type)

