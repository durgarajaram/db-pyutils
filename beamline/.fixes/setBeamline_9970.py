import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"
####bl = BeamlineSuperMouse(_MASTER_CDB)
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 9970

startrun_xml_9970 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='9970' startTime='2017-10-14 08:03:13.970382' startNotes='Manual CDB insert' optics='10-140+M3-Test4' startPulse='0' step='4.000000' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

print bl.set_start_runXML(startrun_xml_9970)

###################################
# now set beamline for Run 9970

beamline_xml_9970 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='9970' beamStop='true' diffuserThickness='15'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='D1' setCurrent='173.835007' polarity='1'/><magnet name='D2' setCurrent='86.973999' polarity='1'/><magnet name='DS' setCurrent='387.932556' polarity='1'/><magnet name='Q1' setCurrent='58.580002' polarity='1'/><magnet name='Q2' setCurrent='73.110001' polarity='1'/><magnet name='Q3' setCurrent='50.75' polarity='1'/><magnet name='Q4' setCurrent='156.287994' polarity='1'/><magnet name='Q5' setCurrent='209.632004' polarity='1'/><magnet name='Q6' setCurrent='138.992004' polarity='1'/><magnet name='Q7' setCurrent='102.667999' polarity='1'/><magnet name='Q8' setCurrent='155.231995' polarity='1'/><magnet name='Q9' setCurrent='132.496002' polarity='1'/> </beamline>"

print bl.set_beamlineXML(beamline_xml_9970)

###################################
# now set end of run for Run 9970

endrun_xml_9970 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='9970' endTime='2017-10-14 09:19:50.345286' endNotes='Manual CDB insert' status='0' endPulse='0' overwrite='0' > <isisBeam name='IBML-TOT' mean='0' sigma='0'/> <isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/> <scalar name='GVa1 Triggers' value='3571'/><scalar name='LMC-1234 Count' value='745165'/><scalar name='LMC-12 Count' value='6388427'/><scalar name='LMC-34 Count' value='6120946'/><scalar name='Particle Triggers' value='425576'/><scalar name='Requested Triggers' value='685920'/><scalar name='ToF0 Triggers' value='2502995'/><scalar name='ToF1 Triggers' value='685893'/><scalar name='ToF2 Triggers' value='171709'/> </endRun>"

print bl.set_end_runXML(endrun_xml_9970)


