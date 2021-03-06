import sys
import cdb

def get_beamline(run_number):
    bl = cdb.Beamline()
    beamline_all = bl.get_beamline_for_run(run_number)[run_number]
    return beamline_all

def get_cc(run_number):
    cc = cdb.CoolingChannel()
    coolingchannel = cc.get_coolingchannel_for_run(run_number)
    return coolingchannel

def get_tof_triggers_sum(tof_key, run_list):
    trig_list = [get_beamline(run_number)["scalars"][tof_key] for run_number in run_list]
    return sum(trig_list)

def get_time_sum(run_list):
    start_time = [get_beamline(run_number)["start_time"] for run_number in run_list]
    end_time = [get_beamline(run_number)["end_time"] for run_number in run_list]
    delta_time = [end_time[i] - start for i, start in enumerate(start_time)]
    total_seconds = sum([delta.total_seconds() for delta in delta_time])
    minutes = int(total_seconds)/60
    hours = minutes/60
    minutes = minutes % 60
    return hours, minutes


def main():
    try:
        if len(sys.argv) != 2:
            raise IndexError("Should have exactly 2 arguments")
        run = sys.argv[1]
        run = int(run)
    except (KeyError, ValueError, IndexError, TypeError):
        print "Failed to run - could not parse command line. Expected:\n    python checkout_cdb.py <run number>"
        return 1
    run_list = [run]
    try:
        scalars = get_beamline(run)["scalars"]
    except KeyError:
        print "Couldnt find run", run
        return 2

    for i in range(5):
        print
    bl = get_beamline(run)
    bl_keys = ["run_number", "start_time", "end_time", "run_type", "daq_trigger", "daq_gate_width", "optics"]
    for key in bl_keys:
        value = bl[key]
        print key.ljust(20), value

    ccinfo = get_cc(run)
    print ccinfo['magnets']

    print "="*30
    scalars_keys = ["Particle Triggers", "Requested Triggers", "GVa1 Triggers", "ToF0 Triggers", "ToF1 Triggers", "ToF2 Triggers", "LMC-12 Count", "LMC-34 Count", "LMC-1234 Count"]
    for key in scalars_keys:
        print key.ljust(20), scalars[key]
    print "="*30

    for key in sorted(bl["isis_beam"]):
        print key.ljust(20), bl["isis_beam"][key]["mean"]

if __name__ == "__main__":
    main()
