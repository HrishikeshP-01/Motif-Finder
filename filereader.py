global DNA
DNA=[]
def readfile(filename):
    f = open(filename)
    global DNA
    DNA = f.readlines()
    for i in range(len(DNA)-1):
        DNA[i]=DNA[i][0:len(DNA[i])-1]
    print(DNA)
readfile('Hi.txt')
