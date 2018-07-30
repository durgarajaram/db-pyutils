import os
from cdb import MCSerialNumberSuperMouse

# location of Preprod
##### uncomment line below to use Preprod
_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"

# location of write-enabled Production Master
#_MASTER_CDB = "http://172.16.246.25:8080"
_MASTER_CDB = "http://heplnm072.pp.rl.ac.uk:8080"

# handle for MCSerialNumberSuperMouse
###### TO USE Master CDB: change _TEST_CDB to _MASTER_CDB in line below
_mcs = MCSerialNumberSuperMouse(_MASTER_CDB)

print _mcs 

# as of CDB v1.1.6 the API has changed so that now:
# the return value from the setter = the MCSerialNumber

#print '> Setting MCSerialNumber....'

############# SET
#serial_number = _mcs.set_datacards('''
#cdb_download_url="http://preprodcdb.mice.rl.ac.uk"
#geometry_download_coolingchannel_tag="SSU-SSD-06pi200+solenoid"
#geometry_download_beamline_tag="3-200+M0"
#geometry_download_by="id"
#geometry_download_id=743
#''',"2.0.0","Tag access for 3-200 beam with fields for 200 MeV/c beam.")
#############

# now we have the serial number to be used for submitting simulation jobs
#print ' >> Done setting. MCSerialNumber = ',serial_number

# check by retrieving this card
#print '=== Retrieving cards for Serial Number ',serial_number
#print _mcs.get_datacards(serial_number)

for i in range(1, 124):
    print '==== reading mcserialnumber',i
    print _mcs.get_datacards(i)

for i in range(155, 200):
    print '==== reading mcserialnumber',i
    print _mcs.get_datacards(i)
