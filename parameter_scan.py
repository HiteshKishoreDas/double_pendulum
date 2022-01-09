#%%

import numpy as np
from matplotlib import pyplot as plt
from numpy.lib.npyio import save
import double_pend as dp
import globals as g 

for i,th1_0 in enumerate(g.th1_0_arr):
    for j,th2_0 in enumerate(g.th2_0_arr):

        print(f'Running para ({i},{j}) ....................')

        init_1 = np.array([th1_0,th2_0,0,0])

        x_arr,t_arr   = dp.double_pendulum(g.a, g.b, init_1, g.N)
        
        save_arr  = np.zeros((np.shape(x_arr)[0],5))

        save_arr[:,0]  = t_arr
        save_arr[:,1:] = x_arr

        np.savetxt(f'save_arr/m1{g.m1}_m2{g.m2}_L1{g.L1}_L2{g.L2}_th1{round(th1_0,2)}_th2{round(th2_0,2)}',save_arr)

        print(f'Saved para ({i},{j}) .......................')
        print('________________________________________________')