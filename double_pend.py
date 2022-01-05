#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:53:16 2020

@author: hitesh
"""
import numpy as np
from matplotlib import pyplot as plt
from globals import *


def f (u,t): # RHS of time-derivative equations
    th1 = u[0]     # Position of top rod
    th2 = u[1]     # Position of bottom rod
    w1 = u[2]  # Velocity of top rod
    w2 = u[3]  # Velocity of bottom rod

    f_th1 = w1  # Equation of change for th1
    f_th2 = w2  # Equation of change for th2

    f_w1 = -g * (2*m1+m2) * np.sin(th1)
    f_w1 += m2 * g * np.sin(th1 - 2*th2)
    f_w1 += 2 * np.sin(th1-th2) * m2 * (w2**2 * L2 + w1**2 * L1 * np.cos(th1-th2))
    f_w1 /= L1* (2*m1 + m2 - m2*np.cos(2*th1 - 2*th2))

    f_w2 = w1**2 * L1 * (m1+m2)
    f_w2 += g * (m1+m2) * np.cos(th1)
    f_w2 += w2**2 * L2 * m2 * np.cos(th1-th2)
    f_w2 *= 2 * np.sin(th1-th2)
    f_w2 /= L2 * (2*m1 + m2 - m2*np.cos(2*th1 - 2*th2))

    return np.array([f_th1,f_th2,f_w1,f_w2])

def leapfrog (f,a,b,h,x0): # Leapfrog method
    t_arr = np.arange(a,b,h)
    x = np.copy(x0)
    x_arr = np.zeros((np.size(t_arr),np.size(x0)),dtype=float)
    
    x_mid = x + h*f(x,t_arr[0])/2
        
    for i in range(np.size(t_arr)):
        t = t_arr[i]
        x_arr[i,:] = x
        
        k1 = h*f(x_mid, t + 0.5*h)
        x += k1
        k2 = h*f(x, t + h)
        x_mid += k2
        
    return x_arr, t_arr

def RK4 (f,a,b,h,x0):

    t_arr = np.arange(a,b,h)
    x = np.copy(x0)
    x_arr = np.zeros((np.size(t_arr),np.size(x0)),dtype=float)
    for i in range(np.size(t_arr)):
        t = t_arr[i]
        x_arr[i,:] = x
        
        k1 = h*f(x,t)
        k2 = h*f(x + 0.5*k1, t + 0.5*h)
        k3 = h*f(x + 0.5*k2, t + 0.5*h)
        k4 = h*f(x + k3, t + h)
        x += (k1 + 2*k2 + 2*k3 + k4)/6
        
        print(f'Completion: {round(t*100/b,2)}%')

    return x_arr,t_arr

def double_pendulum (a, b, x0, N):

    # a = 0.0         # Starting time
    # b = 50.        # Ending time
    # N = 100000      # Number of points

    h_t = (b-a)/N   # Distance between points

    # th0 = np.pi/400   # Initial angular position
    # thdot0 = 0.     # Initial angular velocity

    # x0 = np.array([th0,thdot0])     # Initial condition

    # x_arr,t_arr = leapfrog(f,a,b,h_t,x0)
    x_arr,t_arr = RK4(f,a,b,h_t,x0)
    x_arr = np.array(x_arr)

    return x_arr,t_arr