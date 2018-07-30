import cdb
from cdb import BeamlineSuperMouse

bl = BeamlineSuperMouse('http://preprodcdb.mice.rl.ac.uk')

###################################
# set Start of Run for Run 7661

startrun_xml_7661 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='7661' startTime='2016-02-29 20:42:17.180620' startNotes='3,172 Pion - Zero Absorber' optics='Individual Settings' startPulse='1547079' step='4.000000' runType='Test' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

print bl.set_start_runXML(startrun_xml_7661)

###################################
# now set beamline for Run 7661

beamline_xml_7661 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='7661' beamStop='true' diffuserThickness='0'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='Q9' polarity='1' setCurrent='166.628006' /> <magnet name='Q8' polarity='1' setCurrent='195.296005' /> <magnet name='Q7' polarity='1' setCurrent='129.175995' /> <magnet name='Q6' polarity='1' setCurrent='132.951996' /> <magnet name='Q5' polarity='1' setCurrent='200.656006' /> <magnet name='Q4' polarity='1' setCurrent='149.764008' /> <magnet name='D2' polarity='1' setCurrent='85.716003' /> <magnet name='DS' polarity='1' setCurrent='3.172078' /> <magnet name='D1' polarity='1' setCurrent='171.684998' /> <magnet name='Q3' polarity='1' setCurrent='54.939999' /> <magnet name='Q2' polarity='1' setCurrent='89.930000' /> <magnet name='Q1' polarity='1' setCurrent='49.169998' /> </beamline>"

print bl.set_beamlineXML(beamline_xml_7661)

###################################
# now set end of run for Run 7661
#### no end run in log for 7661
### leave it null
#endrun_xml_7661 = ""
#print bl.set_end_runXML(endrun_xml_7661)

