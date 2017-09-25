# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:55:18 2017

@author: brian
"""

from pylab import *
ion()
t = linspace(0,1,100)

x= 3*sin(2*pi*t)
y = 2*cos(2*pi*t)

figure(1)

clf()
subplot(311)
plot(x,y)
grid()
ylabel('y')
xlabel('x')
axis('equal')

vx = 6*pi*cos(2*pi*t)
vy = -4*pi*sin(2*pi*t)

ax = -12*pi**2*sin(2*pi*t)
ay = -8*pi**2*cos(2*pi*t)

subplot(312)
plot(t,vx)
grid()
ylabel('vx')
xlabel('t')

subplot(313)
plot(t,vy)
grid()
ylabel('vy')
xlabel('t')

figure(2)

for it in arange(len(t)):
    clf()
    #subplot(131)
    plot(x,y)
    plot([0,x[it]],[0,y[it]],'b-o')
    axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    text(1.2*x[it],1.2*y[it],r'$\vec{x}$',color='blue',size=15)

    #subplot(132)
    plot(vx/2,vy/2,'g')
    plot([0,vx[it]/2],[0,vy[it]/2],'g-o')
    text(1.1*vx[it]/2,1.1*vy[it]/2,r'$\vec{v}$',color='green',size=15)
    axis('equal'); xlabel(r'$v_x$'); ylabel(r'$v_y$')


    #subplot(133)
    plot(ax/10,ay/10,'r')
    plot([0,ax[it]/10],[0,ay[it]/10],'r-o')
    axis('equal'); xlabel(r'$v_x$'); ylabel(r'$v_y$')
    text(1.1*ax[it]/10,1.1*ay[it]/10,r'$\vec{a}$',color='red',size=15)
    grid()
    savefig('xva_frame_%03d.png' % it)
    pause(.001)
