"""
This script is for uploading cooling channel currents to a DB

REQUIRED:
	A CDB Installation. Either through MAUS, or standalone as within RunControl
        On miceonrec02:
		source ~/MAUS/.maus_trunk/env.sh

Configurations:
	_TEST_CDB defines the Preprod CDB url
	_PROD_CDB defines the Production Master CDB url

	_CC_TAG defines the name of the tag for the currents

To switch between Preprod and Master, change the argument to the handle on Line:16
e.g. 
     cc = CoolingChannelSuperMouse(_PROD_CDB)
"""
import sys
from cdb import CoolingChannelSuperMouse
import datetime

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_PROD_CDB = "http://cdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"

#_server = CoolingChannelSuperMouse(_TEST_CDB)
_server = CoolingChannelSuperMouse(_MASTER_CDB)
############################################################################

data = [{'polarity': 1, 'coils': [{'vlim': 11.0, 'name': 'FCU-C', 'iset': 56.199, 'calibration': 0.0268, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}], 'name': 'FCU', 'mode': 'solenoid'}, {'polarity': 1, 'coils': [{'vlim': 5.0, 'name': 'SSD-E2', 'iset': 207.996, 'calibration': 0.0451, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0}, {'vlim': 5.0, 'name': 'SSD-E1', 'iset': 207.996, 'calibration': 0.0407, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0}, {'vlim': 7.0, 'name': 'SSD-M2', 'iset': -0.0012, 'calibration': 0.0201, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}, {'vlim': 7.0, 'name': 'SSD-M1', 'iset': 0.0, 'calibration': 0.0302, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}, {'vlim': 16.0, 'name': 'SSD-C', 'iset': 207.996, 'calibration': 0.0147, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}], 'name': 'SSD', 'mode': 'solenoid'}, {'polarity': 1, 'coils': [{'vlim': 5.0, 'name': 'SSU-E2', 'iset': 208.0009, 'calibration': 0.0451, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0}, {'vlim': 5.0, 'name': 'SSU-E1', 'iset': 208.0009, 'calibration': 0.0407, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0}, {'vlim': 7.0, 'name': 'SSU-M2', 'iset': 172.8997, 'calibration': 0.0201, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}, {'vlim': 7.0, 'name': 'SSU-M1', 'iset': 239.1999, 'calibration': 0.0302, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}, {'vlim': 16.0, 'name': 'SSU-C', 'iset': 208.0009, 'calibration': 0.0147, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}], 'name': 'SSU', 'mode': 'solenoid'}]

_RUN = 10382
_TAG = '2016-04-1.7'
_timestamp = '2017-09-07 09:48:11.224337'


################### SET ########################
print 'SETTING with data = '
print data

# set now...note arguments
# 1st arg = RUN, 2nd arg = TAG
# 3rd arg = timestamp === optional(??)

# the timestamp is supposed to be optional
print _server.set_coolingchannel(data, _RUN, _TAG)
#print help(_server)
###print _server.set_coolingchannel(data, run, _TAG, _timestamp)

