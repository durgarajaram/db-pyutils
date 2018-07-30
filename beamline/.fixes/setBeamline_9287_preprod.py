import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
#####_MASTER_CDB = "http://172.16.246.25:8080"
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 9287

startrun_xml_9287 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='9287' startTime='2017-05-08 10:26:56.23627' startNotes='DFC test' optics='DiffMask8-ToF-Calib+Pulser Data' startPulse='4809166' step='4.0' status='false' runType='Pulser Data' daqTrigger='PULSER' daqGateWidth='3.0005' daqVersion='DATE_v7.66 EqList_v1.0.0-1-gf902e9e' gdcHostName='miceraid5' targetDelay='0.0' targetDepth='0.0' targetDriveVoltage='0.0'><ldcHost name='miceacq20'/><ldcHost name='miceacq17'/><ldcHost name='miceacq16'/><ldcHost name='miceacq15'/><ldcHost name='miceacq14'/> </startRun>"

print bl.set_start_runXML(startrun_xml_9287)


###################################
# now set beamline for Run 9287

beamline_xml_9287 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='9287' beamStop='false' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='0' > <magnet name='D1' setCurrent='0.000003' polarity='1'/><magnet name='D2' setCurrent='0.016' polarity='1'/><magnet name='DS' setCurrent='199.119' polarity='1'/><magnet name='Q1' setCurrent='0.0' polarity='1'/><magnet name='Q2' setCurrent='0.0' polarity='1'/><magnet name='Q3' setCurrent='0.0' polarity='1'/><magnet name='Q4' setCurrent='0.0' polarity='1'/><magnet name='Q5' setCurrent='0.0' polarity='1'/><magnet name='Q6' setCurrent='0.0' polarity='1'/><magnet name='Q7' setCurrent='0.0' polarity='1'/><magnet name='Q8' setCurrent='0.0' polarity='1'/><magnet name='Q9' setCurrent='0.0' polarity='1'/> </beamline>"

print bl.set_beamlineXML(beamline_xml_9287)

###################################
# now set end of run for Run 9287

endrun_xml_9287 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='9287' endTime='2017-05-08 12:00:29.356372' endNotes='DFC test' status='0' endPulse='4809516' overwrite='0' > <scalar name='GVa1 Triggers' value='49'/><scalar name='LMC-1234 Count' value='9'/><scalar name='LMC-12 Count' value='93'/><scalar name='LMC-34 Count' value='75'/><scalar name='Particle Triggers' value='748'/><scalar name='Requested Triggers' value='2940'/><scalar name='ToF0 Triggers' value='3'/><scalar name='ToF1 Triggers' value='2'/><scalar name='ToF2 Triggers' value='5'/><isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/><isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/><isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/><isisBeam name='IBML-TOT' mean='0.0' sigma='0.0'/> </endRun>"

print bl.set_end_runXML(endrun_xml_9287)

