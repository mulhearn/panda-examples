import numpy as np
import matplotlib.pyplot as plt

NEUTRONS = 48.3   # neutrons in sparse region per pulse
MEAN_E   = 108  # k electrons
SIGMA_E  = 13   # k electrons
VOLUME   = 7.34*7.34*6.88

def res(N):
    N = N*NEUTRONS
    return 100*(SIGMA_E/MEAN_E)/np.sqrt(N)     

def throw(PULSES):
    # Poisson fluctuations of neutron count:
    neutrons = 0
    for i in range(PULSES):
        neutrons += np.random.poisson(NEUTRONS)
    print("total neutrons:  ", neutrons)

    # Throw each neutron according to mean and sigma from full MC
    x = np.random.normal(MEAN_E, SIGMA_E, size=neutrons)
    h,bins = np.histogram(x,bins=100,range=(0,200))
    cbins = (bins[1:]+bins[:-1])/2
    nz = (h>0)
    h     = h[nz]
    cbins = cbins[nz]
    errs  = h**(0.5)
    plt.errorbar(cbins,h,yerr=errs,fmt="ko")
    plt.xlim(0,200)
    plt.xlabel("Electrons (k))")
    plt.ylabel("Reconstructed Neutrons")

N = 1
YMAX = 10
fres = np.around(res(N),2)
throw(N)
plt.ylim(0,YMAX)
plt.text(20,0.9*YMAX,"Parameterized MC")
plt.text(20,0.8*YMAX,"(Entire Module)")
plt.text(130,0.9*YMAX,"Single DDG pulse")
plt.text(130,0.8*YMAX,"Stat. Unc.: {0:0.2f}%".format(fres))
plt.savefig("entire_1pulse.pdf")


N = 100
YMAX = 400
fres = np.around(res(N),2)
throw(N)
plt.ylim(0,YMAX)
plt.text(20,0.9*YMAX,"Parameterized MC")
plt.text(20,0.8*YMAX,"(Entire Module)")
plt.text(130,0.9*YMAX,"100 DDG pulses")
plt.text(130,0.8*YMAX,"Stat. Unc.: {0:0.2f}%".format(fres))
plt.savefig("entire_100pulses.pdf")

N = 10000
D = int(N / VOLUME) 
YMAX = 110
fres = np.around(res(D),2)
throw(D)
plt.ylim(0,YMAX)
plt.text(20,0.9*YMAX,"Parameterized MC")
plt.text(20,0.8*YMAX,"(1 m^2 region)")
plt.text(130,0.9*YMAX,"10k DDG pulses")
plt.text(130,0.8*YMAX,"Stat. Unc.: {0:0.2f}%".format(fres))
plt.savefig("region_10k.pdf")
