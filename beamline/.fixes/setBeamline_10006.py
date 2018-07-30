import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"
####bl = BeamlineSuperMouse(_MASTER_CDB)
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 10006

startrun_xml_10006 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='10006' startTime='2017-10-16 17:42:03.206314' startNotes='Manual CDB insert' optics='6-140+M3-Test2' startPulse='0' step='4.000000' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

print bl.set_start_runXML(startrun_xml_10006)

###################################
# now set beamline for Run 10006

beamline_xml_10006 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='10006' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='D1' setCurrent='160.820007' polarity='1'/><magnet name='D2' setCurrent='86.547997' polarity='1'/><magnet name='DS' setCurrent='352.846863' polarity='1'/><magnet name='Q1' setCurrent='54.16' polarity='1'/><magnet name='Q2' setCurrent='67.580002' polarity='1'/><magnet name='Q3' setCurrent='46.970001' polarity='1'/><magnet name='Q4' setCurrent='144.731995' polarity='1'/><magnet name='Q5' setCurrent='194.031998' polarity='1'/><magnet name='Q6' setCurrent='128.615997' polarity='1'/><magnet name='Q7' setCurrent='124.919998' polarity='1'/><magnet name='Q8' setCurrent='188.944' polarity='1'/><magnet name='Q9' setCurrent='161.240005' polarity='1'/> </beamline>"

print bl.set_beamlineXML(beamline_xml_10006)

###################################
# now set end of run for Run 10006

endrun_xml_10006 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='10006' endTime='2017-10-16 17:46:29.341314' endNotes='Manual CDB insert' status='0' endPulse='0' overwrite='0' > <isisBeam name='IBML-TOT' mean='0' sigma='0'/> <isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/> <scalar name='GVa1 Triggers' value='177'/><scalar name='LMC-1234 Count' value='23266'/><scalar name='LMC-12 Count' value='200492'/><scalar name='LMC-34 Count' value='190584'/><scalar name='Particle Triggers' value='10004'/><scalar name='Requested Triggers' value='13723'/><scalar name='ToF0 Triggers' value='58691'/><scalar name='ToF1 Triggers' value='13723'/><scalar name='ToF2 Triggers' value='8575'/> </endRun>"

print bl.set_end_runXML(endrun_xml_10006)


