import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"
bl = BeamlineSuperMouse(_MASTER_CDB)
#bl = BeamlineSuperMouse(_TEST_CDB)

###################################
# set Start of Run for Run 10382

startrun_xml_10382 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='10382' startTime='2017-12-02 20:49:00.000000' startNotes='Manual CDB insert' optics='DiffMask8-3-200+M3-Test1' startPulse='0' step='4.000000' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

print bl.set_start_runXML(startrun_xml_10382)

###################################
# now set beamline for Run 10382

beamline_xml_10382 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='10382' beamStop='true' diffuserThickness='8'  overwrite='0'  protonAbsorberThickness='49' > <magnet name='Q9' polarity='1' setCurrent='90.45' /> <magnet name='Q8' polarity='1' setCurrent='105.98' /> <magnet name='Q7' polarity='1' setCurrent='70.03' /> <magnet name='Q6' polarity='1' setCurrent='141.77' /> <magnet name='Q5' polarity='1' setCurrent='213.86' /> <magnet name='Q4' polarity='1' setCurrent='159.45' /> <magnet name='D2' polarity='1' setCurrent='94.91' /> <magnet name='DS' polarity='1' setCurrent='395.22' /> <magnet name='D1' polarity='1' setCurrent='205.0' /> <magnet name='Q3' polarity='1' setCurrent='52.73' /> <magnet name='Q2' polarity='1' setCurrent='75.86' /> <magnet name='Q1' polarity='1' setCurrent='60.77' /> </beamline>"

print bl.set_beamlineXML(beamline_xml_10382)

###################################
# now set end of run for Run 10382

endrun_xml_10382 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='10382' endTime='2017-12-02 21:51:00.000000' endNotes='Manual CDB insert' status='0' endPulse='0' overwrite='0' > <isisBeam name='IBML-TOT' mean='0' sigma='0'/> <isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/> <scalar name='LMC-1234 Count' value='0' /> <scalar name='LMC-12 Count' value='0' /> <scalar name='LMC-34 Count' value='0' /> <scalar name='ToF2 Triggers' value='0' /> <scalar name='ToF1 Triggers' value='41141' /> <scalar name='ToF0 Triggers' value='0' /> <scalar name='GVa1 Triggers' value='0' /> <scalar name='Requested Triggers' value='0' /> <scalar name='Particle Triggers' value='200000' /> </endRun>"

print bl.set_end_runXML(endrun_xml_10382)


