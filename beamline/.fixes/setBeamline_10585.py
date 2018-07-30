import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"
bl = BeamlineSuperMouse(_MASTER_CDB)
#bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 10585

startrun_xml_10585 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='10585' startTime='2017-12-19 05:44:51.541482' startNotes='H64c run - wedge absorber - start run' optics='6-140+M3-Test2' startPulse='8058518' step='4.000000' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v1.0.0-1-gf902e9e' gdcHostName='miceraid5' targetDelay='500000.000000' targetDepth='36.349998' targetDriveVoltage='65.000000' overwrite='0'></startRun>"

#print bl.set_start_runXML(startrun_xml_10585)

###################################
# now set beamline for Run 10585

beamline_xml_10585 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='10585' beamStop='true' diffuserThickness='4'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='Q9' polarity='1' setCurrent='146.60' /> <magnet name='Q8' polarity='1' setCurrent='171.87' /> <magnet name='Q7' polarity='1' setCurrent='113.68' /> <magnet name='Q6' polarity='1' setCurrent='119.02' /> <magnet name='Q5' polarity='1' setCurrent='179.63' /> <magnet name='Q4' polarity='1' setCurrent='133.95' /> <magnet name='D2' polarity='1' setCurrent='76.40' /> <magnet name='DS' polarity='1' setCurrent='323.79' /> <magnet name='D1' polarity='1' setCurrent='153.01' /> <magnet name='Q3' polarity='1' setCurrent='43.40' /> <magnet name='Q2' polarity='1' setCurrent='62.51' /> <magnet name='Q1' polarity='1' setCurrent='50.06' /> </beamline>"

#print bl.set_beamlineXML(beamline_xml_10585)

###################################
# now set end of run for Run 10585

endrun_xml_10585 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='10585' endTime='2017-12-19 06:00:19.746630' endNotes='H64c run - wedge absorber - start run' status='0' endPulse='8059243' overwrite='0' > <isisBeam name='IBML-TOT' mean='5.104181' sigma='0.024849'/> <isisBeam name='IBML-S8.1' mean='2.013904' sigma='0.009734'/> <isisBeam name='IBML-S7.4' mean='1.364189' sigma='0.006550'/> <isisBeam name='IBML-S7.3' mean='1.726088' sigma='0.008566'/> <scalar name='LMC-1234 Count' value='270971' /> <scalar name='LMC-12 Count' value='1850729' /> <scalar name='LMC-34 Count' value='1834083' /> <scalar name='ToF2 Triggers' value='49968' /> <scalar name='ToF1 Triggers' value='96340' /> <scalar name='ToF0 Triggers' value='415691' /> <scalar name='GVa1 Triggers' value='739' /> <scalar name='Requested Triggers' value='96344' /> <scalar name='Particle Triggers' value='59963' /> </endRun>"

print bl.set_end_runXML(endrun_xml_10585)


