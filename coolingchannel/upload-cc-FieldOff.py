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

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_PROD_CDB = "http://cdb.mice.rl.ac.uk"
#_MASTER_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"

_server = CoolingChannelSuperMouse(_MASTER_CDB)
print _server
#_server = CoolingChannelSuperMouse(_TEST_CDB)
############################################################################
### The rates, and limits are NOT used by Run Control, only meaningful for ramping
#_calib = '1.0'
#_rate = '0.0'
#_stab = '0.0'
#_vlim = '5.0'
#_ilim = '50.0'

############## TAG 
##### MUST Provide a tag for the current settings
#_CC_TAG = "CCramp-6.1.4"

#[{'polarity': 1, 'coils': [{'vlim': 5.0, 'name': 'SSU-T2', 'iset': -21.71, 'calibration': 0.0451, 'ilim': 35.0, 'stability': 0.0, 'rate': 0.0022}, {'vlim': 16.0, 'name': 'SSU-C', 'iset': 205.53, 'calibration': 0.0147, 'ilim': 210.0, 'stability': 95.0, 'rate': 0.0207}, {'vlim': 5.0, 'name': 'SSU-T1', 'iset': -31.87, 'calibration': 0.0407, 'ilim': 35.0, 'stability': 0.0, 'rate': 0.0032}, {'vlim': 7.0, 'name': 'SSU-M2', 'iset': 247.81, 'calibration': 0.0201, 'ilim': 250.0, 'stability': 95.0, 'rate': 0.025}, {'vlim': 7.0, 'name': 'SSU-M1', 'iset': 99.83, 'calibration': 0.0302, 'ilim': 110.0, 'stability': 95.0, 'rate': 0.0101}], 'name': 'SSU', 'mode': 'solenoid'}, {'polarity': 1, 'coils': [{'vlim': 11.0, 'name': 'FCU-C', 'iset': 72.0, 'calibration': 0.0268, 'ilim': 75.0, 'stability': 95.0, 'rate': 0.0073}], 'name': 'FCU', 'mode': 'solenoid'}, {'polarity': 1, 'coils': [{'vlim': 5.0, 'name': 'SSD-T2', 'iset': 0.0, 'calibration': 0.0451, 'ilim': 10.0, 'stability': 0.0, 'rate': 0.0025}, {'vlim': 16.0, 'name': 'SSD-C', 'iset': 205.53, 'calibration': 0.0147, 'ilim': 210.0, 'stability': 95.0, 'rate': 0.0207}, {'vlim': 5.0, 'name': 'SSD-T1', 'iset': 0.0, 'calibration': 0.0407, 'ilim': 10.0, 'stability': 0.0, 'rate': 0.0025}, {'vlim': 7.0, 'name': 'SSD-M2', 'iset': 0.0, 'calibration': 0.0201, 'ilim': 5.0, 'stability': 95.0, 'rate': 0.025}, {'vlim': 7.0, 'name': 'SSD-M1', 'iset': 0.0, 'calibration': 0.0302, 'ilim': 5.0, 'stability': 95.0, 'rate': 0.025}], 'name': 'SSD', 'mode': 'solenoid'}]

############## SSU, SSD, FCU, FCD currents
#ssu_currents = {}
#ssu_currents['ssu_e2'] = 0.0
#ssu_currents['ssu_c'] = 0.0
#ssu_currents['ssu_e1'] = 0.0
#ssu_currents['ssu_m1'] = 0.0
#ssu_currents['ssu_m2'] = 0.0


#ssd_currents = {}
#ssd_currents['ssd_e2'] = 0.0
#ssd_currents['ssd_c'] = 0.0
#ssd_currents['ssd_e1'] = 0.0
#ssd_currents['ssd_m1'] = 0.0
#ssd_currents['ssd_m2'] = 0.0

#fcu_currents = {}
#fcu_currents['fcu_c'] = 0.0

