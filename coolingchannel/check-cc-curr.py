import sys
from cdb import CoolingChannel
from cdb import Beamline
from cdb import Cabling
from pprint import pprint
_R_SERVER = "http://cdb.mice.rl.ac.uk"
_TEST_SERVER = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"

#_CCT = CoolingChannel(_R_SERVER)
_CCT = CoolingChannel(_TEST_SERVER)
_CCM = CoolingChannel(_MASTER_CDB)

print _CCT.get_status()
print _CCT.get_server_host_name()
p_cctags = _CCT.list_tags()

print _CCM.get_status()
print _CCM.get_server_host_name()
m_cctags = _CCM.list_tags()

print 
print '++++++ List of CoolingChannel Tags'
print '++++++ MASTER '
pprint(m_cctags)
print
print
print '++++++ PREPROD '
pprint(p_cctags)

for ptag in p_cctags:
    if not ptag in m_cctags:
        print 'Cannot find ', ptag, ' in Production CDB'

print
for mtag in m_cctags:
    cm = _CCM.get_coolingchannel_for_tag(mtag)
#   print mtag, cm
    for mag in cm:
        for cl in mag['coils']:
            if cl['iset'] > 210:
                print '+++++++ TAG: ',mtag, ' mag, coil', cl, '++ iset = ',cl['iset']
  
    if not mtag in p_cctags:
        print 'Cannot find ', ptag, ' in Preprod CDB'
#for tag in cctags:
#  print '++ TAG: ', tag
#  print _CC.get_coolingchannel_for_tag(tag)
#  #print
#
print
print
#print _CC.get_coolingchannel_for_tag('Stop 8341 AFTER2 HR')
#_TAG = '2016-05-4'
#_TAG = '2016-05-4-SSU'
##_TAG = 'StepIV-Off'

#print 'TEST CDB ', _TAG
##test_tag_data = _CCT.get_coolingchannel_for_tag(_TAG)
#print 'MASTER CDB', _TAG
##prod_tag_data = _CCM.get_coolingchannel_for_tag(_TAG)
#pprint(_CCM.get_coolingchannel_for_tag(_TAG))

#pairs = zip(test_tag_data, prod_tag_data)
#any(x != y for x, y in pairs)

#for magid, mag in enumerate(test_tag_data):
#  mag_name = mag['name']
#  print mag['name'], mag['mode'], mag['polarity']
#  print prod_tag_data[magid]['name'], prod_tag_data[magid]['mode'], prod_tag_data[magid]['polarity']
#  for coilid, coil in enumerate(mag['coils']):
#      #print coil['name'], coil['iset']
#      #print prod_tag_data[magid]['coils'][coilid]['iset']
#      this_set = coil['iset']
#      other_set =  prod_tag_data[magid]['coils'][coilid]['iset']
#      assert(this_set == other_set)
#  
#print test_tag_data
_TAG = '2016-05-3-SSUSSD'
_TAG = 'StepIV-Off'
_TAG = 'CCramp-6.1.4-NoTrims'
_TAG = '2016-04-1.3'
_TAG = '2016-04-1.3'
_TAG = '2016-04-1.2'
#print '++++++++++++++++++++++'
#print '++++++ MASTER ',_TAG
#pprint(_CCM.get_coolingchannel_for_tag(_TAG))
#print '++++++ PREPROD ',_TAG
#pprint(_CCM.get_coolingchannel_for_tag(_TAG))
#cm = _CCM.get_coolingchannel_for_tag(_TAG)

#for mag in cm:
#    for cl in mag['coils']:
#        if cl['iset'] > 210:
#            print '+++++++ TAG: ',_TAG, ' mag, coil', mag,cl, '++ iset = ',cl['iset']
  
