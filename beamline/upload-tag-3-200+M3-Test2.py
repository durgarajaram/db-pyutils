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
_TAG = '3-200+M3-Test2'

if _TAG in bl_list_tags:
    print "Found", _TAG, "in tag list - press <CR> to continue"
    raw_input()

_tag_data = {
    'proton_absorber_thickness': 29 ,
    'diffuser_thickness': 0 ,
    'beam_stop': 'Open' ,
}
_magnet_data = [
    {'name':'D1',  'current': 185.229996 },
    {'name':'D2',  'current': 94.917999 },
    {'name':'DS',  'current': 394.861725 },
    {'name':'Q1',  'current': 60.77 },
    {'name':'Q2',  'current': 75.860001 },
    {'name':'Q3',  'current': 52.73 },
    {'name':'Q4',  'current': 159.460007 },
    {'name':'Q5',  'current': 213.880005 },
    {'name':'Q6',  'current': 141.776001 },
    {'name':'Q7',  'current': 70.036003 },
    {'name':'Q8',  'current': 105.984001 },
    {'name':'Q9',  'current': 90.412003 },
]

print '+++++ SETTING TAG on CDB MASTER', _TAG, _tag_data, _magnet_data
_BL.set_beamline_tag(_TAG, _tag_data, _magnet_data)
print '++++++++++++++++++ READING BACK TAG FROM CDB', _TAG
print _BL.get_beamline_for_tag(_TAG)

##############################################################
