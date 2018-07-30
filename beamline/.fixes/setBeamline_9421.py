import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"
#bl = BeamlineSuperMouse(_MASTER_CDB)
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 9421

startrun_xml_9421 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='9421' startTime='2017-09-07 09:48:11.224337' startNotes='Manual CDB insert' optics='PionReference-DS' startPulse='0' step='4.000000' runType='Special Run' daqTrigger='PULSER' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

print bl.set_start_runXML(startrun_xml_9421)

###################################
# now set beamline for Run 9421

beamline_xml_9421 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='9421' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='Q9' polarity='1' setCurrent='0.0' /> <magnet name='Q8' polarity='1' setCurrent='0.0' /> <magnet name='Q7' polarity='1' setCurrent='0.0' /> <magnet name='Q6' polarity='1' setCurrent='0.0' /> <magnet name='Q5' polarity='1' setCurrent='0.0' /> <magnet name='Q4' polarity='1' setCurrent='0.0' /> <magnet name='D2' polarity='1' setCurrent='0.0' /> <magnet name='DS' polarity='1' setCurrent='20.5' /> <magnet name='D1' polarity='1' setCurrent='0.0' /> <magnet name='Q3' polarity='1' setCurrent='0.0' /> <magnet name='Q2' polarity='1' setCurrent='0.0' /> <magnet name='Q1' polarity='1' setCurrent='0.0' /> </beamline>"

print bl.set_beamlineXML(beamline_xml_9421)

###################################
# now set end of run for Run 9421

endrun_xml_9421 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='9421' endTime='2017-09-07 09:55:04.921446' endNotes='Manual CDB insert' status='0' endPulse='0' overwrite='0' > <isisBeam name='IBML-TOT' mean='0' sigma='0'/> <isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/> <scalar name='LMC-1234 Count' value='0' /> <scalar name='LMC-12 Count' value='0' /> <scalar name='LMC-34 Count' value='0' /> <scalar name='ToF2 Triggers' value='0' /> <scalar name='ToF1 Triggers' value='0' /> <scalar name='ToF0 Triggers' value='0' /> <scalar name='GVa1 Triggers' value='0' /> <scalar name='Requested Triggers' value='0' /> <scalar name='Particle Triggers' value='53726' /> </endRun>"

print bl.set_end_runXML(endrun_xml_9421)


