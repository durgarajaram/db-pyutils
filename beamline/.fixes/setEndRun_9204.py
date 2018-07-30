import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"
bl = BeamlineSuperMouse(_MASTER_CDB)

# now set end of run for Run 9204 (illegal message characters caused this to be aborted)

endrun_xml_9204 = """<?xml version='1.0'?>
<endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='9204' endTime='2017-02-25 23:52:28.334778' endNotes='H13c 10-140 OK good night ' status='0' endPulse='4495650' overwrite='0'>
  <isisBeam name='IBML-TOT' mean='1.481618' sigma='0.008197'/>
  <isisBeam name='IBML-S8.1' mean='0.779805' sigma='0.003662'/>
  <isisBeam name='IBML-S7.4' mean='0.286207' sigma='0.001402'/>
  <isisBeam name='IBML-S7.3' mean='0.415604' sigma='0.003133'/>
  <scalar name='LMC-1234 Count' value='623738' />
  <scalar name='LMC-12 Count' value='4961584' />
  <scalar name='LMC-34 Count' value='4637590' />
  <scalar name='ToF2 Triggers' value='70241' />
  <scalar name='ToF1 Triggers' value='467078' />
  <scalar name='ToF0 Triggers' value='1775730' />
  <scalar name='GVa1 Triggers' value='4639' />
  <scalar name='Requested Triggers' value='467095' />
  <scalar name='Particle Triggers' value='343376' />
</endRun>"""

#print endrun_xml_9204
print bl.set_end_runXML(endrun_xml_9204)


