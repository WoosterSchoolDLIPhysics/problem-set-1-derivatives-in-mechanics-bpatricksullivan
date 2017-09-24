# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:47:13 2017

@author: brian
"""

from pylab import *

t = linspace(0,4,1000)

def x(t):
    return t**4-4*t**3+2*t**2+3*t+6

def v(t):
    return 4*t**3-12*t**2+4*t+3
    
def a(t):
    return 12*t**2-24*t+4
    
def jerk(t):
    return 24*t-24
    
xx = x(t)
vv = v(t)
aa = a(t)
jj = jerk(t)

figure(1)
clf()
subplot(411)
plot(t,xx)
grid()
ylabel('x(t)')
xlabel('t')

subplot(412)
plot(t,vv)
grid()
ylabel('v(t)')
xlabel('t')

subplot(413)
plot(t,aa)
grid()
ylabel('a(t)')
xlabel('t')

subplot(414)
plot(t,jj)
grid()
ylabel('jerk(t)')
xlabel('t')
