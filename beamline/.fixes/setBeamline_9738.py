import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
####_MASTER_CDB = "http://172.16.246.25:8080"
####bl = BeamlineSuperMouse(_MASTER_CDB)
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 9738

startrun_xml_9738 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='9738' startTime='2017-09-26 19:56:48.892527' startNotes='H23a H2 full 3-140 test3' optics='3-140+M3-Test3' startPulse='0' step='4.000000' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /></startRun>"

print bl.set_start_runXML(startrun_xml_9738)

###################################
# now set beamline for Run 9738

beamline_xml_9738 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='9738' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='D1' setCurrent='146.494995' polarity='1'/><magnet name='D2' setCurrent='71.917999' polarity='1'/><magnet name='DS' setCurrent='326.647064' polarity='1'/><magnet name='Q1' setCurrent='49.369999' polarity='1'/><magnet name='Q2' setCurrent='61.599998' polarity='1'/><magnet name='Q3' setCurrent='42.720001' polarity='1'/><magnet name='Q4' setCurrent='134.876007' polarity='1'/><magnet name='Q5' setCurrent='180.843994' polarity='1'/><magnet name='Q6' setCurrent='119.872002' polarity='1'/><magnet name='Q7' setCurrent='114.444' polarity='1'/><magnet name='Q8' setCurrent='173.076004' polarity='1'/><magnet name='Q9' setCurrent='147.595993' polarity='1'/> </beamline>"

print bl.set_beamlineXML(beamline_xml_9738)

###################################
# now set end of run for Run 9738

endrun_xml_9738 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='9738' endTime='2017-09-26 22:38:31.56399' endNotes='H23a H2 full 3-140 test3' status='0' endPulse='0' overwrite='0' > <isisBeam name='IBML-TOT' mean='0' sigma='0'/> <isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/><scalar name='GVa1 Triggers' value='4524'/><scalar name='LMC-1234 Count' value='1104175'/><scalar name='LMC-12 Count' value='8798740'/><scalar name='LMC-34 Count' value='8404946'/><scalar name='Particle Triggers' value='325767'/><scalar name='Requested Triggers' value='470207'/><scalar name='ToF0 Triggers' value='2143625'/><scalar name='ToF1 Triggers' value='470200'/><scalar name='ToF2 Triggers' value='258216'/> </endRun>"


print bl.set_end_runXML(endrun_xml_9738)

