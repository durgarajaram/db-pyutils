import sys
sys.path.insert(1, "/home/mice/MAUS/CDB/mice.cdb.client.api-python/src/")
from cdb import Beamline
from cdb import CoolingChannel
from pprint import pprint
from collections import defaultdict

_BL = Beamline("http://cdb.mice.rl.ac.uk")
_CC = CoolingChannel("http://cdb.mice.rl.ac.uk")

_RUNMIN = int(sys.argv[1])
_RUNMAX = int(sys.argv[2])


print 'min: ',_RUNMIN, 'max: ',_RUNMAX
tot_npart_26a = 0
tot_npart_26b = 0
tot_npart_26c = 0
tot_npart_27a = 0
tot_npart_27b = 0
tot_npart_27c = 0
tot_npart_28a = 0
tot_npart_28b = 0
tot_npart_28c = 0
tot_npart_29a = 0
tot_npart_29b = 0
tot_npart_29c = 0
tot_npart_14a = 0
tot_npart_14b = 0
tot_npart_14c = 0
tot_npart_14d = 0
tot_npart_14c = 0
tot_npart_30a = 0
tot_npart_30b = 0
tot_npart_30c = 0
tot_npart_31a = 0
tot_npart_31b = 0
tot_npart_31c = 0
tot_npart_32a = 0
tot_npart_32b = 0
tot_npart_32c = 0

tot_npart_35a = 0
tot_npart_35b = 0
tot_npart_35c = 0

tot_npart_36a = 0
tot_npart_36aa = 0
tot_npart_36b = 0
tot_npart_36c = 0
tot_npart_36d = 0

tot_npart_38a = 0

tot_npart_39a = 0
tot_npart_39b = 0
tot_npart_39c = 0

tot_npart_40a = 0
tot_npart_40b = 0
tot_npart_40c = 0

tot_npart_42a = 0
tot_npart_42b = 0
tot_npart_42c = 0

tot_npart = 0 
taskdict = defaultdict(lambda: defaultdict(dict))
trigdict = defaultdict(int)
modedict = defaultdict(str)
optdict = defaultdict(str)
timedict = defaultdict(float)
ssdict = defaultdict(float)
fcdict = defaultdict(float)
ccdict = defaultdict(str)
absdict = defaultdict(str)

taskdict["3-170+M3-Test1"]["2017-02-1"]["ABS-LH2"] = "task22a"
taskdict["3-200+M3-Test1"]["2017-02-1"]["ABS-LH2"] = "task22b"
taskdict["3-240+M3-Test1"]["2017-02-1"]["ABS-LH2"] = "task22c"

taskdict["3-140+M3-Test3"]["2017-02-1"]["ABS-LH2"] = "task23a"
taskdict["6-140+M3-Test2"]["2017-02-1"]["ABS-LH2"] = "task23b"
taskdict["10-140+M3-Test4"]["2017-02-1"]["ABS-LH2"] = "task23c"

taskdict["3-200+M3-Test2"]["2017-02-2"]["ABS-LH2"] = "task25a"
taskdict["6-200+M3-Test1"]["2017-02-2"]["ABS-LH2"] = "task25b"
taskdict["10-200+M3-Test1"]["2017-02-2"]["ABS-LH2"] = "task25c"

taskdict["3-140+M3-Test3"]["2017-02-3"]["ABS-LH2"] = "task26a"
taskdict["6-140+M3-Test2"]["2017-02-3"]["ABS-LH2"] = "task26b"
taskdict["10-140+M3-Test4"]["2017-02-3"]["ABS-LH2"] = "task26c"

taskdict["3-170+M3-Test1"]["2017-02-3"]["ABS-LH2"] = "task27a"
taskdict["3-200+M3-Test2"]["2017-02-3"]["ABS-LH2"] = "task27b"
taskdict["3-240+M3-Test1"]["2017-02-3"]["ABS-LH2"] = "task27c"

taskdict["3-140+M3-Test3"]["2017-02-4"]["ABS-LH2"] = "task28a"
taskdict["6-140+M3-Test2"]["2017-02-4"]["ABS-LH2"] = "task28b"
taskdict["10-140+M3-Test4"]["2017-02-4"]["ABS-LH2"] = "task28c"

taskdict["3-170+M3-Test1"]["2017-02-4"]["ABS-LH2"] = "task29a"
taskdict["3-200+M3-Test2"]["2017-02-4"]["ABS-LH2"] = "task29b"
taskdict["3-240+M3-Test1"]["2017-02-4"]["ABS-LH2"] = "task29c"

taskdict["3-140+M3-Test3"]["M2D-flip-2017-02-5"]["ABS-LH2"] = "task30a"
taskdict["6-140+M3-Test2"]["M2D-flip-2017-02-5"]["ABS-LH2"] = "task30b"
taskdict["10-140+M3-Test4"]["M2D-flip-2017-02-5"]["ABS-LH2"] = "task30c"

