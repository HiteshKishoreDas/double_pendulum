import numpy as np
import matplotlib.pyplot as plt
import double_pend as dp

th1_dist = np.linspace(0,2*np.pi,num=10000)
th2_dist = np.linspace(0,2*np.pi,num=10000)

distance_arr = np.linspace(0,2,num=1000)

th1,th2 = np.meshgrid(th1_dist,th2_dist)

distance = dp.dist_to_end(th1,th2)

#%%

hist = np.histogram(distance, bins=100)

#%%
plt.figure(figsize=(8,8))
plt.yscale('log')
plt.plot(hist[1][:-1],hist[0]/np.sum(hist[0]))
# %%