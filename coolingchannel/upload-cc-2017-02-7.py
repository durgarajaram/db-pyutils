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
import time
from cdb import CoolingChannelSuperMouse
from cdb import CoolingChannel

_MASTER_CDB = "http://172.16.246.25:8080" # MLCR master CDB
_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk" # Preproduction test CDB
_PROD_CDB = "http://cdb.mice.rl.ac.uk" # Public read-only CDB

_master_server = CoolingChannelSuperMouse(_MASTER_CDB)
_test_server = CoolingChannelSuperMouse(_TEST_CDB)
_prod_server = CoolingChannel(_PROD_CDB)

#print _server
############################################################################
_CC_TAG = '2017-02-7'
data = [\
  {'polarity': 1, 'coils': \
   [{'vlim': 5.0, 'name': 'SSU-T2', 'iset': 0.0, 'calibration': 0.0451, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0}, \
    {'vlim': 16.0, 'name': 'SSU-C', 'iset': 205.7 , 'calibration': 0.0147, 'ilim': 210.0, 'stability': 95.0, 'rate': 0.0246}, \
    {'vlim': 5.0, 'name': 'SSU-T1', 'iset': 0.0, 'calibration': 0.0407, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0}, \
    {'vlim': 7.0, 'name': 'SSU-M2', 'iset': 168.25, 'calibration': 0.0201, 'ilim': 170.0, 'stability': 95.0, 'rate': 0.025}, \
    {'vlim': 7.0, 'name': 'SSU-M1', 'iset': 191.0, 'calibration': 0.0302, 'ilim': 200.0, 'stability': 95.0, 'rate': 0.0123} \
   ], \
   'name': 'SSU', 'mode': 'solenoid'\
  },\
  {'polarity': -1, 'coils': \
   [{'vlim': 11.0, 'name': 'FCU-C', 'iset': 129.24, 'calibration': 0.0268, 'ilim': 132.0, 'stability': 95.0, 'rate': 0.005}],\
    'name': 'FCU', 'mode': 'flip'\
  },\
  {'polarity': -1, 'coils':\
   [{'vlim': 5.0, 'name': 'SSD-T2', 'iset': 0.0, 'calibration': 0.0451, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0},\
    {'vlim': 16.0, 'name': 'SSD-C', 'iset': 144.0, 'calibration': 0.0147, 'ilim': 210.0, 'stability': 95.0, 'rate': 0.0246},\
    {'vlim': 5.0, 'name': 'SSD-T1', 'iset': 0.0, 'calibration': 0.0407, 'ilim': 1.0, 'stability': 0.0, 'rate': 0.0},\
    {'vlim': 7.0, 'name': 'SSD-M2', 'iset': 195.72, 'calibration': 0.0201, 'ilim': 200.0, 'stability': 95.0, 'rate': 0.025},\
    {'vlim': 7.0, 'name': 'SSD-M1', 'iset': 0.0, 'calibration': 0.0302, 'ilim': 1.0, 'stability': 95.0, 'rate': 0.0}\
   ],\
   'name': 'SSD', 'mode': 'flip'}\
]


##### Print
print data

print 'SETTING PREPROD'
print _test_server.set_coolingchannel_tag(_CC_TAG, data)

print '++++++ Readback Channel Tag from PREPROD', _CC_TAG
print _test_server.get_coolingchannel_for_tag(_CC_TAG)

time.sleep(2)
print 'SETTING MASTER'
print _master_server.set_coolingchannel_tag(_CC_TAG, data)

time.sleep(2)
print '++++++ Readback Channel Tag from PROD', _CC_TAG
print _prod_server.get_coolingchannel_for_tag(_CC_TAG)


