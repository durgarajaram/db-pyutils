import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"
####bl = BeamlineSuperMouse(_MASTER_CDB)
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 10051

startrun_xml_10051 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='10051' startTime='2017-10-22 10:50:17.718776' startNotes='Manual CDB insert' optics='6-140+M3-Test2' startPulse='0' step='4.000000' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

print bl.set_start_runXML(startrun_xml_10051)

###################################
# now set beamline for Run 10051

beamline_xml_10051 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='10051' beamStop='true' diffuserThickness='4'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='D1' setCurrent='153.014999' polarity='1'/><magnet name='D2' setCurrent='76.400002' polarity='1'/><magnet name='DS' setCurrent='323.612122' polarity='1'/><magnet name='Q1' setCurrent='50.060001' polarity='1'/><magnet name='Q2' setCurrent='62.509998' polarity='1'/><magnet name='Q3' setCurrent='43.400002' polarity='1'/><magnet name='Q4' setCurrent='133.960007' polarity='1'/><magnet name='Q5' setCurrent='179.636002' polarity='1'/><magnet name='Q6' setCurrent='119.019997' polarity='1'/><magnet name='Q7' setCurrent='113.68' polarity='1'/><magnet name='Q8' setCurrent='171.876007' polarity='1'/><magnet name='Q9' setCurrent='146.595993' polarity='1'/> </beamline>"

print bl.set_beamlineXML(beamline_xml_10051)

###################################
# now set end of run for Run 10051

endrun_xml_10051 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='10051' endTime='2017-10-22 11:51:35.704165' endNotes='Manual CDB insert' status='0' endPulse='0' overwrite='0' > <isisBeam name='IBML-TOT' mean='0' sigma='0'/> <isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/> <scalar name='GVa1 Triggers' value='2894'/><scalar name='LMC-1234 Count' value='765268'/><scalar name='LMC-12 Count' value='5693850'/><scalar name='LMC-34 Count' value='5450610'/><scalar name='Particle Triggers' value='206693'/><scalar name='Requested Triggers' value='315815'/><scalar name='ToF0 Triggers' value='1349174'/><scalar name='ToF1 Triggers' value='315806'/><scalar name='ToF2 Triggers' value='187624'/> </endRun>"

print bl.set_end_runXML(endrun_xml_10051)


