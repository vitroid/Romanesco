# romanesco

from math import *


def length(a):
    s = 0
    for x in a:
        s += x**2
    return sqrt(s)    


def normalize(a):
    s= 1.0/length(a)
    b = [0.0] * 3
    for i in range(len(a)):
        b[i] = a[i] * s
    return b
        

def romanesco(origin,direc,depth):
    #decorate a vector
    #define a vector orthogonal to direc vector
    s = length(direc)
    end = [0.0]*3
    for i in range(3):
        end[i] = origin[i]+direc[i]
    if s < 10:
        ovals = ((origin,end,depth),)
    else:
        ovals = ()
        e0 = (0.0,0.0,1.0)
        e1 = (direc[1]*e0[2]-direc[2]*e0[1],
              direc[2]*e0[0]-direc[0]*e0[2],
              direc[0]*e0[1]-direc[1]*e0[0])
        e2 = (direc[1]*e1[2]-direc[2]*e1[1],
              direc[2]*e1[0]-direc[0]*e1[2],
              direc[0]*e1[1]-direc[1]*e1[0])
        e1 = normalize(e1)
        e2 = normalize(e2)
        e0 = tuple(direc)
        e0 = normalize(e0)
        ss = s*0.5
        th = 0.0
        tau = (sqrt(5.0)-1)*pi 
        while ss > 10:
            ori = [0.0] * 3
            costh = cos(th)
            sinth = sin(th)
            th += tau
            depth *= 0.98
            for i in range(3):
                ori[i] = origin[i] + e0[i]*(s - ss)
            r = ss / 2.0
            horiz = [0.0] * 3
            horiz[0] = e1[0]*costh + e2[0]*sinth
            horiz[1] = e1[1]*costh + e2[1]*sinth
            horiz[2] = e1[2]*costh + e2[2]*sinth
            dir = [0.0] * 3
            dir[0] = r*(e0[0] + horiz[0])
            dir[1] = r*(e0[1] + horiz[1])
            dir[2] = r*(e0[2] + horiz[2])
            end = [0.0]*3
            for i in range(3):
                end[i] = ori[i]+dir[i]
            #ovals += ((ori,end,depth),)
            ovals += romanesco(ori,dir,depth)
            ss *= 0.98
        ori = [0.0] * 3
        for i in range(3):
            ori[i] = origin[i] + e0[i]*(s - ss)
        dir = [0.0] * 3
        dir[0] = ss*e0[0]
        dir[1] = ss*e0[1]
        dir[2] = ss*e0[2]
        #ovals += ((ori,dir,depth),)
        ovals += romanesco(ori,dir,depth)
    return ovals

origin = (250,800,0)
direc  = (0,-700,0)
ovals = romanesco(origin,direc,1.0)
print len(ovals)
fill(1,1,1)
stroke(0)
colormode(HSB)
size(500,500)
rad=3
#for o,e,d in sorted(ovals,cmp=lambda x,y:cmp(x[1][2],y[1][2])):
#    line(o[0],o[1],e[0],e[1])
#for o,e,d in sorted(ovals,cmp=lambda x,y:cmp(x[1][2],y[1][2])):
#    oval(e[0]-rad,e[1]-rad,2*rad,2*rad)
for o,e,d in sorted(ovals,cmp=lambda x,y:cmp(y[1][1],x[1][1])):
    oval(e[0]-rad,e[2]-rad+250,2*rad,2*rad)
    