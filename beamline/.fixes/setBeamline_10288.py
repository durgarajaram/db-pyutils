import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"
####bl = BeamlineSuperMouse(_MASTER_CDB)
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 10288

startrun_xml_10288 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='10288' startTime='2017-11-26 16:38:51.491814' startNotes='Task H50a start' optics='3-140+M3-Test3' startPulse='0' step='4.000000' runType='Pulser Data' daqTrigger='PULSER' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

print bl.set_start_runXML(startrun_xml_10288)

###################################
# now set beamline for Run 10288

beamline_xml_10288 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='10288' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='29' ><magnet name='D1' setCurrent='146.494995' polarity='1'/><magnet name='D2' setCurrent='71.914001' polarity='1'/><magnet name='DS' setCurrent='326.364288' polarity='1'/><magnet name='Q1' setCurrent='49.369999' polarity='1'/><magnet name='Q2' setCurrent='61.59' polarity='1'/><magnet name='Q3' setCurrent='42.73' polarity='1'/><magnet name='Q4' setCurrent='134.876007' polarity='1'/><magnet name='Q5' setCurrent='180.839996' polarity='1'/><magnet name='Q6' setCurrent='119.860001' polarity='1'/><magnet name='Q7' setCurrent='114.444' polarity='1'/><magnet name='Q8' setCurrent='173.076004' polarity='1'/><magnet name='Q9' setCurrent='147.591995' polarity='1'/></beamline>"

print bl.set_beamlineXML(beamline_xml_10288)

###################################
# now set end of run for Run 10288

endrun_xml_10288 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='10288' endTime='2017-11-26 18:07:55.413541' endNotes='Task H50a end' status='0' endPulse='0' overwrite='0' > <isisBeam name='IBML-TOT' mean='0' sigma='0'/> <isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/><scalar name='GVa1 Triggers' value='4342'/><scalar name='LMC-1234 Count' value='1404936'/><scalar name='LMC-12 Count' value='10344030'/><scalar name='LMC-34 Count' value='10154953'/><scalar name='Particle Triggers' value='347347'/><scalar name='Requested Triggers' value='533985'/><scalar name='ToF0 Triggers' value='2484218'/><scalar name='ToF1 Triggers' value='533968'/><scalar name='ToF2 Triggers' value='301324'/></endRun>"

print bl.set_end_runXML(endrun_xml_10288)

