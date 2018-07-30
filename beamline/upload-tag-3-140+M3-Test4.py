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
_TAG = '3-140+M3-Test4'

if _TAG in bl_list_tags:
    print "Found", _TAG, "in tag list - press <CR> to continue"
    raw_input()

_tag_data = {}
_tag_data["proton_absorber_thickness"] = 29
_tag_data["diffuser_thickness"] = 0
_tag_data["beam_stop"] = "Open"

_magnet_data = [\
                {'name': 'Q1', 'current': 49.37}, \
		{'name': 'Q2', 'current': 61.59}, \
 		{'name': 'Q3', 'current': 42.72}, \
 		{'name': 'D1', 'current': 146.51}, \
 		{'name': 'DS', 'current': 326.74}, \
 		{'name': 'D2', 'current': 71.92}, \
 		{'name': 'Q4', 'current': 148.91}, \
 		{'name': 'Q5', 'current': 185.14}, \
 		{'name': 'Q6', 'current': 107.52}, \
 		{'name': 'Q7', 'current': 87.04}, \
 		{'name': 'Q8', 'current': 196.59}, \
 		{'name': 'Q9', 'current': 155.82} \
 		]
print '+++++ SETTING TAG on CDB MASTER', _TAG, _tag_data, _magnet_data
_BL.set_beamline_tag(_TAG, _tag_data, _magnet_data)
print '++++++++++++++++++ READING BACK TAG FROM CDB', _TAG
print _BL.get_beamline_for_tag(_TAG)

##############################################################
