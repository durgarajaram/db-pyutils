from cdb import Beamline
import collections
import ROOT
from datetime import datetime, timedelta
import sys

_cdbServerUrl = "http://cdb.mice.rl.ac.uk"

class TrigInfo():
    def __init__(self):
        self._bl = Beamline(_cdbServerUrl)
        self.beenin = False

    def get_trigger_counts(self, run_min, run_max):
        trigdict = {}
        blrunmin = self._bl.get_beamline_for_run(run_min)
        oldrunts = blrunmin[run_min]['start_time']
        old_run_date = oldrunts.day
        #oldrunts = None
        run = run_min
        while run < run_max:
            try:
                blrun = self._bl.get_beamline_for_run(run)
                blscalers = blrun[run]['scalars']
                runts = blrun[run]['start_time']
                # date for this run
                run_date = runts.day
                print '++ RTS: N: O ',runts, type(runts), run_date, old_run_date

#mdate1 = datetime.datetime.strptime(mdate, "%Y-%m-%d").date()
#rdate1 = datetime.datetime.strptime(rdate, "%Y-%m-%d").date()
#delta =  (mdate1 - rdate1).days


                #date_diff = runts - oldrunts
w
                ## if this run has a date different from previous
                if run_date != old_run_date:
                    print '!!! change >>> ',run_date-old_run_date
                    # check how many days between this run date and previous
                    mdate1 = datetime.datetime.strptime(oldrunts, "%Y-%m-%d %H:%M:%S.%f").date()
                    print '>>>>>>>>>>>>>>>>> D ', mdate1
                    #rdate1 = datetime.datetime.strptime(runts, "%Y-%m-%d %H:%M:%S.%f").date()
                    #delta =  (mdate1 - rdate1).days
                    #print '>D ', mdate1, rdate1
                    #ndays=run_date-old_run_date
                    print '>D ', delta
                    for d in range(int(ndays)):
                    #for d in range(delta):
                        print '<<< ', d
                        inc_run_date = old_run_date + d
                        print '+++++++++++++ ', old_run_date, old_run_date + d
                        trigdict[incr_run_date] += 0
                    ##print '!!! change >>> ',run_date,old_run_date,'>>>>>>>>>>>>>>> ',date_diff
                else:
                    print '...........same'
                old_run_date = run_date
                oldrunts = runts
                ##rundate = runts.strftime("%Y-%m-%d")
                rundate = runts.strftime("%Y/%m/%d")
                for k,v in blscalers.iteritems():
                    skey = k.translate(None, ' ')
                    ##print skey, v
                    if "Particle" in k:
                        if rundate in trigdict:
                            ##print '>>>> key exists -- appending',rundate,v
                            trigdict[rundate] += v
                        else:
                            ##print '<<<<<< new key -- ',rundate,v
                            ##print '<<NO'
                            trigdict[rundate] = v
            except:
                pass
            run = run + 1
        return trigdict

    def print_trigger_counts(self, trigdict):
        ##print sorted(trigdict)
        print len(trigdict)
        for key in sorted(trigdict.iterkeys()):
            print key,trigdict[key]

        ##od = collections.OrderedDict(sorted(trigdict.items()))
        ##print od

if __name__ == "__main__":
    run_min = 7497
    run_max = 9279
    try:
        run_min = int(sys.argv[1])
        run_max = int(sys.argv[2])
    except:
        print "Usage: ", sys.argv[0], " <min-runNumber> <max-runNumber>"
    
    triginfo = TrigInfo()
    trigdict = TrigInfo().get_trigger_counts(run_min, run_max)
    TrigInfo().print_trigger_counts(trigdict)
