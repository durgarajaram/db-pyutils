import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"
####bl = BeamlineSuperMouse(_MASTER_CDB)
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 10476

startrun_xml_10476 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='10476' startTime='2017-12-11 10:42:01.993876' startNotes='Manual CDB insert' optics='3-240+M0' startPulse='0' step='4.000000' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

print bl.set_start_runXML(startrun_xml_10476)

###################################
# now set beamline for Run 10476

beamline_xml_10476 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='10476' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='131' > <magnet name='D2' setCurrent='0.018' polarity='0'/><magnet name='DS' setCurrent='198.472427' polarity='0'/><magnet name='Q1' setCurrent='0.01' polarity='0'/><magnet name='Q2' setCurrent='-0.01' polarity='0'/><magnet name='Q3' setCurrent='-0.02' polarity='0'/><magnet name='Q4' setCurrent='0.08' polarity='0'/><magnet name='Q5' setCurrent='0.056' polarity='0'/><magnet name='Q6' setCurrent='0.056' polarity='0'/><magnet name='Q7' setCurrent='0.06' polarity='0'/><magnet name='Q8' setCurrent='0.02' polarity='0'/><magnet name='Q9' setCurrent='0.044' polarity='0'/> </beamline>"

print bl.set_beamlineXML(beamline_xml_10476)

###################################
# now set end of run for Run 10476

endrun_xml_10476 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='10476' endTime='2017-12-11 10:43:28.940621' endNotes='Manual CDB insert' status='0' endPulse='0' overwrite='0' > <isisBeam name='IBML-TOT' mean='0' sigma='0'/> <isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/> <scalar name='GVa1 Triggers' value='60'/><scalar name='LMC-1234 Count' value='21'/><scalar name='LMC-12 Count' value='234'/><scalar name='LMC-34 Count' value='183'/><scalar name='Particle Triggers' value='1195'/><scalar name='Requested Triggers' value='3120'/><scalar name='ToF0 Triggers' value='7'/><scalar name='ToF1 Triggers' value='1'/><scalar name='ToF2 Triggers' value='7'/> </endRun>"

print bl.set_end_runXML(endrun_xml_10476)

