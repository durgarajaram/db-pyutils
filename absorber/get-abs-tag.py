#from cdb import CoolingChannelSuperMouse
from cdb import CoolingChannel
from cdb import Beamline

#_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"

_R_CDB = "http://cdb.mice.rl.ac.uk"
cc = CoolingChannel(_R_CDB)

#_MASTER_CDB = "http://172.16.246.25:8080"
#cc = CoolingChannelSuperMouse(_MASTER_CDB)


bl = Beamline(_R_CDB)

#print cc, help(cc), cc.get_name(), cc.get_server_host_name(), cc.get_version()

############################################################################

#print 'List'
#rint cc.list_absorber_tags()
#print 'Get'
#print cc.get_absorber_for_tag('ABS-SOLID-EMPTY')

print 'Get CCrun'
print cc.get_coolingchannel_for_run(7929)
print 'Get Absrun'
print cc.get_absorber_for_run(7929)


#print 'Get Beamline'
#print bl.get_beamline_for_run(7929)

