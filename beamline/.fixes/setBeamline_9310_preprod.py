import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
#####_MASTER_CDB = "http://172.16.246.25:8080"
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 9310

startrun_xml_9310 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='9310' startTime='2017-05-27 12:16:31.551793' startNotes='reference run, GNe' optics='PionReference-DS' startPulse='4852515' step='4.0' status='false' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.0005' daqVersion='DATE_v7.66 EqList_v1.0.0-1-gf902e9e' gdcHostName='miceraid5' targetDelay='500000.0' targetDepth='38.0' targetDriveVoltage='65.0'><ldcHost name='miceacq20'/><ldcHost name='miceacq17'/><ldcHost name='miceacq16'/><ldcHost name='miceacq15'/><ldcHost name='miceacq14'/> </startRun>"

print bl.set_start_runXML(startrun_xml_9310)


###################################
# now set beamline for Run 9310

beamline_xml_9310 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='9310' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='D1' setCurrent='203.024994' polarity='1'/><magnet name='D2' setCurrent='104.795998' polarity='1'/><magnet name='DS' setCurrent='442.849609' polarity='1'/><magnet name='Q1' setCurrent='67.93' polarity='1'/><magnet name='Q2' setCurrent='84.93' polarity='1'/><magnet name='Q3' setCurrent='59.0' polarity='1'/><magnet name='Q4' setCurrent='176.807999' polarity='1'/><magnet name='Q5' setCurrent='237.147995' polarity='1'/><magnet name='Q6' setCurrent='157.212006' polarity='1'/><magnet name='Q7' setCurrent='157.660004' polarity='1'/><magnet name='Q8' setCurrent='238.539993' polarity='1'/><magnet name='Q9' setCurrent='203.712006' polarity='1'/> </beamline>"

print bl.set_beamlineXML(beamline_xml_9310)

###################################
# now set end of run for Run 9310

endrun_xml_9310 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='9310' endTime='2017-05-27 12:37:41.206588' endNotes='reference run end' status='0' endPulse='4853507' overwrite='0' ><scalar name='GVa1 Triggers' value='977'/><scalar name='LMC-1234 Count' value='105397'/><scalar name='LMC-12 Count' value='836122'/><scalar name='LMC-34 Count' value='811201'/><scalar name='Particle Triggers' value='75569'/><scalar name='Requested Triggers' value='122957'/><scalar name='ToF0 Triggers' value='414696'/><scalar name='ToF1 Triggers' value='122951'/><scalar name='ToF2 Triggers' value='21392'/><isisBeam name='IBML-S8.1' mean='4.031507' sigma='0.103391'/><isisBeam name='IBML-S7.4' mean='1.25782' sigma='0.03271'/><isisBeam name='IBML-S7.3' mean='1.762283' sigma='0.038945'/><isisBeam name='IBML-TOT' mean='7.051621' sigma='0.175046'/></endRun>"

print bl.set_end_runXML(endrun_xml_9310)


