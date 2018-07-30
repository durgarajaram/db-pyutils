import cdb

#_server = "http://preprodcdb.mice.rl.ac.uk"
_server = "http://cdb.mice.rl.ac.uk"

cali = cdb.Calibration(_server)

_TSTART = '2017-01-01 00:00:00'
_TEND = '2017-10-01 00:00:00'

print cali.get_ids(_TSTART, _TEND)
