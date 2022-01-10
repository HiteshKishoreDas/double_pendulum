import numpy as np
import matplotlib.pyplot as plt
import double_pend as dp

th1_dist = np.linspace(0,2*np.pi,num=10000)
th2_dist = np.linspace(0,2*np.pi,num=10000)

th1,th2 = np.meshgrid(th1_dist,th2_dist)

distance = dp.dist_to_end(th1,th2)

#%%

hist = np.histogram(distance, bins=100)

#%%

distance_arr = np.linspace(0,1.99,num=100)

def theory (x):

    P = np.sqrt(1-0.25*x**2)
    P = 1/P
    P = P/np.pi

    return P


plt.figure(figsize=(8,8))
plt.yscale('log')
plt.plot(hist[1][:-1],hist[0]/np.sum(hist[0]),label="Numerical")

y = theory(distance_arr)
y = y / np.sum(y)

# plt.figure(figsize=(8,8))
# plt.yscale('log')
plt.plot(distance_arr,y,label="Theory")

plt.legend()
# %%
