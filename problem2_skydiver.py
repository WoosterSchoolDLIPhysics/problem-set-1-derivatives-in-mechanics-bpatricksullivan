from pylab import *

#make an array to hold our time data
t0 = 0; tf = 30.0; dt = .5
t = arange(t0,tf,dt)

#make an array to hold our velocity data
v = zeros(len(t))
x = zeros(len(t))

#set the initial condition.
v0 = 0.
v[0] = v0


b = 0.1 #the linear drag coefficient
c = 0.0001 #quadratic drag coefficient
g = 10. #the acceleration due to gravity
m = 1.0 #the mass in kilograms

v_term = -m*g/b

for i in range(1,len(t)):
    dv = (-(b/m)*v[i-1] - g + c*v[i-1]**2)*dt
    v[i] = v[i-1] + dv
    
    x[i] = x[i-1] + v[i-1]*dt
    
figure(1)
clf()
subplot(211)
plot(t,v,'bo')
plot(t,(m*g/b)*(exp(-b*t/m)-1),'k')
text(15,-40,r'$v(t) = v_T(e^{-\frac{b}{m}t}-1)$',size=18,color='blue')
plot(t,0*t+v_term,'k--')
plot(t,-g*t,'k--')
ylim(1.1*v_term,v[0])

subplot(212)
plot(t,x)
