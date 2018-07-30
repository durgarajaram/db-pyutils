import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"
bl = BeamlineSuperMouse(_MASTER_CDB)
#bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 10379

startrun_xml_10379 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='10379' startTime='2017-12-02 19:00:00.006000' startNotes='Manual CDB insert' optics='10-200+M3-Test1' startPulse='0' step='4.000000' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

print bl.set_start_runXML(startrun_xml_10379)

###################################
# now set beamline for Run 10379

beamline_xml_10379 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='10379' beamStop='true' diffuserThickness='15'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='Q9' polarity='1' setCurrent='194.4' /> <magnet name='Q8' polarity='1' setCurrent='227.01' /> <magnet name='Q7' polarity='1' setCurrent='150.46' /> <magnet name='Q6' polarity='1' setCurrent='165.7' /> <magnet name='Q5' polarity='1' setCurrent='249.84' /> <magnet name='Q4' polarity='1' setCurrent='186.24' /> <magnet name='D2' polarity='1' setCurrent='108.01' /> <magnet name='DS' polarity='1' setCurrent='455.36' /> <magnet name='D1' polarity='1' setCurrent='214.01' /> <magnet name='Q3' polarity='1' setCurrent='60.7' /> <magnet name='Q2' polarity='1' setCurrent='87.34' /> <magnet name='Q1' polarity='1' setCurrent='69.94' /> </beamline>"

print bl.set_beamlineXML(beamline_xml_10379)

###################################
# now set end of run for Run 10379

endrun_xml_10379 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='10379' endTime='2017-12-02 19:57:00.000000' endNotes='Manual CDB insert' status='0' endPulse='0' overwrite='0' > <isisBeam name='IBML-TOT' mean='0' sigma='0'/> <isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/> <scalar name='LMC-1234 Count' value='0' /> <scalar name='LMC-12 Count' value='0' /> <scalar name='LMC-34 Count' value='0' /> <scalar name='ToF2 Triggers' value='0' /> <scalar name='ToF1 Triggers' value='41141' /> <scalar name='ToF0 Triggers' value='0' /> <scalar name='GVa1 Triggers' value='0' /> <scalar name='Requested Triggers' value='0' /> <scalar name='Particle Triggers' value='345000' /> </endRun>"

print bl.set_end_runXML(endrun_xml_10379)


