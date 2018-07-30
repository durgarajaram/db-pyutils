import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"
####bl = BeamlineSuperMouse(_MASTER_CDB)
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 10299

startrun_xml_10299 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='10299' startTime='2017-11-27 16:40:04.067249' startNotes='Manual CDB insert' optics='10-140+M3-Test4' startPulse='0' step='4.000000' runType='Pulser Data' daqTrigger='PULSER' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

print bl.set_start_runXML(startrun_xml_10299)

###################################
# now set beamline for Run 10299

beamline_xml_10299 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='10299' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='D1' setCurrent='0.01' polarity='0'/><magnet name='D2' setCurrent='0.02' polarity='0'/><magnet name='DS' setCurrent='198.805496' polarity='0'/><magnet name='Q1' setCurrent='0.0' polarity='0'/><magnet name='Q2' setCurrent='-0.02' polarity='0'/><magnet name='Q3' setCurrent='-0.02' polarity='0'/><magnet name='Q4' setCurrent='0.076' polarity='0'/><magnet name='Q5' setCurrent='0.056' polarity='0'/><magnet name='Q6' setCurrent='0.056' polarity='0'/><magnet name='Q7' setCurrent='0.052' polarity='0'/><magnet name='Q8' setCurrent='0.024' polarity='0'/><magnet name='Q9' setCurrent='0.048' polarity='0'/> </beamline>"

print bl.set_beamlineXML(beamline_xml_10299)

###################################
# now set end of run for Run 10299

endrun_xml_10299 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='10299' endTime='2017-11-27 16:40:59.087442' endNotes='Manual CDB insert' status='0' endPulse='0' overwrite='0' > <isisBeam name='IBML-TOT' mean='0' sigma='0'/> <isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/> scalar name='GVa1 Triggers' value='11'/><scalar name='LMC-1234 Count' value='0'/><scalar name='LMC-12 Count' value='21'/><scalar name='LMC-34 Count' value='18'/><scalar name='Particle Triggers' value='233'/><scalar name='Requested Triggers' value='660'/><scalar name='ToF0 Triggers' value='2'/><scalar name='ToF1 Triggers' value='1'/><scalar name='ToF2 Triggers' value='2'/> </endRun>"

print bl.set_end_runXML(endrun_xml_10299)

