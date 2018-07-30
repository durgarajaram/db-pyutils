import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
####_MASTER_CDB = "http://172.16.246.25:8080"
####bl = BeamlineSuperMouse(_MASTER_CDB)
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 9721

startrun_xml_9721 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='9721' startTime='2017-09-25 23:46:42.209542' startNotes='140MeV/c test run H22.5' optics='Individual Settings' startPulse='0' step='4.000000' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /></startRun>"

print bl.set_start_runXML(startrun_xml_9721)

###################################
# now set beamline for Run 9721

beamline_xml_9721 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='9721' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='D1' setCurrent='146.494995' polarity='1'/><magnet name='D2' setCurrent='71.916' polarity='1'/><magnet name='DS' setCurrent='326.824249' polarity='1'/><magnet name='Q1' setCurrent='49.360001' polarity='1'/><magnet name='Q2' setCurrent='61.59' polarity='1'/><magnet name='Q3' setCurrent='42.720001' polarity='1'/><magnet name='Q4' setCurrent='178.820007' polarity='1'/><magnet name='Q5' setCurrent='188.539993' polarity='1'/><magnet name='Q6' setCurrent='96.519997' polarity='1'/><magnet name='Q7' setCurrent='87.540001' polarity='1'/><magnet name='Q8' setCurrent='227.688004' polarity='1'/><magnet name='Q9' setCurrent='155.395996' polarity='1'/></beamline>"

print bl.set_beamlineXML(beamline_xml_9721)

###################################
# now set end of run for Run 9721

endrun_xml_9721 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='9721' endTime='2017-09-26 00:16:47.806926' endNotes='Manual CDB insert' status='0' endPulse='0' overwrite='0' > <isisBeam name='IBML-TOT' mean='0' sigma='0'/> <isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/><scalar name='LMC-12 Count' value='788183'/><scalar name='LMC-34 Count' value='751874'/><scalar name='Particle Triggers' value='19037'/><scalar name='Requested Triggers' value='25332'/><scalar name='ToF0 Triggers' value='189456'/><scalar name='ToF1 Triggers' value='25251'/><scalar name='ToF2 Triggers' value='6050'/> </endRun>"

print bl.set_end_runXML(endrun_xml_9721)

