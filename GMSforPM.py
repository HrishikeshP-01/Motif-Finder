# fn to find the hamming distance btw 2 sequences
def Ham(x,y):
    s=0
    for i in range(0,len(x)):
        if x[i]!=y[i]:
            s=s+1
    return s

# fn to find the best motifs from the 1st 2 sequences
def first(x,y,l):
    bm=["",""]
    bs=l
    for i in range(0,len(x)-l+1):
        h=x[i:i+l]
        for j in range(0,len(y)-l+1):
            p=y[j:j+l]
            s=Ham(h,p)
            if s<bs:
                bs=s
                bm[0]=h
                bm[1]=p
    return bm

#fn to find the motif matrix using greedy search
def greedy(t,DNA,l):
    bm=first(DNA[0],DNA[1],l)
    for i in range(2,t):
        z=DNA[i]
        bs=len(z)*len(bm)
        bms=""
        for j in range(0,len(z)-l+1):
            h=z[j:j+l]
            s=0
            for p in range(0,len(bm)):
                s=s+Ham(h,bm[p])
            if s<bs:
                bs=s
                bms=h
        bm.append(bms)
    print(bm)
    Count(bm)

def Count(bm):
    a=[]
    for i in range(len(bm[0])):
        a.append("1")
    c=a.copy()
    g=a.copy()
    t=a.copy()
    for i in range(len(bm)):
        for j in range(len(bm[i])):
            if bm[i][j]=='A':
                a[j]=str(int(a[j])+1)
            if bm[i][j]=='C':
                c[j]=str(int(c[j])+1)
            if bm[i][j]=='G':
                g[j]=str(int(g[j])+1)
            if bm[i][j]=='T':
                t[j]=str(int(t[j])+1)
    print(a)
    print(g)
    print(c)
    print(t)
    Profile(a,g,c,t)

def Profile(a,g,c,t):
    total = len(a)
    for i in range(total):
        a[i]=str(float(a[i])/total)
        c[i]=str(float(c[i])/total)
        g[i]=str(float(g[i])/total)
        t[i]=str(float(t[i])/total)
    print(a)
    print(c)
    print(g)
    print(t)
    Consensus(a,c,g,t)

def Consensus(a,c,g,t):
    con=a.copy()
    for i in range(len(a)):
        m='A'
        mc=float(a[i])
        if(mc<float(g[i])):
            m='G'
            mc=float(g[i])
        if(mc<float(c[i])):
            m='C'
            mc=float(c[i])
        if(mc<float(t[i])):
            m='T'
        con[i]=m
    consensus=("".join(con))
    print(consensus)

def Score(a,g,c,t,mo):
    s=0
    for i in range(len(mo)):
        if mo[i]=='A':
            s=s+float(a[i])
        elif mo[i]=='C':
            s=s+float(c[i])
        elif mo[i]=='G':
            s=s+float(g[i])
        elif mo[i]=='T':
            s=s+float(t[i])
    print(s)
    return s

greedy(4,["ATTGT","AATGT","AATTG","TGTAA"],3)



        
    
