import cdb
from cdb import Beamline
from pprint import pprint

########## MASTER CDB
_MASTER_CDB = "http://172.16.246.25:8080"
_PROD_CDB = "http://172.16.246.25:8080"
#_BL = Beamline(_PROD_CDB)
_BL = Beamline(_MASTER_CDB)


########## PREPROD CDB
#_PREPROD_CDB = "http://preprodcdb.mice.rl.ac.uk"
#_BL = BeamlineSuperMouse(_PREPROD_CDB)

tags_list = _BL.list_tags()
print "++++ List of Beamline Tags"
pprint(sorted(tags_list))
#for _tag in ['PionReference-DS', '3-200+M3--Test1']:
for _tag in sorted(tags_list):
    print
    print
    print tags_list.index(_tag), _tag #, _BL.get_beamline_for_tag(_tag).keys().index(_tag)
    settings = _BL.get_beamline_for_tag(_tag)[_tag]
    for key in settings:
        if key == 'magnets':
            mags = settings['magnets']
            for a_mag in sorted(mags.keys()):
                print '   ', a_mag.ljust(5), str(mags[a_mag]).ljust(5)
        else:
            print key.ljust(20), str(settings[key]).ljust(5)

#print _BL.get_beamline_for_tag('ToF-Calib+150')
#print
#print _BL.get_beamline_for_tag('PionReference-DS')
#print
#print _BL.get_beamline_for_tag('400MeV+DS200')
#print
#print _BL.get_beamline_for_tag('400MeV+pi_pa82')
#print
_BLT = '3-200+M3-Test2'
pprint(_BL.get_beamline_for_tag(_BLT))
print
_BLT = '6-200+M3-Test1'
pprint(_BL.get_beamline_for_tag(_BLT))
print
_BLT = '10-200+M3-Test1'
pprint(_BL.get_beamline_for_tag(_BLT))

