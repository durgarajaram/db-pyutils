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

from cdb._coolingchannel_supermouse import CoolingChannelSuperMouse

########### PREPROD CDB
_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
cc = CoolingChannelSuperMouse(_TEST_CDB)

########### PRODUCTION CDB
#_PROD_CDB = "http://172.16.246.25:8080"
#cc = CoolingChannelSuperMouse(_PROD_CDB)

############################################################################
### The rates, and limits are NOT used by Run Control, only meaningful for ramping
_calib = '0.0'
_rate = '0.0'
_stab = '0.0'
_vlim = '0.0'
_ilim = '0.0'

############## TAG 
##### MUST Provide a tag for the current settings
_CC_TAG = "FC-100-flip-reverse"

######### Setup the cooling channel structure for stuffing into CDB
cooling_channel_data = [{'polarity': 1, 'coils': [{'vlim': 5.0, 'name': 'SSU-T2', 'iset': 0.0, 'calibration': 0.0451, 'ilim': 60.0, 'stability': 0.0, 'rate': 0.00187}, {'vlim': 16.0, 'name': 'SSU-C', 'iset': 0.0, 'calibration': 0.0147, 'ilim': 290.0, 'stability': 92.0, 'rate': 0.02438}, {'vlim': 5.0, 'name': 'SSU-T1', 'iset': 0.0, 'calibration': 0.0407, 'ilim': 60.0, 'stability': 0.0, 'rate': 0.00356}, {'vlim': 7.0, 'name': 'SSU-M2', 'iset': 0.0, 'calibration': 0.0201, 'ilim': 290.0, 'stability': 92.0, 'rate': 0.02278}, {'vlim': 7.0, 'name': 'SSU-M1', 'iset': 0.0, 'calibration': 0.0302, 'ilim': 290.0, 'stability': 92.0, 'rate': 0.025}], 'name': 'SSU', 'mode': 'solenoid'}, {'polarity': 1, 'coils': [{'vlim': 10.0, 'name': 'FCU-C', 'iset': -100.0, 'calibration': 0.0, 'ilim': 0.0, 'stability': 0.0, 'rate': 0.0}], 'name': 'FCU', 'mode': 'flip'}, {'polarity': 1, 'coils': [{'vlim': 5.0, 'name': 'SSD-T2', 'iset': 0.0, 'calibration': 0.0451, 'ilim': 60.0, 'stability': 0.0, 'rate': 0.00187}, {'vlim': 16.0, 'name': 'SSD-C', 'iset': 0.0, 'calibration': 0.0147, 'ilim': 290.0, 'stability': 92.0, 'rate': 0.02438}, {'vlim': 5.0, 'name': 'SSD-T1', 'iset': 0.0, 'calibration': 0.0407, 'ilim': 60.0, 'stability': 0.0, 'rate': 0.00356}, {'vlim': 7.0, 'name': 'SSD-M2', 'iset': 0.0, 'calibration': 0.0201, 'ilim': 290.0, 'stability': 92.0, 'rate': 0.02278}, {'vlim': 7.0, 'name': 'SSD-M1', 'iset': 0.0, 'calibration': 0.0302, 'ilim': 290.0, 'stability': 92.0, 'rate': 0.025}], 'name': 'SSD', 'mode': 'solenoid'}]

##### Print
print _CC_TAG, cooling_channel_data

################### SET ########################
### Uncomment line below to set
cc.set_coolingchannel_tag(_CC_TAG,cooling_channel_data)

#### VERIFY by reading back the Tag

print ">>> READ BACK of Tag: ",_CC_TAG
print cc.get_coolingchannel_for_tag(_CC_TAG)