taskdict["3-170+M3-Test1"]["FieldOff"]["ABS-LH2"] = "task14a"
taskdict["3-200+M3-Test2"]["FieldOff"]["ABS-LH2"] = "task14b"
taskdict["3-140+M3-Test3"]["FieldOff"]["ABS-LH2"] = "task14c"
taskdict["3-170+M3-Test1"]["StepIV-Off"]["ABS-LH2"] = "task14a"
taskdict["3-200+M3-Test2"]["StepIV-Off"]["ABS-LH2"] = "task14b"
taskdict["3-140+M3-Test3"]["StepIV-Off"]["ABS-LH2"] = "task14c"
taskdict["3-240+M3-Test1"]["FieldOff"]["ABS-LH2"] = "task14d"

taskdict["3-170+M3-Test1"]["FieldOff"]["ABS-LH2-EMPTY"] = "task15a"
taskdict["3-200+M3-Test2"]["FieldOff"]["ABS-LH2-EMPTY"] = "task15b"
taskdict["3-140+M3-Test3"]["FieldOff"]["ABS-LH2-EMPTY"] = "task15c"
taskdict["3-240+M3-Test1"]["FieldOff"]["ABS-LH2-EMPTY"] = "task15d"

taskdict["3-170+M3-Test1"]["2017-02-6"]["ABS-LH2"] = "task32a"
taskdict["3-200+M3-Test2"]["2017-02-6"]["ABS-LH2"] = "task32b"
taskdict["3-240+M3-Test1"]["2017-02-6"]["ABS-LH2"] = "task32c"


taskdict["3-140+M3-Test3"]["2017-02-5"]["ABS-LH2"] = "task35a"
taskdict["6-140+M3-Test2"]["2017-02-5"]["ABS-LH2"] = "task35b"
taskdict["10-140+M3-Test4"]["2017-02-5"]["ABS-LH2"] = "task35c"

taskdict["3-140+M3-Test3"]["2017-02-6"]["ABS-LH2"] = "task31a"
taskdict["6-140+M3-Test2"]["2017-02-6"]["ABS-LH2"] = "task31b"
taskdict["10-140+M3-Test4"]["2017-02-6"]["ABS-LH2"] = "task31c"

taskdict["3-140+M3-Test4"]["2017-02-7"]["ABS-LH2"] = "task36a"
taskdict["3-140+M3-Test3"]["2017-02-7"]["ABS-LH2"] = "task36aa"
taskdict["4-140+M3-Test1"]["2017-02-7"]["ABS-LH2"] = "task36b"
taskdict["6-140+M3-Test2"]["2017-02-7"]["ABS-LH2"] = "task36c"
taskdict["10-140+M3-Test4"]["2017-02-7"]["ABS-LH2"] = "task36d"

taskdict["3-170+M3-Test1"]["2017-02-8"]["ABS-LH2"] = "task39a"
taskdict["6-170+M3-Test2"]["2017-02-8"]["ABS-LH2"] = "task39b"
taskdict["10-170+M3-Test2"]["2017-02-8"]["ABS-LH2"] = "task39c"

taskdict["3-140+M3-Test3"]["2017-02-3"]["ABS-LH2-EMPTY"] = "task40a"
taskdict["6-140+M3-Test2"]["2017-02-3"]["ABS-LH2-EMPTY"] = "task40b"
taskdict["10-140+M3-Test4"]["2017-02-3"]["ABS-LH2-EMPTY"] = "task40c"

taskdict["3-140+M3-Test3"]["2017-02-4"]["ABS-LH2-EMPTY"] = "task42a"
taskdict["6-140+M3-Test2"]["2017-02-4"]["ABS-LH2-EMPTY"] = "task42b"
taskdict["10-140+M3-Test4"]["2017-02-4"]["ABS-LH2-EMPTY"] = "task42c"

taskdict["3-140+M3-Test3"]["2017-02-5"]["ABS-LH2-EMPTY"] = "task44a"
taskdict["6-140+M3-Test2"]["2017-02-5"]["ABS-LH2-EMPTY"] = "task44b"
taskdict["10-140+M3-Test4"]["2017-02-5"]["ABS-LH2-EMPTY"] = "task44c"


taskdict["3-140+M3-Test3"]["2017-02-2"]["ABS-LH2-EMPTY"] = "task46a"
taskdict["6-140+M3-Test2"]["2017-02-2"]["ABS-LH2-EMPTY"] = "task46b"
taskdict["10-140+M3-Test4"]["2017-02-2"]["ABS-LH2-EMPTY"] = "task46c"

taskdict["3-140+M3-Test3"]["2017-02-6"]["ABS-LH2-EMPTY"] = "task48a"
taskdict["6-140+M3-Test2"]["2017-02-6"]["ABS-LH2-EMPTY"] = "task48b"
taskdict["10-140+M3-Test4"]["2017-02-6"]["ABS-LH2-EMPTY"] = "task48c"

taskdict["3-170+M3-Test1"]["2017-02-6"]["ABS-LH2-EMPTY"] = "task49a"
taskdict["3-200+M3-Test2"]["2017-02-6"]["ABS-LH2-EMPTY"] = "task49b"
taskdict["3-240+M3-Test1"]["2017-02-6"]["ABS-LH2-EMPTY"] = "task49c"

