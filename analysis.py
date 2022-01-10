import numpy as np
import matplotlib.pyplot as plt

import double_pend as dp

import globals as g

plt.figure(figsize=(8,8))
plt.yscale('log')

fig1, ax1 = plt.subplots(1,1,figsize=(8,8))
ax1.set_yscale('log')

fig2, ax2 = plt.subplots(1,1,figsize=(8,8))
ax2.set_yscale('log')

fig3, ax3 = plt.subplots(1,1,figsize=(8,8))
ax3.set_yscale('log')

for i,th1_0 in enumerate(g.th1_0_arr):
    for j,th2_0 in enumerate(g.th2_0_arr):

        save_arr = np.loadtxt(f'save_arr/m1{g.m1}_m2{g.m2}_L1{g.L1}_L2{g.L2}_th1{round(th1_0,2)}_th2{round(th2_0,2)}')

        x_arr = save_arr[:,1:]
        t_arr = save_arr[:,0]

        dist = dp.dist_to_end(x_arr[:,0],x_arr[:,1])


        # plt.figure()
        # plt.plot(t_arr , dist)
        # plt.show()

        hist_dist  = np.histogram(dist,bins=100)
        hist_th1  = np.histogram(np.mod(x_arr[:,0],2*np.pi),bins=100)
        hist_th2  = np.histogram(np.mod(x_arr[:,1],2*np.pi),bins=100)

        ax1.plot(hist_dist[1][:-1],hist_dist[0])

        ax2.plot(hist_th1[1][:-1],hist_th1[0])

        ax3.plot(hist_th2[1][:-1],hist_th2[0])

        print(i,j)

ax1.set_title("Distance histogram")        
ax1.set_xlabel("Distance from origin")
ax1.set_ylabel("Frequency")
fig1.savefig("distance_histogram.png")

ax2.set_title(r"$\theta_1$ histogram")        
ax2.set_xlabel(r"$\theta_1$")
ax2.set_ylabel("Frequency")
fig2.savefig("theta1_histogram.png")

ax3.set_title(r"$\theta_2$ histogram")        
ax3.set_xlabel(r"$\theta_2$")
ax3.set_ylabel("Frequency")
fig3.savefig("theta2_histogram.png")