######### Setup the cooling channel structure for stuffing into CDB
#data = [{'name':'SSU','polarity':'1','mode':'solenoid',\
#                              'coils':\
#                              [{'name':'SSU-E2','calibration':_calib,'ilim':_ilim,'iset':ssu_currents['ssu_e2'],\
#                                'rate':_rate,'stability':_stab,'vlim':_vlim},\
#                               {'name':'SSU-C','calibration':_calib,'ilim':_ilim,'iset':ssu_currents['ssu_c'],\
#                                'rate':_rate,'stability':_stab,'vlim':_vlim},\
#                               {'name':'SSU-E1','calibration':_calib,'ilim':_ilim,'iset':ssu_currents['ssu_e1'],\
#                                'rate':_rate,'stability':_stab,'vlim':_vlim},\
#                               {'name':'SSU-M2','calibration':_calib,'ilim':_ilim,'iset':ssu_currents['ssu_m2'],\
#                                'rate':_rate,'stability':_stab,'vlim':_vlim},\
#                               {'name':'SSU-M1','calibration':_calib,'ilim':_ilim,'iset':ssu_currents['ssu_m1'],\
#                                'rate':_rate,'stability':_stab,'vlim':_vlim}]},\
#                             {'name':'FCU','polarity':'1','mode':'solenoid',\
#                              'coils':\
#                              [{'name':'FCU-C','calibration':_calib,'ilim':_ilim,'iset':fcu_currents['fcu_c'],\
#                                'rate':_rate,'stability':_stab,'vlim':_vlim}]},
#                             {'name':'SSD','polarity':'1','mode':'solenoid',\
#                              'coils':\
#                              [{'name':'SSD-E2','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_e2'],\
#                                'rate':_rate,'stability':_stab,'vlim':_vlim},
#                               {'name':'SSD-C','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_c'],\
#                                'rate':_rate,'stability':_stab,'vlim':_vlim},
#                               {'name':'SSD-E1','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_e1'],\
#                                'rate':_rate,'stability':_stab,'vlim':_vlim},
#                               {'name':'SSD-M2','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_m2'],\
#                                'rate':_rate,'stability':_stab,'vlim':_vlim},
#                               {'name':'SSD-M1','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_m1'],\
#                                'rate':_rate,'stability':_stab,'vlim':_vlim}]}]
_CC_TAG = 'FieldOff'

data = [{'polarity': 1, 'coils': [{'vlim': 5.0, 'name': 'SSU-T2', 'iset': 0.0, 'calibration': 0.0451, 'ilim': 60.0, 'stability': 0.0, 'rate': 0.00187}, {'vlim': 16.0, 'name': 'SSU-C', 'iset': 0.0, 'calibration': 0.0147, 'ilim': 290.0, 'stability': 92.0, 'rate': 0.02438}, {'vlim': 5.0, 'name': 'SSU-T1', 'iset': 0.0, 'calibration': 0.0407, 'ilim': 60.0, 'stability': 0.0, 'rate': 0.00356}, {'vlim': 7.0, 'name': 'SSU-M2', 'iset': 0.0, 'calibration': 0.0201, 'ilim': 290.0, 'stability': 92.0, 'rate': 0.02278}, {'vlim': 7.0, 'name': 'SSU-M1', 'iset': 0.0, 'calibration': 0.0302, 'ilim': 290.0, 'stability': 92.0, 'rate': 0.025}], 'name': 'SSU', 'mode': 'solenoid'}, {'polarity': 1, 'coils': [{'vlim': 10.0, 'name': 'FCU-C', 'iset': 0.0, 'calibration': 1.0, 'ilim': 120.0, 'stability': 90.0, 'rate': 0.01014}], 'name': 'FCU', 'mode': 'solenoid'}, {'polarity': 1, 'coils': [{'vlim': 5.0, 'name': 'SSD-T2', 'iset': 0.0, 'calibration': 0.0451, 'ilim': 60.0, 'stability': 0.0, 'rate': 0.00187}, {'vlim': 16.0, 'name': 'SSD-C', 'iset': 0.0, 'calibration': 0.0147, 'ilim': 290.0, 'stability': 92.0, 'rate': 0.02438}, {'vlim': 5.0, 'name': 'SSD-T1', 'iset': 0.0, 'calibration': 0.0407, 'ilim': 60.0, 'stability': 0.0, 'rate': 0.00356}, {'vlim': 7.0, 'name': 'SSD-M2', 'iset': 0.0, 'calibration': 0.0201, 'ilim': 290.0, 'stability': 92.0, 'rate': 0.02278}, {'vlim': 7.0, 'name': 'SSD-M1', 'iset': 0.0, 'calibration': 0.0302, 'ilim': 290.0, 'stability': 92.0, 'rate': 0.025}], 'name': 'SSD', 'mode': 'solenoid'}]

##### Print
print data

################### SET ########################
print 'SETTING'
print _server.set_coolingchannel_tag(_CC_TAG, data)
#return_xml = str(_server.setCoolingchannel(str(xml)))
#print return_xml


#parseString(return_xml, self._status_handler)
#return self._status_handler.get_message()


print '++++++ Channel Tag', _CC_TAG
print _server.get_coolingchannel_for_tag(_CC_TAG)


