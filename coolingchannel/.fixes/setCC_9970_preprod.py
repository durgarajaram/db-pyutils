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

_server = CoolingChannelSuperMouse(_TEST_CDB)
############################################################################

data = [{'polarity': -1, 'coils': [{'vlim': 11.0, 'name': 'FCU-C', 'iset': 129.240005, 'calibration': 0.0268, 'ilim': 132.0, 'stability': 95.0, 'rate': 0.005}], 'name': 'FCU', 'mode': 'flip'}, {'polarity': -1, 'coils': [{'vlim': 5.0, 'name': 'SSD-E2', 'iset': 143.998795, 'calibration': 0.0451, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0}, {'vlim': 5.0, 'name': 'SSD-E1', 'iset': 143.998795, 'calibration': 0.0407, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0}, {'vlim': 7.0, 'name': 'SSD-M2', 'iset': 195.720093, 'calibration': 0.0201, 'ilim': 200.0, 'stability': 95.0, 'rate': 0.025}, {'vlim': 7.0, 'name': 'SSD-M1', 'iset': 0.0, 'calibration': 0.0302, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}, {'vlim': 16.0, 'name': 'SSD-C', 'iset': 143.998795, 'calibration': 0.0147, 'ilim': 210.0, 'stability': 95.0, 'rate': 0.0246}], 'name': 'SSD', 'mode': 'flip'}, {'polarity': 1, 'coils': [{'vlim': 5.0, 'name': 'SSU-E2', 'iset': 205.699799, 'calibration': 0.0451, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0}, {'vlim': 5.0, 'name': 'SSU-E1', 'iset': 205.699799, 'calibration': 0.0407, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0}, {'vlim': 7.0, 'name': 'SSU-M2', 'iset': 168.2491, 'calibration': 0.0201, 'ilim': 170.0, 'stability': 95.0, 'rate': 0.025}, {'vlim': 7.0, 'name': 'SSU-M1', 'iset': 190.999405, 'calibration': 0.0302, 'ilim': 200.0, 'stability': 95.0, 'rate': 0.0123}, {'vlim': 16.0, 'name': 'SSU-C', 'iset': 205.699799, 'calibration': 0.0147, 'ilim': 210.0, 'stability': 95.0, 'rate': 0.0246}], 'name': 'SSU', 'mode': 'solenoid'}]

_RUN = 9970
_TAG = '2017-02-7'
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

