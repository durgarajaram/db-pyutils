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
_TAG = '10-170+M3-Test3'

if _TAG in bl_list_tags:
    print "Found", _TAG, "in tag list - press <CR> to continue"
    raw_input()

_tag_data = {}
_tag_data["proton_absorber_thickness"] = 29
_tag_data["diffuser_thickness"] = 15
_tag_data["beam_stop"] = "Open"

_magnet_data = [\
                {'name': 'Q1', 'current': 71.45}, \
		{'name': 'Q2', 'current': 89.24}, \
 		{'name': 'Q3', 'current': 62.08}, \
 		{'name': 'D1', 'current': 203.41}, \
 		{'name': 'DS', 'current': 514.87}, \
 		{'name': 'D2', 'current': 90.70}, \
 		{'name': 'Q4', 'current': 155.46}, \
 		{'name': 'Q5', 'current': 208.54}, \
 		{'name': 'Q6', 'current': 138.30}, \
 		{'name': 'Q7', 'current': 104.43}, \
 		{'name': 'Q8', 'current': 157.90}, \
 		{'name': 'Q9', 'current': 134.82} \
 		]
print '+++++ SETTING TAG on CDB MASTER', _TAG, _tag_data, _magnet_data
_BL.set_beamline_tag(_TAG, _tag_data, _magnet_data)
print '++++++++++++++++++ READING BACK TAG FROM CDB', _TAG
print _BL.get_beamline_for_tag(_TAG)

##############################################################
