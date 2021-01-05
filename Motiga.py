from random import *
# import tkinter
from tkinter import *
# import filedialog
from tkinter import filedialog
# make root widget
root = Tk()

global ch
global l
global DNA
DNA=[]

# make title label
title = Label(root,text="Motiga")
# changing title font and size
title.config(font=("Courier",44))
# displaying title
title.pack()
# creating option title
# var for optionmenu
var = StringVar()
var.set("Select an algorithm")
opt = ["Select an algorithm","Greedy Motif Search","Randomized Motif Search"]
drop = OptionMenu(root,var,*opt)
drop.pack()

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
    return bm

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
    # make new window for count
    top = Toplevel()
    top.title("Position Based Matrices")
    Label(top,text="Count").pack()
    x="A : "
    for m in a:
        x=x+" "+m
    Label(top,text=x).pack()
    x="C : "
    for m in c:
        x=x+" "+m
    Label(top,text=x).pack()
    x="G : "
    for m in g:
        x=x+" "+m
    Label(top,text=x).pack()
    x="T : "
    for m in t:
        x=x+" "+m
    Label(top,text=x).pack()
    Profile(a,g,c,t,top)

def Profile(a,g,c,t,top):
    total = len(a)
    for i in range(total):
        a[i]=str(float(a[i])/total)
        c[i]=str(float(c[i])/total)
        g[i]=str(float(g[i])/total)
        t[i]=str(float(t[i])/total)
    Label(top,text="Profile").pack()
    x="A : "
    for m in a:
        x=x+" "+m[0:3]
    Label(top,text=x).pack()
    x="C : "
    for m in c:
        x=x+" "+m[0:3]
    Label(top,text=x).pack()
    x="G : "
    for m in g:
        x=x+" "+m[0:3]
    Label(top,text=x).pack()
    x="T : "
    for m in t:
        x=x+" "+m[0:3]
    Label(top,text=x).pack()
    Consensus(a,c,g,t,top)

def Consensus(a,c,g,t,top):
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
    Label(top,text="Consensus").pack()
    we=Label(top,text=consensus)
    we.config(font=("Courier",20))
    we.pack()
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

def randomMat(a,l):
    m=[]
    for i in range(len(a)):
        s=randint(0,len(a[i])-l)
        print(s)
        m.append(a[i][s:s+l])
    tip=Toplevel()
    tip.title("Random Motif Matrix")
    x="Random Matrix"
    for q in m:
        x=x+"\n"+q
    Label(tip,text=x).pack()
    CountRandom(m)

def CountRandom(m):
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
    tipi=Toplevel()
    tipi.title("Position Matrices")
    Label(tipi,text="Count").pack()
    x="A : "
    for we in a:
        x=x+" "+we
    Label(tipi,text=x).pack()
    x="T : "
    for we in t:
        x=x+" "+we
    Label(tipi,text=x).pack()
    x="G : "
    for we in g:
        x=x+" "+we
    Label(tipi,text=x).pack()
    x="C : "
    for we in c:
        x=x+" "+we
    Label(tipi,text=x).pack()
    ScoreRandom(a,t,g,c,h,tipi)

def ScoreRandom(a,t,g,c,h,tipi):
    for i in range(len(a)):
        a[i]=str(float(a[i])/h)
        t[i]=str(float(t[i])/h)
        g[i]=str(float(g[i])/h)
        c[i]=str(float(c[i])/h)
    Label(tipi,text="Score").pack()
    x="A : "
    for we in a:
        x=x+" "+we[0:3]
    Label(tipi,text=x).pack()
    x="T : "
    for we in t:
        x=x+" "+we[0:3]
    Label(tipi,text=x).pack()
    x="G : "
    for we in g:
        x=x+" "+we[0:3]
    Label(tipi,text=x).pack()
    x="C : "
    for we in c:
        x=x+" "+we[0:3]
    Label(tipi,text=x).pack()
    b=BestScorer(a,t,g,c,tipi)

def reiterate(bs,tipi):
    tipi.destroy()
    tiji=Toplevel()
    tiji.title('New Base Matrix')
    Label(tiji,text="New Base Matrix").pack()
    zz=""
    for mm in bs:
        zz=zz+'\n'+mm
    Label(tiji,text=zz).pack()
    print(bs[0])
    CountRandom(bs)

def BestScorer(a,t,g,c,tipi):
    bs=[]
    global DNA
    global l
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
    Label(tipi,text="Newly formulated motif matrix").pack()
    xx=''
    for z in bs:
        xx=xx+'\n'+z
    ll=Label(tipi,text=xx)
    ll.config(font=("Courier",20))
    ll.pack()
    Button(tipi,text="Reiterate?",command=lambda: reiterate(bs,tipi)).pack()

def choice():
    global ch
    global DNA
    global l
    if ch=='Greedy Motif Search':
        bm=greedy(len(DNA),DNA,l)
        print(bm)
        x="Profile Matrix"
        for m in bm:
            x=x+"\n"+m
        prof = Toplevel()
        Label(prof,text=x).pack()
        Count(bm)
    if ch=='Randomized Motif Search':
        randomMat(DNA,l)
        
# fn to display the file selected
def fileclick():
    root.filename=filedialog.askopenfilename(initialdir="C:",title="Select DNA sequence file",
                                         filetypes=(("text files","*.txt"),
                                                    ("csv files","*.csv"),
                                                    ("all files","*.*")))
    try:
        print(root.filename)
        readfile(root.filename)
        fbutton['text']=root.filename
        
    except:
        print('try again')
fbutton=Button(root,text="Select DNA sequence file",command=fileclick)
fbutton.pack()

# fn to make default text disappear from entry on mouse click and reappear when the user
# focus shifts and he hasn't entered anything yet
def on_entry_click(event):
    if e.get()=='Enter motif length here':
        e.delete(0,"end")
        e.insert(0,"")
def on_focusout(event):
    if e.get()=='':
        e.insert(0,"Enter motif length here")
e = Entry(root)
e.insert(0,'Enter motif length here')
e.bind('<FocusIn>',on_entry_click)
e.bind('<FocusOut>',on_focusout)
e.pack()

# fn to store the option selected
def algoclick():
    global ch
    ch = var.get()
    print(ch)
    global l
    l=int(e.get())
    choice()
Button(root,text="Go!",command=algoclick).pack()

# fn to read DNA sequence
def readfile(filename):
    f = open(filename)
    global DNA
    DNA = f.readlines()
    for i in range(len(DNA)-1):
        DNA[i]=DNA[i][0:len(DNA[i])-1]
    print(DNA)     
    
# loop for gui
root.mainloop()
