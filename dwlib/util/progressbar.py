import numpy as np
import time

class progressbar():
    def __init__(self, maxV, jobname=""):
        self.maxV = maxV
        self._current_percent = 1
        self.t0 = time.time()
        self.jobname = "."*(max([7-len(jobname), 1]))+jobname
    
    def reset(self, maxV, jobname=""):
        self.maxV = maxV
        self._current_percent = 1
        self.t0 = time.time()
        self.jobname = "."*(max([7-len(jobname), 1]))+jobname
        
    def start(self):
        print(self._pout(0), end="")
        self.t0 = time.time()
    
    def _ETA(self, progress):
        t_now = time.time()
        t_passed = t_now - self.t0
        eta = t_passed * ((100-progress)/(progress+1e-6))
        h = eta//3600
        eta -= h*3600
        m = eta//60
        s = eta%60
        if h>0:
            return "ETA %d:%02d"%(h, m)
        return "ETA %02d:%02d"%(m, s)

    def _pout(self, percent, eta_disp=True):
        bk = 4-len(str(int(percent)))
        bar = "| "  + "█"*int(percent//2) + " "*int(50-percent//2)
        percentage = " "*bk +"%d%%"%percent+ "|"
        if eta_disp:
            eta = self._ETA(percent)
            return  bar + percentage + eta + self.jobname
        return bar + percentage + self.jobname

    def update(self, c):
        percent = c/self.maxV*100
        if np.ceil(percent)>=self._current_percent:
            print("\r"+self._pout(percent), end="")
            self._current_percent += 1

    def finish(self):
        print("\r"+self._pout(100, eta_disp=False), end="")
        print(" Finish    ")
        return

# import time
# n = 100
# pb = progressbar(n)
# pb.start()
# for i in range(n):
#     pb.update(i)
#     time.sleep(0.05)
# pb.finish()
