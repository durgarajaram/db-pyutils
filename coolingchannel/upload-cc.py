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

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_PROD_CDB = "http://cdb.mice.rl.ac.uk"

cc = CoolingChannelSuperMouse(_TEST_CDB)
############################################################################
### The rates, and limits are NOT used by Run Control, only meaningful for ramping
_calib = '1.0'
_rate = '0.0'
_stab = '0.0'
_vlim = '5.0'
_ilim = '50.0'

############## TAG 
##### MUST Provide a tag for the current settings
_CC_TAG = "StepIV-SSU-ECE-3T"

############## SSU, SSD, FCU, FCD currents
ssu_currents = {}
ssu_currents['ssu_e2'] = 192.45
ssu_currents['ssu_c'] = 211.26
ssu_currents['ssu_e1'] = 187.11
ssu_currents['ssu_m1'] = 0.0
ssu_currents['ssu_m2'] = 0.0


ssd_currents = {}
ssd_currents['ssd_e2'] = 0.0 # 192.45
ssd_currents['ssd_c'] = 0.0 # 211.26
ssd_currents['ssd_e1'] = 0.0 # 187.11
ssd_currents['ssd_m1'] = 0.0
ssd_currents['ssd_m2'] = 0.0

fcu_currents = {}
fcu_currents['fcu_c'] = 0.0 # 63.12

######### Setup the cooling channel structure for stuffing into CDB
cooling_channel_data = [{'name':'SSU','polarity':'1','mode':'solenoid',\
                              'coils':\
                              [{'name':'SSU-E2','calibration':_calib,'ilim':_ilim,'iset':ssu_currents['ssu_e2'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim},\
                               {'name':'SSU-C','calibration':_calib,'ilim':_ilim,'iset':ssu_currents['ssu_c'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim},\
                               {'name':'SSU-E1','calibration':_calib,'ilim':_ilim,'iset':ssu_currents['ssu_e1'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim},\
                               {'name':'SSU-M2','calibration':_calib,'ilim':_ilim,'iset':ssu_currents['ssu_m2'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim},\
                               {'name':'SSU-M1','calibration':_calib,'ilim':_ilim,'iset':ssu_currents['ssu_m1'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim}]},\
                             {'name':'FCU','polarity':'1','mode':'solenoid',\
                              'coils':\
                              [{'name':'FCU-C','calibration':_calib,'ilim':_ilim,'iset':fcu_currents['fcu_c'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim}]},
                             {'name':'SSD','polarity':'1','mode':'solenoid',\
                              'coils':\
                              [{'name':'SSD-E2','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_e2'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim},
                               {'name':'SSD-C','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_c'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim},
                               {'name':'SSD-E1','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_e1'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim},
                               {'name':'SSD-M2','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_m2'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim},
                               {'name':'SSD-M1','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_m1'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim}]}]

##### Print
print _CC_TAG, cooling_channel_data

################### SET ########################
### Uncomment line below to set
#cc.set_coolingchannel_tag(_CC_TAG,cooling_channel_data)

#### VERIFY by reading back the Tag
print ">>> READ BACK of Tag: ",_CC_TAG
cc.get_coolingchannel_for_tag(_CC_TAG)