tasks = ["task22a", "task22b", "task22c", "task23a", "task23b", "task23c", "task25a", "task25b", "task25c", "task26a", "task26b", "task26c", "task27a", "task27b", "task27c", "task28a", "task28b", "task28c", "task29a", "task29b", "task29c", "task14a", "task14b", "task14c", "task14d", "task31a", "task31b", "task31c", "task32a", "task32b", "task32c", "task35a", "task35b", "task35c", "task36a", "task36aa", "task36b", "task36c", "task36d", "task39a", "task39b", "task39c", "task40a", "task40b", "task40c", "task42a", "task42b", "task42c", "task44a", "task44b", "task44c", "task15a", "task15b", "task15c", "task15d", "task46a", "task46b", "task46c", "task48a", "task48b", "task48c", "task49a", "task49b", "task49c" ]

#cclist = ["2017-02-1", "2017-02-2", "2017-02-3", "2017-02-4", "FieldOff", "2017-02-5", "2017-02-6", "2017-02-7", "2017-02-8", "M2D-flip-2017-02-5"]
cclist = ["2017-02-1", "2017-02-2", "2017-02-3", "2017-02-4", "FieldOff", "2017-02-5", "2017-02-6", "2017-02-7", "2017-02-8"]

excluded_runs = [10138, 10139]
for _RUN in range(_RUNMIN, _RUNMAX+1):
    if _RUN in excluded_runs:
        continue
    try:
        blinfo = _BL.get_beamline_for_run(_RUN)
        ccinfo = _CC.get_coolingchannel_for_run(_RUN)
        absinfo = _CC.get_absorber_for_run(_RUN)
        if blinfo[_RUN]['daq_trigger'] != 'TOF1':
            continue
        trigs = blinfo[_RUN]['scalars']
        ntof1 = trigs['ToF1 Triggers']
        ntof2 = trigs['ToF2 Triggers']
        npart = trigs['Particle Triggers']
        bl_task_name = blinfo[_RUN]['optics']
        tstart = blinfo[_RUN]["start_time"]
        tend = blinfo[_RUN]["end_time"]
        hdiff = ((tend - tstart).seconds)*1.0/3600.0
        cc_task_name = ccinfo['tag']
        abs_task_name = next(iter(absinfo))[1]
        for mag in ccinfo['magnets']:
            if mag['name'] == "FCU":
                cc_mode = mag['mode']
            for coil in mag['coils']:
                if coil['name'] == "SSD-C":
                    ssd_current = coil['iset']
                if coil['name'] == "FCU-C":
                    fc_current = coil['iset']
        if cc_task_name == "FieldOff" or cc_task_name == "StepIV-Off":
            cc_mode = "Off"
        if _RUN > 9889 and _RUN < 9894:
            cc_task_name = '2017-02-6' # these runs have the wrong CDB cc tag
        if cc_task_name not in cclist:
            continue
        print abs_task_name
        task_name = taskdict[bl_task_name][cc_task_name][abs_task_name]
        trigdict[task_name] += npart
        modedict[task_name] = cc_mode
        optdict[task_name] = bl_task_name
        ssdict[task_name] = ssd_current
        fcdict[task_name] = fc_current
        timedict[task_name] += hdiff
        ccdict[task_name] = cc_task_name
        absdict[task_name] = abs_task_name
        tot_npart+=npart          
        #print '++++ RUN:',_RUN,'optics: ',blinfo[_RUN]['optics'],'nParticles,nTOF1,nTOF2,nTOF2/nParticles: ',npart,ntof1,ntof2,ntof2*1.0/npart
        print '++++ RUN:',_RUN, 'date: ',blinfo[_RUN]['start_time'], 'optics: ',blinfo[_RUN]['optics'],'CC: ',ccinfo['tag'],'Task: ',task_name,'nParticles: ',npart,'time: ',str(round(hdiff, 2)), 'hrs', cc_mode, ssd_current
    except:
        #print _RUN,'does not exist'
        pass
print
print " Total particles : ", tot_npart
print
print '%8s\t|%8s\t|%8s\t|%8s\t|%16s\t|%8s\t|%8s' % ("Task", "Mode", "Channel", "Absorber", "Beam", "Triggers", "Time(hrs)")
for task in tasks:
    #print task, ": triggers: ", trigdict[task], " mode: ",modedict[task], " beam: ",optdict[task], " time: ", str(round(timedict[task], 2))
    #print 'task: %10s\tmode: %10s\tssd-c: %5.2f\tbeam: %16s\ttrigs: %8d\thours: %3.2f' % (task, modedict[task], ssdict[task], optdict[task], trigdict[task], timedict[task])
    print '%8s\t|%8s\t|%8s\t|%8s\t|%16s\t|%8d\t|%3.2f' % (task, modedict[task], ccdict[task], absdict[task], optdict[task], trigdict[task], timedict[task])

