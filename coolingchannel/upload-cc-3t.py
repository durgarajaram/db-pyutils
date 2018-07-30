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
#_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
#cc = CoolingChannelSuperMouse(_TEST_CDB)

########### PRODUCTION CDB
_PROD_CDB = "http://172.16.246.25:8080"
cc = CoolingChannelSuperMouse(_PROD_CDB)

############################################################################
### The rates, and limits are NOT used by Run Control, only meaningful for ramping
_calib = '0.0'
_rate = '0.0'
_stab = '0.0'
_vlim = '0.0'
_ilim = '0.0'

############## TAG 
##### MUST Provide a tag for the current settings
_CC_TAG = "StepIV-3T"

############## SSU, SSD, FCU, FCD currents
ssu_currents = {}
ssu_currents['ssu_t2'] = -18.81
ssu_currents['ssu_c'] = 211.26
ssu_currents['ssu_t1'] = -24.15
ssu_currents['ssu_m1'] = 135.21 # 0.0
ssu_currents['ssu_m2'] = 236.83 # 0.0


ssd_currents = {}
ssd_currents['ssd_t2'] = -13.37
ssd_currents['ssd_c'] = 150.11
ssd_currents['ssd_t1'] = -17.16
ssd_currents['ssd_m1'] = 0.0
ssd_currents['ssd_m2'] = 0.0

############### To make things interesting, FCU is actually FC1 which is downstream
fcu_currents = {}
fcu_currents['fcu_c'] = 55.98

############### The magnet in the hall for StepIV is actually FCD
fcd_currents = {}
fcd_currents['fcd_c'] = 0.0

######### Setup the cooling channel structure for stuffing into CDB
cooling_channel_data = [{'name':'SSU','polarity':'1','mode':'solenoid',\
                              'coils':\
                              [{'name':'SSU-T2','calibration':_calib,'ilim':_ilim,'iset':ssu_currents['ssu_t2'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim},\
                               {'name':'SSU-C','calibration':_calib,'ilim':_ilim,'iset':ssu_currents['ssu_c'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim},\
                               {'name':'SSU-T1','calibration':_calib,'ilim':_ilim,'iset':ssu_currents['ssu_t1'],\
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
                              [{'name':'SSD-T2','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_t2'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim},
                               {'name':'SSD-C','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_c'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim},
                               {'name':'SSD-T1','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_t1'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim},
                               {'name':'SSD-M2','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_m2'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim},
                               {'name':'SSD-M1','calibration':_calib,'ilim':_ilim,'iset':ssd_currents['ssd_m1'],\
                                'rate':_rate,'stability':_stab,'vlim':_vlim}]}]

##### Print
print _CC_TAG, cooling_channel_data

################### SET ########################
### Uncomment line below to set
cc.set_coolingchannel_tag(_CC_TAG,cooling_channel_data)

#### VERIFY by reading back the Tag
print ">>> READ BACK of Tag: ",_CC_TAG
print cc.get_coolingchannel_for_tag(_CC_TAG)
