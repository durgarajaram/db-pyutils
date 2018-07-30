import cdb
from cdb import BeamlineSuperMouse

_TEST_CDB = "http://preprodcdb.mice.rl.ac.uk"
_MASTER_CDB = "http://172.16.246.25:8080"
bl = BeamlineSuperMouse(_MASTER_CDB)

###################################
# set Start of Run for Run 8760

startrun_xml_8760 = "<?xml version='1.0'?><startRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setStartRun.xsd' runNumber='8760' startTime='2016-12-07 08:25:00.0' startNotes='Manual CDB insert H7c' optics='10-140+M3-Test3' startPulse='0' step='4.000000' runType='Special Run' daqTrigger='TOF1' daqGateWidth='3.000500' daqVersion='DATE_v7.66 EqList_v0.9.2' gdcHostName='miceraid5' overwrite='0'> <ldcHost name='miceacq20' /> <ldcHost name='miceacq17' /> <ldcHost name='miceacq16' /> <ldcHost name='miceacq15' /> <ldcHost name='miceacq14' /> </startRun>"

print bl.set_start_runXML(startrun_xml_8760)

###################################
# now set beamline for Run 8760

#{'10-140+M3-Test3': {'beam_stop': 'Open', 'diffuser_thickness': 15, 'magnets': {'Q1': 57.2, 'Q3': 49.6, 'Q2': 71.39, 'Q5': 204.8, 'Q4': 152.73, 'Q7': 99.9, 'Q6': 135.78, 'Q9': 129.0, 'Q8': 151.1, 'D2': 85.0, 'DS': 372.4, 'D1': 169.95}, 'proton_absorber_thickness': 29}}

#beamline_xml_8760 = "<?xml version='1.0'?> <beamline xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setBeamlineTag.xsd' runNumber='8760' beamStop='true' diffuserThickness='15'  overwrite='0'  protonAbsorberThickness='29' > <magnet name='Q9' polarity='1' setCurrent='129.0' /> <magnet name='Q8' polarity='1' setCurrent='151.1' /> <magnet name='Q7' polarity='1' setCurrent='99.9' /> <magnet name='Q6' polarity='1' setCurrent='135.78' /> <magnet name='Q5' polarity='1' setCurrent='204.8' /> <magnet name='Q4' polarity='1' setCurrent='152.73' /> <magnet name='D2' polarity='1' setCurrent='85.0' /> <magnet name='DS' polarity='1' setCurrent='372.4' /> <magnet name='D1' polarity='1' setCurrent='169.95' /> <magnet name='Q3' polarity='1' setCurrent='49.6' /> <magnet name='Q2' polarity='1' setCurrent='71.39' /> <magnet name='Q1' polarity='1' setCurrent='57.2' /> </beamline>"

#print bl.set_beamlineXML(beamline_xml_8760)

###################################
# now set end of run for Run 8760

endrun_xml_8760 = "<?xml version='1.0'?> <endRun xmlns='http://mice.stfc.ac.uk' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://mice.stfc.ac.uk bl_setEndRun.xsd' runNumber='8760' endTime='2016-12-07 10:24:00.0' endNotes='Manual CDB insert H7c' status='0' endPulse='0' overwrite='0' > <isisBeam name='IBML-TOT' mean='0' sigma='0'/> <isisBeam name='IBML-S8.1' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.4' mean='0.0' sigma='0.0'/> <isisBeam name='IBML-S7.3' mean='0.0' sigma='0.0'/> <scalar name='LMC-1234 Count' value='0' /> <scalar name='LMC-12 Count' value='0' /> <scalar name='LMC-34 Count' value='0' /> <scalar name='ToF2 Triggers' value='0' /> <scalar name='ToF1 Triggers' value='0' /> <scalar name='ToF0 Triggers' value='0' /> <scalar name='GVa1 Triggers' value='0' /> <scalar name='Requested Triggers' value='0' /> <scalar name='Particle Triggers' value='301000' /> </endRun>"

print bl.set_end_runXML(endrun_xml_8760)


