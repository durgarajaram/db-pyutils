import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
#####_MASTER_CDB = "http://172.16.246.25:8080"
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 8448

startrun_xml_8448 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='8448' startTime='2016-10-25 10:29:10.834174' startNotes='Starting task 3 170 MeV ' optics='3-170+M3-Test1' startPulse='2907882' step='4.0' status='false' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.0005' daqVersion='DATE_v7.66 EqList_v1.0.0-1-gf902e9e' gdcHostName='miceraid5' targetDelay='0.0' targetDepth='0.0' targetDriveVoltage='0.0'><ldcHost name='miceacq20'/><ldcHost name='miceacq17'/><ldcHost name='miceacq16'/><ldcHost name='miceacq15'/><ldcHost name='miceacq14'/> </startRun>"

print bl.set_start_runXML(startrun_xml_8448)

###################################
# now set beamline for Run 8448

beamline_xml_8448 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='8448' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='D1' setCurrent='160.800003' polarity='1'/><magnet name='D2' setCurrent='86.545998' polarity='1'/><magnet name='DS' setCurrent='352.738464' polarity='1'/><magnet name='Q1' setCurrent='54.150002' polarity='1'/><magnet name='Q2' setCurrent='67.57' polarity='1'/><magnet name='Q3' setCurrent='46.959999' polarity='1'/><magnet name='Q4' setCurrent='144.731995' polarity='1'/><magnet name='Q5' setCurrent='194.024002' polarity='1'/><magnet name='Q6' setCurrent='128.612' polarity='1'/><magnet name='Q7' setCurrent='124.916' polarity='1'/><magnet name='Q8' setCurrent='188.936005' polarity='1'/><magnet name='Q9' setCurrent='161.244003' polarity='1'/> </beamline>"

print bl.set_beamlineXML(beamline_xml_8448)

###################################
# now set end of run for Run 8448

endrun_xml_8448 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='8448' endTime='2016-10-25 11:08:43.353377' endNotes='Task 3 170 MeV stopped. ISIS down' status='0' endPulse='2909644' overwrite='0' > <scalar name='LMC-34 Count' value='1344334'/><scalar name='Particle Triggers' value='62479'/><scalar name='Requested Triggers' value='78895'/><scalar name='ToF0 Triggers' value='350352'/><scalar name='ToF1 Triggers' value='78895'/><scalar name='ToF2 Triggers' value='24211'/><isisBeam name='IBML-S8.1' mean='1.093642' sigma='0.027869'/><isisBeam name='IBML-S7.4' mean='0.358788' sigma='0.009143'/><isisBeam name='IBML-S7.3' mean='0.593269' sigma='0.014807'/><isisBeam name='IBML-TOT' mean='2.0457' sigma='0.051818'/> </endRun>"

print bl.set_end_runXML(endrun_xml_8448)

