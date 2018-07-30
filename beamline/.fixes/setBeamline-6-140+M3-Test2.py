import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"
bl = BeamlineSuperMouse(_MASTER_CDB)

###################################
# set Start of Run for Run 8761

#startrun_xml_8761 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='8761' startTime='2016-12-07 10:33:00.0' startNotes='Manual CDB insert' optics='6-140+M3-Test2' startPulse='0' step='4.000000' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

#print '+++ Setting Start run'
#print bl.set_start_runXML(startrun_xml_8761)

###################################
# now set beamline for Run 8761

#{'6-140+M3-Test2': {'beam_stop': 'Open', 'diffuser_thickness': 4, 'magnets': {'Q1': 50.03, 'Q3': 43.4, 'Q2': 62.48, 'Q5': 179.63, 'Q4': 133.92, 'Q7': 113.64, 'Q6': 119.01, 'Q9': 146.6, 'Q8': 171.83, 'D2': 76.4, 'DS': 324.75, 'D1': 153.01}, 'proton_absorber_thickness': 29}}

#beamline_xml_8761 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='8761' beamStop='true' diffuserThickness='4'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='Q9' polarity='1' setCurrent='146.6' /> <magnet name='Q8' polarity='1' setCurrent='171.83' /> <magnet name='Q7' polarity='1' setCurrent='113.64' /> <magnet name='Q6' polarity='1' setCurrent='119.01' /> <magnet name='Q5' polarity='1' setCurrent='179.63' /> <magnet name='Q4' polarity='1' setCurrent='133.92' /> <magnet name='D2' polarity='1' setCurrent='76.4' /> <magnet name='DS' polarity='1' setCurrent='324.75' /> <magnet name='D1' polarity='1' setCurrent='153.01' /> <magnet name='Q3' polarity='1' setCurrent='43.40' /> <magnet name='Q2' polarity='1' setCurrent='62.48' /> <magnet name='Q1' polarity='1' setCurrent='50.03' /> </beamline>"

#print '+++ Setting Beamline'
#print bl.set_beamlineXML(beamline_xml_8761)

###################################
# now set end of run for Run 8761

endrun_xml_8761 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='8761' endTime='2016-12-07 12:32:00.0' endNotes='Manual CDB insert 6-140-M3-Test2' status='0' endPulse='0' overwrite='0' > <isisBeam name='IBML-TOT' mean='0' sigma='0'/> <isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/> <scalar name='LMC-1234 Count' value='0' /> <scalar name='LMC-12 Count' value='0' /> <scalar name='LMC-34 Count' value='0' /> <scalar name='ToF2 Triggers' value='0' /> <scalar name='ToF1 Triggers' value='0' /> <scalar name='ToF0 Triggers' value='0' /> <scalar name='GVa1 Triggers' value='0' /> <scalar name='Requested Triggers' value='0' /> <scalar name='Particle Triggers' value='215000' /> </endRun>"

print '+++ Setting End run'
print bl.set_end_runXML(endrun_xml_8761)


