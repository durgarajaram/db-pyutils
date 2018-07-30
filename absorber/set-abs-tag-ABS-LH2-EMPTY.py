from cdb._coolingchannel_supermouse import CoolingChannelSuperMouse

######### PREPROD TEST
#_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
#cc = CoolingChannelSuperMouse(_TEST_CDB)
#########

######## MASTER
_MASTER_CDB = "http://172.16.246.25:8080"
cc = CoolingChannelSuperMouse(_MASTER_CDB)

print help(cc), cc.get_name(), cc.get_server_host_name(), cc.get_version()

############################################################################

abs_data = [\
        {'name':'primary','material':'LH2','shape':'empty','temperature':'0','pressure':'0','comment':'Empty lh2 absorber'},\
        {'name':'secondary1','material':'solid','shape':'empty','temperature':'0','pressure':'0','comment':'Empty solid absorber'},\
        {'name':'secondary2','material':'solid','shape':'empty','temperature':'0','pressure':'0','comment':'Empty solid absorber'}\
        ]

_ABS_TAG = 'ABS-LH2-EMPTY'
xml = ("<tag name='" + str(_ABS_TAG) + "'>")
for absorber in abs_data:
    xml = xml + "<absorber name='" + str(absorber['name']) + "' "
    xml = xml + "material='" + str(absorber['material']) + "' "
    xml = xml + "shape='" + str(absorber['shape']) + "' "
    xml = xml + "temperature='" + str(absorber['temperature']) + "' "
    xml = xml + "pressure='" + str(absorber['pressure']) + "' "
    xml = xml + "comment='" + str(absorber['comment']) + "'/> "
xml = xml + "</tag>"

cc.set_absorber_tag(_ABS_TAG, abs_data)
print 'List'
print cc.list_absorber_tags()
print 'Get'
print cc.get_absorber_for_tag('ABS-LH2-EMPTY')
#print xml
