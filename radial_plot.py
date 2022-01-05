#%%

import numpy as np
from matplotlib import pyplot as plt
from numpy.lib.npyio import save
import double_pend as dp
from globals import *

def dist_to_end(th1,th2):

    x1 = L1 * np.sin(th1)
    y1 = -L1 * np.cos(th1)

    x2 = x1 + L2 * np.sin(th2)
    y2 = y1 - L2 * np.cos(th2)

    # print(x1,y1)
    # print(x2,y2)

    return np.sqrt(x2*x2 + y2*y2)

#%%

dth1_0 = 0.5*th1_0

init_1 = np.array([th1_0,th2_0,0,0])
init_2 = np.array([th1_0+dth1_0,th2_0,0,0])

x_arr,t_arr   = dp.double_pendulum(a, b, init_1, N)
x_arr2,t_arr2 = dp.double_pendulum(a, b, init_2, N)

save_arr  = np.zeros((np.shape(x_arr)[0],5))
save_arr2 = np.zeros((np.shape(x_arr)[0],5))

save_arr[:,0]  = t_arr
save_arr[:,1:] = x_arr

save_arr2[:,0]  = t_arr2
save_arr2[:,1:] = x_arr2

np.savetxt(f'save_arr_m1{m1}_m2{m2}_L1{L1}_L2{L2}',save_arr)
np.savetxt(f'save_arr2_m1{m1}_m2{m2}_L1{L1}_L2{L2}',save_arr2)

#%%

# plt.figure()
# plt.plot(t_arr , x_arr[:,0])
# # plt.plot(t_arr2, x_arr2[:,0])
# plt.show()

# plt.figure()
# plt.plot(t_arr , x_arr[:,1])
# # plt.plot(t_arr2, x_arr2[:,1])
# plt.show()
# %%

save_arr = np.loadtxt("save_arr_m11_m21_L11_L21")
save_arr2 = np.loadtxt("save_arr2_m11_m21_L11_L21")

x_arr = save_arr[:,1:]
t_arr = save_arr[:,0]

x_arr2 = save_arr2[:,1:]
t_arr2 = save_arr2[:,0]

dist = dist_to_end(x_arr[:,0],x_arr[:,1])
dist2 = dist_to_end(x_arr2[:,0],x_arr2[:,1])

plt.figure()
plt.plot(t_arr , dist)
plt.plot(t_arr2 , dist2)
plt.show()
 
# %%

# hist  = np.histogram(np.mod(x_arr[:,1],2*np.pi),bins=100)
# hist2 = np.histogram(np.mod(x_arr2[:,1],2*np.pi),bins=100)

hist  = np.histogram(dist,bins=100)
hist2 = np.histogram(dist2,bins=100)

plt.figure()
plt.plot(hist[1][:-1],hist[0])
plt.plot(hist2[1][:-1],hist2[0])
# %%
