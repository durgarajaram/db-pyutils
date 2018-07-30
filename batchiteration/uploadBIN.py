#!/usr/bin/env python

import os
from cdb import BatchIterationSuperMouse

#_CDB_W_SERVER = 'http://172.16.246.25:8080'
#_CDB_W_SERVER = 'http://preprodcdb.mice.rl.ac.uk'
_CDB_W_SERVER = 'http://heplnm072.pp.rl.ac.uk:8080'

print 'CDB_W_SERVER set to: ',_CDB_W_SERVER

print '======== BatchIteration =========='
_BIN_SM = None
try:
  _BIN_SM = BatchIterationSuperMouse(_CDB_W_SERVER)
  print "API Version: " + _BIN_SM.get_version()
  print "Server name: " + _BIN_SM.get_name()
  print _BIN_SM 
  ########################
  # set cards, iterationNumber from Janusz
  ########################
  #######################################################iterationNumber = 3
#  res = _BIN_SM.set_datacards(iterationNumber, "Updated - Preliminary track reconstruction cards",
#'''simulation_geometry_filename = "Stage4.dat"
#reconstruction_geometry_filename = "Stage4.dat" 
#SciFiDigitizationNPECut = 2.0
#SciFiPRHelicalOn = False ''', "")
#  print res
  #######################################################iterationNumber = 4
#  res = _BIN_SM.set_datacards(iterationNumber, "Updated - Preliminary track reconstruction cards",
#'''simulation_geometry_filename = "Stage4.dat"
#reconstruction_geometry_filename = "Stage4.dat" 
#SciFiDigitizationNPECut = 2.0 ''', "")
#  print res
  #######################################################iterationNumber = 5
#  res = _BIN_SM.set_datacards(iterationNumber, "Mapping for Runs 7273 to 7290",
#'''simulation_geometry_filename = "Stage4.dat"
#reconstruction_geometry_filename = "Stage4.dat" 
#SciFiMappingFileName = "scifi_mapping_2015-07-28.txt"
#SciFiCalibrationFileName = "scifi_calibration_2015-07-28.txt"
#SciFiDigitizationNPECut = 2.0 ''', "")
#  print res
  #######################################################iterationNumber = 6
#  res = _BIN_SM.set_datacards(iterationNumber, "No-field legacy geometry for track reconstruction",
#'''simulation_geometry_filename = "Stage4_NoField.dat"
#reconstruction_geometry_filename = "Stage4_NoField.dat" 
#SciFiDigitizationNPECut = 2.0
#SciFiPRHelicalOn = False ''', "")
#  print res


# iterationNumber = 2
#  res = _BIN_SM.set_datacards("Global track matching for mu plus only",
#'''track_matching_pid_hypothesis = "kMuPlus"
#''', "")
#  print res

# iterationNumber = 3
  res = _BIN_SM.set_datacards("Scaled coolingchannel currents from FD",
'''track_matching_pid_hypothesis = "kMuPlus"
geometry_coolingchannel_scales = {"SSU-E2": 1.0180, "SSU-C": 1.0180, "SSU-E1": 1.0180, "SSU-M2": 1.0, "SSU-M1": 1.0, "FCU-C": 1.0, "SSD-E2": 1.0155, "SSD-C": 1.0155, "SSD-E1": 1.0155, "SSD-M1": 1.0, "SSD-M2": 1.0}
''', "")
  print res

  ########################
  # readback
  ########################
  iterationNumber = res
  print '==== reading back ', iterationNumber
  print '======= reco cards: '
  res2 = _BIN_SM.get_reco_datacards(iterationNumber)['reco']
  print res2
  print '======= mc cards: '
  res2 = _BIN_SM.get_reco_datacards(iterationNumber)['mc']
  print res2
except Exception as e:
  print e.message

