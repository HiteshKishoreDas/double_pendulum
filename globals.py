import numpy as np

# Parameters

h = 1e-4

a = 0
b = 100

N = b/h

m1 = 1
m2 = 1

L1 = 1
L2 = 1

g  = 9.8

th1_0 = np.pi/2
th2_0 = 0 #np.pi/4

th1_0_arr = np.linspace(0,np.pi/2, 4)
th2_0_arr = np.linspace(0,np.pi/2, 4)