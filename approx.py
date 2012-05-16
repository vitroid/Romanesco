from math import *

tau=(sqrt(5)-1)/2
y = [0]*2000
for i in range(2000):
    a = tau*i-floor(tau*i)
    if a>0.5:
        a=1-a
    y[i] = (i,a)
    


y = sorted(y,cmp=lambda p,q:cmp(y[p[0]][1],y[q[0]][1]))
for i in range(100):
    print y[i],tau*y[i][0]
