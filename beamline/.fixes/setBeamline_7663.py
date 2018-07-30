import cdb
from cdb import BeamlineSuperMouse

bl = BeamlineSuperMouse('http://preprodcdb.mice.rl.ac.uk')

###################################
# set Start of Run for Run 7663

startrun_xml_7663 = "<?xml version='1.0'?> <startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='7663' startTime='2016-02-29 22:29:07.064792' startNotes='3,200 Pion - Zero Absorber' optics='Individual Settings' startPulse='1552088' step='4.000000' runType='Test' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

print bl.set_start_runXML(startrun_xml_7663)

###################################
# now set beamline for Run 7663

beamline_xml_7663 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='7663' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='78' > <magnet name='Q9' polarity='1' setCurrent='188.723999' /> <magnet name='Q8' polarity='1' setCurrent='221.024002' /> <magnet name='Q7' polarity='1' setCurrent='146.143997' /> <magnet name='Q6' polarity='1' setCurrent='147.315994' /> <magnet name='Q5' polarity='1' setCurrent='222.255997' /> <magnet name='Q4' polarity='1' setCurrent='165.891998' /> <magnet name='D2' polarity='1' setCurrent='94.400002' /> <magnet name='DS' polarity='1' setCurrent='3.094593' /> <magnet name='D1' polarity='1' setCurrent='189.804993' /> <magnet name='Q3' polarity='1' setCurrent='60.689999' /> <magnet name='Q2' polarity='1' setCurrent='99.220001' /> <magnet name='Q1' polarity='1' setCurrent='54.220001' /> </beamline>"

print bl.set_beamlineXML(beamline_xml_7663)

###################################
# now set end of run for Run 7663

endrun_xml_7663 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='7663' endTime='2016-02-29 22:55:59.502932' endNotes='3,200 Pion - Zero Absorber' status='0' endPulse='1553348' overwrite='0' > <isisBeam name='IBML-TOT' mean='3.963453' sigma='3.963453'/> <isisBeam name='IBML-S8.1' mean='1.655476' sigma='1.655476'/> <isisBeam name='IBML-S7.4' mean='0.969486' sigma='0.969486'/> <isisBeam name='IBML-S7.3' mean='1.338491' sigma='1.338491'/> <scalar name='LMC-1234 Count' value='217752' /> <scalar name='LMC-12 Count' value='1783333' /> <scalar name='LMC-34 Count' value='1646246' /> <scalar name='ToF2 Triggers' value='8168' /> <scalar name='ToF1 Triggers' value='21850' /> <scalar name='ToF0 Triggers' value='100004' /> <scalar name='GVa1 Triggers' value='1069' /> <scalar name='Requested Triggers' value='21850' /> <scalar name='Particle Triggers' value='17399' /> </endRun>"

print bl.set_end_runXML(endrun_xml_7663)

