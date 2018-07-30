import cdb
from cdb import BeamlineSuperMouse

########## MASTER CDB
_MASTER_CDB = "http://172.16.246.25:8080"
_BL = BeamlineSuperMouse(_MASTER_CDB)


########## PREPROD CDB
#_PREPROD_CDB = "http://preprodcdb.mice.rl.ac.uk"
#_BL = BeamlineSuperMouse(_PREPROD_CDB)

bl_list_tags = sorted(_BL.list_tags())

print "list of existing settings"
for tag in bl_list_tags:
    print "    ", tag
print "press <CR> to continue"

raw_input()

##############################################################
_TAG = 'ToF-Calib+150-NoDS'

if _TAG in bl_list_tags:
    print "Found", _TAG, "in tag list - press <CR> to continue"
    raw_input()

_tag_data = {}
_tag_data["proton_absorber_thickness"] = 29
_tag_data["diffuser_thickness"] = 0 
_tag_data["beam_stop"] = "Open"

_magnet_data = [\
                {'name': 'Q1', 'current': 42.0}, \
		{'name': 'Q2', 'current': 52.3}, \
 		{'name': 'Q3', 'current': 36.25}, \
 		{'name': 'D1', 'current': 124.4}, \
 		{'name': 'DS', 'current': 200.0}, \
 		{'name': 'D2', 'current': 63.3}, \
 		{'name': 'Q4', 'current': 102.5}, \
 		{'name': 'Q5', 'current': 137.4}, \
 		{'name': 'Q6', 'current': 90.4}, \
 		{'name': 'Q7', 'current': 61.0}, \
 		{'name': 'Q8', 'current': 91.9}, \
 		{'name': 'Q9', 'current': 77.8} \
 		]
print '+++++ SETTING TAG ', _TAG, _tag_data, _magnet_data
_BL.set_beamline_tag(_TAG, _tag_data, _magnet_data)
print '++++++++++++++++++ CHECKING TAG ', _TAG
print _BL.get_beamline_for_tag(_TAG)

##############################################################
