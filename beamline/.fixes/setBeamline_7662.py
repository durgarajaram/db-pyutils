import cdb
from cdb import BeamlineSuperMouse

bl = BeamlineSuperMouse('http://preprodcdb.mice.rl.ac.uk')

###################################
# set Start of Run for Run 7662

startrun_xml_7662 = "<?xml version='1.0'?> <startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='7662' startTime='2016-02-29 20:47:00.218291' startNotes='3,172 Pion - Zero Absorber' optics='Individual Settings' startPulse='1547300' step='4.000000' runType='Test' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

print bl.set_start_runXML(startrun_xml_7662)

###################################
# now set beamline for Run 7661

beamline_xml_7662 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='7662' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='78' > <magnet name='Q9' polarity='1' setCurrent='166.636002' /> <magnet name='Q8' polarity='1' setCurrent='195.300003' /> <magnet name='Q7' polarity='1' setCurrent='129.175995' /> <magnet name='Q6' polarity='1' setCurrent='132.955994' /> <magnet name='Q5' polarity='1' setCurrent='200.656006' /> <magnet name='Q4' polarity='1' setCurrent='149.751999' /> <magnet name='D2' polarity='1' setCurrent='85.713997' /> <magnet name='DS' polarity='1' setCurrent='3.059656' /> <magnet name='D1' polarity='1' setCurrent='171.679993' /> <magnet name='Q3' polarity='1' setCurrent='54.939999' /> <magnet name='Q2' polarity='1' setCurrent='89.940002' /> <magnet name='Q1' polarity='1' setCurrent='49.169998' /> </beamline>"

print bl.set_beamlineXML(beamline_xml_7661)

###################################
# now set end of run for Run 7662

endrun_xml_7662 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='7662' endTime='2016-02-29 22:24:30.786753' endNotes='3,172 Pion - Zero Absorber' status='0' endPulse='1551872' overwrite='0' > <isisBeam name='IBML-TOT' mean='3.934231' sigma='3.934231'/> <isisBeam name='IBML-S8.1' mean='1.637861' sigma='1.637861'/> <isisBeam name='IBML-S7.4' mean='0.964380' sigma='0.964380'/> <isisBeam name='IBML-S7.3' mean='1.331983' sigma='1.331983'/> <scalar name='LMC-1234 Count' value='906541' /> <scalar name='LMC-12 Count' value='7397057' /> <scalar name='LMC-34 Count' value='6818131' /> <scalar name='ToF2 Triggers' value='28750' /> <scalar name='ToF1 Triggers' value='59085' /> <scalar name='ToF0 Triggers' value='300048' /> <scalar name='GVa1 Triggers' value='4144' /> <scalar name='Requested Triggers' value='59085' /> <scalar name='Particle Triggers' value='45039' /> </endRun>"

print bl.set_end_runXML(endrun_xml_7662)

