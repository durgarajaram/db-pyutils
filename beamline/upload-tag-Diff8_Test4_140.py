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
_TAG = 'DiffMask8-3-140+M3-Test4'

if _TAG in bl_list_tags:
    print "Found", _TAG, "in tag list - press <CR> to continue"
    raw_input()

_tag_data = {}
_tag_data["proton_absorber_thickness"] = 49
_tag_data["diffuser_thickness"] = 8
_tag_data["beam_stop"] = "Open"

_magnet_data = [\
                {'name': 'Q1', 'current': 48.0}, \
		{'name': 'Q2', 'current': 59.9}, \
 		{'name': 'Q3', 'current': 41.6}, \
 		{'name': 'D1', 'current': 165.0}, \
 		{'name': 'DS', 'current': 311.0}, \
 		{'name': 'D2', 'current': 78.0}, \
 		{'name': 'Q4', 'current': 131.3}, \
 		{'name': 'Q5', 'current': 176.0}, \
 		{'name': 'Q6', 'current': 116.7}, \
 		{'name': 'Q7', 'current': 110.8}, \
 		{'name': 'Q8', 'current': 167.5}, \
 		{'name': 'Q9', 'current': 142.9} \
 		]
print '+++++ SETTING TAG on CDB MASTER', _TAG, _tag_data, _magnet_data
_BL.set_beamline_tag(_TAG, _tag_data, _magnet_data)
print '++++++++++++++++++ READING BACK TAG FROM CDB', _TAG
print _BL.get_beamline_for_tag(_TAG)

##############################################################
