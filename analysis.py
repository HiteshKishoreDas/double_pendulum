import numpy as np
import matplotlib.pyplot as plt

import double_pend as dp

import globals as g

plt.figure()
plt.yscale('log')

for i,th1_0 in enumerate(g.th1_0_arr):
    for j,th2_0 in enumerate(g.th2_0_arr):

        save_arr = np.loadtxt(f'save_arr/m1{g.m1}_m2{g.m2}_L1{g.L1}_L2{g.L2}_th1{round(th1_0,2)}_th2{round(th2_0,2)}')

        x_arr = save_arr[:,1:]
        t_arr = save_arr[:,0]

        dist = dp.dist_to_end(x_arr[:,0],x_arr[:,1])


        # plt.figure()
        # plt.plot(t_arr , dist)
        # plt.show()

        hist  = np.histogram(dist,bins=100)

        plt.plot(hist[1][:-1],hist[0])
        
plt.show()