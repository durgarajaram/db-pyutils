import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
#####_MASTER_CDB = "http://172.16.246.25:8080"
bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 8449

startrun_xml_8449 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='8449' startTime='2016-10-25 12:07:06.631133' startNotes='Restarting task 3 170 MeV. ISIS back ' optics='3-170+M3-Test1' startPulse='2909968' step='4.0' status='false' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.0005' daqVersion='DATE_v7.66 EqList_v1.0.0-1-gf902e9e' gdcHostName='miceraid5' targetDelay='0.0' targetDepth='0.0' targetDriveVoltage='0.0'><ldcHost name='miceacq20'/><ldcHost name='miceacq17'/><ldcHost name='miceacq16'/><ldcHost name='miceacq15'/><ldcHost name='miceacq14'/> </startRun>"

print bl.set_start_runXML(startrun_xml_8449)


###################################
# now set beamline for Run 8449

beamline_xml_8449 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='8449' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='D1' setCurrent='160.800003' polarity='1'/><magnet name='D2' setCurrent='86.545998' polarity='1'/><magnet name='DS' setCurrent='352.738464' polarity='1'/><magnet name='Q1' setCurrent='54.150002' polarity='1'/><magnet name='Q2' setCurrent='67.57' polarity='1'/><magnet name='Q3' setCurrent='46.959999' polarity='1'/><magnet name='Q4' setCurrent='144.731995' polarity='1'/><magnet name='Q5' setCurrent='194.024002' polarity='1'/><magnet name='Q6' setCurrent='128.612' polarity='1'/><magnet name='Q7' setCurrent='124.916' polarity='1'/><magnet name='Q8' setCurrent='188.936005' polarity='1'/><magnet name='Q9' setCurrent='161.244003' polarity='1'/> </beamline>"

print bl.set_beamlineXML(beamline_xml_8449)

###################################
# now set end of run for Run 8449

endrun_xml_8449 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='8449' endTime='2016-10-25 14:22:20.600033' endNotes='Task 3 170 MeV complete.' status='0' endPulse='2916307' overwrite='0' > <scalar name='GVa1 Triggers' value='6318'/><scalar name='LMC-1234 Count' value='936636'/><scalar name='LMC-12 Count' value='6103856'/><scalar name='LMC-34 Count' value='5750747'/><scalar name='Particle Triggers' value='266735'/><scalar name='Requested Triggers' value='338786'/><scalar name='ToF0 Triggers' value='1505656'/><scalar name='ToF1 Triggers' value='338776'/><scalar name='ToF2 Triggers' value='105834'/><isisBeam name='IBML-S8.1' mean='1.117761' sigma='0.001884'/><isisBeam name='IBML-S7.4' mean='0.367908' sigma='7.12E-4'/><isisBeam name='IBML-S7.3' mean='0.610299' sigma='0.00106'/><isisBeam name='IBML-TOT' mean='2.095967' sigma='0.001536'/> </endRun>"

print bl.set_end_runXML(endrun_xml_8449)

