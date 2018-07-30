import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
#####_MASTER_CDB = "http://172.16.246.25:8080"
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 8410

startrun_xml_8410 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='8410' startTime='2016-10-18 07:41:08.030242' startNotes='start of shift' optics='PionReference-NoDS' startPulse='2827625' step='4.0' status='false' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.0005' daqVersion='DATE_v7.66 EqList_v1.0.0-1-gf902e9e' gdcHostName='miceraid5' targetDelay='0.0' targetDepth='0.0' targetDriveVoltage='0.0'><ldcHost name='miceacq20'/><ldcHost name='miceacq17'/><ldcHost name='miceacq16'/><ldcHost name='miceacq15'/><ldcHost name='miceacq14'/> </startRun>"

print bl.set_start_runXML(startrun_xml_8410)

###################################
# now set beamline for Run 8410

beamline_xml_8410 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='8410' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='D1' setCurrent='202.835007' polarity='1'/><magnet name='D2' setCurrent='100.405998' polarity='1'/><magnet name='DS' setCurrent='19.584475' polarity='1'/><magnet name='Q1' setCurrent='57.830002' polarity='1'/><magnet name='Q2' setCurrent='105.709999' polarity='1'/><magnet name='Q3' setCurrent='64.589996' polarity='1'/><magnet name='Q4' setCurrent='176.919998' polarity='1'/><magnet name='Q5' setCurrent='237.151993' polarity='1'/><magnet name='Q6' setCurrent='157.220001' polarity='1'/><magnet name='Q7' setCurrent='157.660004' polarity='1'/><magnet name='Q8' setCurrent='238.544006' polarity='1'/><magnet name='Q9' setCurrent='203.723999' polarity='1'/> </beamline>"

print bl.set_beamlineXML(beamline_xml_8410)

###################################
# now set end of run for Run 8410

endrun_xml_8410 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='8410' endTime='2016-10-18 07:47:02.715884' endNotes='start of shift - notriggers' status='0' endPulse='2827806' overwrite='0' > <scalar name='LMC-1234 Count' value='868'/><scalar name='LMC-12 Count' value='6335'/><scalar name='LMC-34 Count' value='5635'/><scalar name='Particle Triggers' value='0'/><scalar name='Requested Triggers' value='0'/><scalar name='ToF0 Triggers' value='0'/><scalar name='ToF1 Triggers' value='0'/><scalar name='ToF2 Triggers' value='0'/><isisBeam name='IBML-S8.1' mean='16.63954' sigma='5.194544'/><isisBeam name='IBML-S7.4' mean='5.346002' sigma='1.664406'/><isisBeam name='IBML-S7.3' mean='8.819445' sigma='2.939815'/><isisBeam name='IBML-TOT' mean='30.804985' sigma='9.798765'/> </endRun>"

print bl.set_end_runXML(endrun_xml_8410)

