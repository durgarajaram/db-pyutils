import cdb
from cdb import BeamlineSuperMouse

bl = BeamlineSuperMouse('http://preprodcdb.mice.rl.ac.uk')

###################################
# set Start of Run for Run 7664

startrun_xml_7664 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='7664' startTime='2016-02-29 22:57:47.301821' startNotes='3,200 Pion - Zero Absorber' optics='Individual Settings' startPulse='1553433' step='4.000000' runType='Test' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /></startRun>"

print bl.set_start_runXML(startrun_xml_7664)

###################################
# now set beamline for Run 7664

beamline_xml_7664 = "<?xml version='1.0'?><beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='7664' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='82' ><magnet name='Q9' polarity='1' setCurrent='188.727997' /><magnet name='Q8' polarity='1' setCurrent='221.020004' /> <magnet name='Q7' polarity='1' setCurrent='146.147995' /> <magnet name='Q6' polarity='1' setCurrent='147.315994' /> <magnet name='Q5' polarity='1' setCurrent='222.251999' /> <magnet name='Q4' polarity='1' setCurrent='165.888000' /> <magnet name='D2' polarity='1' setCurrent='94.402000' /> <magnet name='DS' polarity='1' setCurrent='3.823579' /> <magnet name='D1' polarity='1' setCurrent='189.809998' /> <magnet name='Q3' polarity='1' setCurrent='60.700001' /> <magnet name='Q2' polarity='1' setCurrent='99.209999' /> <magnet name='Q1' polarity='1' setCurrent='54.220001' /> </beamline>"

print bl.set_beamlineXML(beamline_xml_7664)

###################################
# now set end of run for Run 7664

endrun_xml_7664 = "<?xml version='1.0'?><endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='7664' endTime='2016-03-01 08:29:41.975666' endNotes='3,200 Pion - Zero Absorber' status='0' endPulse='1556291' overwrite='0' ><isisBeam name='IBML-TOT' mean='3.346256' sigma='3.346256'/><isisBeam name='IBML-S8.1' mean='1.385449' sigma='1.385449'/><isisBeam name='IBML-S7.4' mean='0.810350' sigma='0.810350'/> <isisBeam name='IBML-S7.3' mean='1.150464' sigma='1.150464'/> <scalar name='LMC-1234 Count' value='564538' /> <scalar name='LMC-12 Count' value='4637779' /> <scalar name='LMC-34 Count' value='4302601' /> <scalar name='ToF2 Triggers' value='21278' /> <scalar name='ToF1 Triggers' value='56728' /> <scalar name='ToF0 Triggers' value='261491' /> <scalar name='GVa1 Triggers' value='2853' /> <scalar name='Requested Triggers' value='56753' /> <scalar name='Particle Triggers' value='45458' /></endRun>"

print bl.set_end_runXML(endrun_xml_7664)

