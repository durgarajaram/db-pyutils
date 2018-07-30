import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
#####_MASTER_CDB = "http://172.16.246.25:8080"
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 9288

startrun_xml_9288 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='9288' startTime='2017-05-08 12:09:48.04657' startNotes='LH2 Empty Reference Run' optics='PionReference-DS' startPulse='4809949' step='4.0' status='false' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.0005' daqVersion='DATE_v7.66 EqList_v1.0.0-1-gf902e9e' gdcHostName='miceraid5' targetDelay='500000.0' targetDepth='38.0' targetDriveVoltage='65.0'><ldcHost name='miceacq20'/><ldcHost name='miceacq17'/><ldcHost name='miceacq16'/><ldcHost name='miceacq15'/><ldcHost name='miceacq14'/> </startRun>"

print bl.set_start_runXML(startrun_xml_9288)


###################################
# now set beamline for Run 9288

beamline_xml_9288 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='9288' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='D1' setCurrent='203.024994' polarity='1'/><magnet name='D2' setCurrent='104.795998' polarity='1'/><magnet name='DS' setCurrent='442.849609' polarity='1'/><magnet name='Q1' setCurrent='67.93' polarity='1'/><magnet name='Q2' setCurrent='84.93' polarity='1'/><magnet name='Q3' setCurrent='59.0' polarity='1'/><magnet name='Q4' setCurrent='176.807999' polarity='1'/><magnet name='Q5' setCurrent='237.147995' polarity='1'/><magnet name='Q6' setCurrent='157.212006' polarity='1'/><magnet name='Q7' setCurrent='157.660004' polarity='1'/><magnet name='Q8' setCurrent='238.539993' polarity='1'/><magnet name='Q9' setCurrent='203.712006' polarity='1'/> </beamline>"

print bl.set_beamlineXML(beamline_xml_9288)

###################################
# now set end of run for Run 9288

endrun_xml_9288 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='9288' endTime='2017-05-08 12:14:50.801637' endNotes='LH2 Empty Reference Run- stopped fr daq' status='0' endPulse='4810186' overwrite='0' > <scalar name='GVa1 Triggers' value='221'/><scalar name='LMC-1234 Count' value='12610'/><scalar name='LMC-12 Count' value='101091'/><scalar name='LMC-34 Count' value='98589'/><scalar name='Particle Triggers' value='8901'/><scalar name='Requested Triggers' value='15171'/><scalar name='ToF0 Triggers' value='52965'/><scalar name='ToF1 Triggers' value='15172'/><scalar name='ToF2 Triggers' value='2582'/><isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/><isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/><isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/><isisBeam name='IBML-TOT' mean='0.0' sigma='0.0'/> </endRun>"

print bl.set_end_runXML(endrun_xml_9288)

