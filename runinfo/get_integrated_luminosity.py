"""
My job is to:
    given a starting and ending run:
      get the run information for the cdb for each run
      integrate the #particle triggers
      write them out to file

Pulser runs are excluded
If there is a break >=1 day between runs, "missing" days will be reported as having 0 triggers

Script arguments are: 
     <starting-runNumber> & <ending-runNumber>
     e.g plot_trigs.py 9302 9308
"""

from cdb import Beamline
import collections
from datetime import datetime, timedelta
import sys

_cdbServerUrl = "http://cdb.mice.rl.ac.uk"

class TrigInfo():
    def __init__(self):
       """"
       initialize stuff"
       """
       self._bl = Beamline(_cdbServerUrl)
       self.trigOutFile = None

    def get_trigger_counts(self, run_min, run_max):
        # output file for writing trigger count
        self.trigOutFile = "integratedTriggers_"+str(run_min)+"_"+str(run_max)+".txt"
        # trigdict is a dict of date, #triggers as key, value
        # date will be in the format YYYY/MM/DD
        trigdict = {}
        # get the beamline info for the starting run
        # need the starting timestamp to compare against if date changes
        blrunmin = self._bl.get_beamline_for_run(run_min)
        oldrunts = blrunmin[run_min]['start_time']
        old_run_date = oldrunts.day

        # loop over runs
        run = run_min
        while run < run_max:
            try:
                # get the beamline scalers, trigger, and run time info
                blrun = self._bl.get_beamline_for_run(run)
                blscalers = blrun[run]['scalars']
                runts = blrun[run]['start_time']
                trigtype = blrun[run]['daq_trigger']
                # date for this run
                run_date = runts.day
         
                # check the diff in #days between this run's date and previous
                tsdiff = runts-oldrunts
                deltats = tsdiff.days
                # print '        ', runts, oldrunts, '>>> ', deltats

                # if there's a gap in #days between runs, they were empty
                # loop over the #elapsed days between runs
                for i in range(1, deltats+1):
                    # print '         ... ', i
                    incr_runts = oldrunts + timedelta(days=i)
                    # print '         ... ', incr_runts
                    # fill the dict with 0
                    # make sure date is in the right format
                    trigdict[incr_runts.strftime("%Y/%m/%d")] = 0

                # format the date for storing in the dict
                rundate = runts.strftime("%Y/%m/%d")

                # do not count pulsers
                if trigtype != "TOF1":
                    if rundate in trigdict:
                        trigdict[rundate] += 0
                    else:
                        trigdict[rundate] = 0
                else:
                    # get the scalers count
                    for k,v in blscalers.iteritems():
                        skey = k.translate(None, ' ')
                        ##print skey, v
                        if "Particle" in k:
                            if rundate in trigdict:
                                ##print '>>>> key exists -- appending',rundate,v
                                trigdict[rundate] += v
                            else:
                                ##print '<<<<<< new key -- ',rundate,v
                                trigdict[rundate] = v
                            print '++ ', run, v
                # done with this run
                # reset the old run date to be this one
                old_run_date = run_date
                oldrunts = runts
            except:
                pass
            # increment run
            run = run + 1
        # return trigdict contains date,triggers 
        return trigdict

    def print_trigger_counts(self, trigdict):
        ##print sorted(trigdict)
        ##print len(trigdict)
        try:
            with open(self.trigOutFile, "w") as f:
                for key in sorted(trigdict.iterkeys()):
                    print >>f, key,trigdict[key]
        except Exception as e:
            print e
        ##od = collections.OrderedDict(sorted(trigdict.items()))
        ##print od

if __name__ == "__main__":
    # set default start and end run
    run_min = 7497
    run_max = 9412

    # expect 2 arguments
    #   : start run, end run
    try:
        run_min = int(sys.argv[1])
        run_max = int(sys.argv[2])
    except:
        print "Usage: ", sys.argv[0], " <min-runNumber> <max-runNumber>"
  
    # class init
    triginfo = TrigInfo()
    # get the dict with date, triggers k,v pairs
    trigdict = triginfo.get_trigger_counts(run_min, run_max)
    # parse dict and write to file
    triginfo.print_trigger_counts(trigdict)

