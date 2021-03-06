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

data = {'valid_from_time': datetime.datetime(2017, 5, 8, 10, 26, 56, 657156), 'valid_until_time': None, 'tag': 'StepIV-Off', 'run': '9287', 'magnets': [{'polarity': -1, 'coils': [{'vlim': 11.0, 'name': 'FCU-C', 'iset': -0.0095, 'calibration': 0.0268, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}], 'name': 'FCU', 'mode': 'flip'}, {'polarity': -1, 'coils': [{'vlim': 5.0, 'name': 'SSD-E2', 'iset': 0.003, 'calibration': 0.0451, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0}, {'vlim': 5.0, 'name': 'SSD-E1', 'iset': 0.003, 'calibration': 0.0407, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0}, {'vlim': 7.0, 'name': 'SSD-M2', 'iset': -0.0012, 'calibration': 0.0201, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}, {'vlim': 7.0, 'name': 'SSD-M1', 'iset': 0.0, 'calibration': 0.0302, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}, {'vlim': 16.0, 'name': 'SSD-C', 'iset': 0.003, 'calibration': 0.0147, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}], 'name': 'SSD', 'mode': 'flip'}, {'polarity': 1, 'coils': [{'vlim': 5.0, 'name': 'SSU-E2', 'iset': 0.0, 'calibration': 0.0451, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0}, {'vlim': 5.0, 'name': 'SSU-E1', 'iset': 0.0, 'calibration': 0.0407, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0}, {'vlim': 7.0, 'name': 'SSU-M2', 'iset': 0.0012, 'calibration': 0.0201, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}, {'vlim': 7.0, 'name': 'SSU-M1', 'iset': -0.0101, 'calibration': 0.0302, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}, {'vlim': 16.0, 'name': 'SSU-C', 'iset': 0.0, 'calibration': 0.0147, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}], 'name': 'SSU', 'mode': 'flip'}]}

_TAG = 'StepIV-Off'
_timestamp = '2017-05-08 10:26:56.657156'

##### Print
print data

#### Get run number
try:
    run = sys.argv[1]
except IndexError:
    print 'No run number supplied. Supply run number as argument'
    sys.exit(1)
   
################### SET ########################
print 'SETTING'
print _server.set_coolingchannel(data, run, _TAG, _timestamp)


#parseString(return_xml, self._status_handler)
#return self._status_handler.get_message()




