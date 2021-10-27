# environment:  pandas matplotlib scipy pyarrow=5.0.0
# conda create -n zen pandas matplotlib scipy pyarrow=5.0.0

from pandas import read_feather
import numpy as np
import matplotlib.pyplot as plt

SIZE     = 1  # bin size in meters
NBINS    = 10//SIZE
NEUTRONS  = 3e4 # PER PULSE
SIMULATED = 1e5 
MCSCALE   = NEUTRONS / SIMULATED 

df   = read_feather("neutrons.feather")
dat = np.array([df.x, df.y, df.z]).T
#print(np.shape(dat))

H, edges = np.histogramdd(dat, bins = (NBINS, NBINS, NBINS), range=((-5,5),(-5,5),(-5,5)))

H = H*MCSCALE

sparse = H<=1

total  = np.sum(H)
recon  = np.sum(H[sparse])

print("Total Neutron Captures:  ", total)
print("Reconstructed Sparse:    ", recon)

