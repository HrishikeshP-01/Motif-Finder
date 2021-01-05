from random import *

def randomMat(a,l):
    m=[]
    for i in range(len(a)):
        s=randint(0,len(a[i])-l)
        print(s)
        m.append(a[i][s:s+l])
    print(m)
    return m

def Count(m):
    a=[]
    for i in range(len(m[0])):
        a.append("1")
    c=a.copy()
    g=a.copy()
    t=a.copy()
    h=len(m)
    for i in range(h):
        for j in range(len(m[i])):
            if m[i][j]=='A':
                a[j]=str(int(a[j])+1)
            if m[i][j]=='T':
                t[j]=str(int(t[j])+1)
            if m[i][j]=='G':
                g[j]=str(int(g[j])+1)
            if m[i][j]=='C':
                c[j]=str(int(c[j])+1)
    print(a)
    print(t)
    print(g)
    print(c)
    Score(a,t,g,c,h)

def Score(a,t,g,c,h):
    for i in range(len(a)):
        a[i]=str(float(a[i])/h)
        t[i]=str(float(t[i])/h)
        g[i]=str(float(g[i])/h)
        c[i]=str(float(c[i])/h)
    print(a)
    print(t)
    print(g)
    print(c)
    global x
    b=BestScorer(x,2,a,t,g,c)

def BestScorer(DNA,l,a,t,g,c):
    bs=[]
    for i in range(len(DNA)):
        ms=0
        bm=""
        x=DNA[i]
        for j in range(len(x)-l+1):
            d=x[j:j+l]
            s=float(0)
            for q in range(len(d)):
                if d[q]=='A':
                    s=s+float(a[q])
                elif d[q]=='T':
                    s=s+float(t[q])
                elif d[q]=='G':
                    s=s+float(g[q])
                elif d[q]=='C':
                    s=s+float(c[q])
            if s>ms:
                ms=s
                bm=d
        bs.append(bm)
    print(bs)
    return bs

global x
x=['AAAC','TTAA','AAGA']
m=randomMat(x,2)
Count(m)
