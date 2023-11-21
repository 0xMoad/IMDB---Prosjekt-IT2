# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:11:02 2023

@author: fetra001
"""
import math

m=6.6447*10**-27
c=3*10**8
v=0.07*c

e=1.602*10**-19
k=8.99*10**9

d=2.488*10**-12
delta=10**-17

Ek=(1/2)*m*v**2

def Ep(d):
    return (k*79*2*e**2)/d

while Ek>Ep(d):
    print(d)
    d=d-delta
