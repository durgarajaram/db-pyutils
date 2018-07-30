import os
from cdb import MCSerialNumberSuperMouse

# location of Preprod
##### uncomment line below to use Preprod
_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"

# location of write-enabled Production Master
#_MASTER_CDB = "http://172.16.246.25:8080"
_MASTER_CDB = "http://heplnm072.pp.rl.ac.uk:8080"
#_MASTER_CDB = "http://cdb.mice.rl.ac.uk"


# handle for MCSerialNumberSuperMouse
###### TO USE Master CDB: change _TEST_CDB to _MASTER_CDB in line below
_mcs = MCSerialNumberSuperMouse(_MASTER_CDB)

print _mcs 

# as of CDB v1.1.6 the API has changed so that now:
# the return value from the setter = the MCSerialNumber

print '> Setting MCSerialNumber....'

############# SET
#serial_number = _mcs.set_datacards('''
#geometry_download_by="run_number"
#geometry_download_run_number=7469
#TOF_calib_by="date"
#TOF_cabling_by="date"
#TOF_calib_date_from="2015-10-07 14:00:00"
#TOF_cabling_date_from="2015-10-07 14:00:00"
#TOFscintLightSpeed=134.5
#''',"2.5.0","Download by run number 7469. Emittance production. G4BL 3182Mu.")
############# SET
#serial_number = _mcs.set_datacards('''
#geometry_download_by="id" 
#geometry_download_id=168
#geometry_download_beamline_for_run=7469
#geometry_download_coolingchannel_tag="StepIV-3T" 
#''',"2.5.0","Download by id 168. Energy loss study, Empty absorber. G4BL 3182Mu.")
#############
#serial_number = _mcs.set_datacards('''
#geometry_download_by="run_number"
#geometry_download_run_number=7798
#''',"3.0.1","Download by run number 7798. 218 MeV. G4BL V4 3_218Mu")
#############
#serial_number = _mcs.set_datacards('''
#geometry_download_by="run_number" 
#geometry_download_run_number=8681
#keep_tracks=True
#particle_decay=True
#physics_processes="standard" 
#''',"2.9.1","Download by run number 8681. 140 MeV. G4BL V4 3_140_M3v2")
#############
#serial_number = _mcs.set_datacards('''
#geometry_download_by="run_number"
#geometry_download_run_number=10288
#cdb_download_url="http://preprodcdb.mice.rl.ac.uk/cdb/" 
#SciFiPatRecLongitudinalFitter=0
#SciFiPatRecCircleFitter=0
#''',"3.0.3","Run 10288. Extra lh2 v.p. LSQ fitter. G4BL V4 3_140_M3v2")
#############           
#serial_number = _mcs.set_datacards('''
#geometry_download_by="run_number"
#geometry_download_run_number=8366
#''',"3.1.2","writing test")
#############
serial_number = _mcs.set_datacards('''
geometry_download_by="run_number" 
geometry_download_run_number=8643
track_matching_pid_hypothesis="kMuPlus" 
geometry_coolingchannel_scales={"SSU-E2": 1.0180, "SSU-C": 1.0180, "SSU-E1": 1.0180, "SSU-M2": 1.0, "SSU-M1": 1.0, "FCU-C": 1.0, "SSD-E2": 1.0155, "SSD-C": 1.0155, "SSD-E1": 1.0155, "SSD-M1": 1.0, "SSD-M2": 1.0}
SciFiParams_Density=1.60
''',"3.2.1","run 8643 2016-04_1-2 LiH 3-140. G4BL V5 3-140+M3-Test4")
#############         


# now we have the serial number to be used for submitting simulation jobs
print ' >> Done setting. MCSerialNumber = ',serial_number

# check by retrieving this card
print '=== Retrieving cards for Serial Number ',serial_number
print _mcs.get_datacards(serial_number)
