import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"
####bl = BeamlineSuperMouse(_MASTER_CDB)
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 10515

startrun_xml_10515 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='10515' startTime='2017-12-14 20:19:58.583392' startNotes='S18a - wedge - start' optics='3-170+M3-Test1' startPulse='0' step='4.000000' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

print bl.set_start_runXML(startrun_xml_10515)

###################################
# now set beamline for Run 10515

beamline_xml_10515 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='10515' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='29' ><magnet name='D1' setCurrent='160.815002' polarity='1'/><magnet name='D2' setCurrent='86.543999' polarity='1'/><magnet name='DS' setCurrent='352.26178' polarity='1'/><magnet name='Q1' setCurrent='54.16' polarity='1'/><magnet name='Q2' setCurrent='67.57' polarity='1'/><magnet name='Q3' setCurrent='46.959999' polarity='1'/><magnet name='Q4' setCurrent='144.727997' polarity='1'/><magnet name='Q5' setCurrent='194.024002' polarity='1'/><magnet name='Q6' setCurrent='128.608002' polarity='1'/><magnet name='Q7' setCurrent='124.916' polarity='1'/><magnet name='Q8' setCurrent='188.944' polarity='1'/><magnet name='Q9' setCurrent='161.235992' polarity='1'/></beamline>"

print bl.set_beamlineXML(beamline_xml_10515)

###################################
# now set end of run for Run 10515

endrun_xml_10515 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='10515' endTime='2017-12-14 20:31:02.185239' endNotes='S18a - wedge - stop 500 spills' status='0' endPulse='0' overwrite='0' > <isisBeam name='IBML-TOT' mean='0' sigma='0'/> <isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/><scalar name='GVa1 Triggers' value='539'/><scalar name='LMC-1234 Count' value='110316'/><scalar name='LMC-12 Count' value='820288'/><scalar name='LMC-34 Count' value='791973'/><scalar name='Particle Triggers' value='31040'/><scalar name='Requested Triggers' value='46353'/><scalar name='ToF0 Triggers' value='208095'/><scalar name='ToF1 Triggers' value='46353'/><scalar name='ToF2 Triggers' value='6122'/></endRun>"

print bl.set_end_runXML(endrun_xml_10515)

