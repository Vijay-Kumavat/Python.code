import numpy as np
import re

def gtval(t):
    try:
        if t[0] == -1 or t[1] == -1:
            return -1
        return a[t[0], t[1]]
    except:
        return -1

def findar(m, d):
   
    ict = {
        "nxt": tuple([m[0], m[1]+1]),
        "bck": tuple([m[0], m[1]-1]),
        "up" : tuple([m[0]-1, m[1]]),
        "dwn" : tuple([m[0]+1, m[1]])
    }
   
    valdict = {
        "nxt" : gtval(ict['nxt']),
        "bck" : gtval(ict['bck']),
        "up" : gtval(ict['up']),
        "dwn" : gtval(ict['dwn'])    
    }
   
    vl = sorted(valdict.items(), key=lambda x: x[1], reverse=True)
    for m in vl:
        if ict[m[0]] not in d:
            return ict[m[0]]
   
# a = np.array([[0,1,5,0,0],[2,0,1,0,1],[3,4,0,5,5],[6,7,8,0,9]], int)
a = np.array([[9,1,1,0,7],[1,0,2,1,0],[1,9,1,1,0]], int)
p = []

for i in a:
    p.extend(list(i))
dim = a.shape

pct = []
if dim[0] ==1 or dim[1] == 1:
    strlst = map(str, p)
    for q in range(len(p)):
        pct.append(p[q:q+4])
    c = [j for j in pct if len(j) ==4]
    final = []
    for q in c:
        final.append("".join(map(str,list(q))))
    print(max(map(int, final)))
else:
    dct = {}
    q = list(zip(*np.where(a == max(p))))
   
    for i in q:
        n = i
        dct[n] = []
        dct[n].append(i)
        for j in range(3):
            i = findar(tuple(i), dct[n])
            dct[n].append(i)
   
    vals = []
    for i,j in dct.items():
        s= ""
        for o in j:
            s += str(a[o[0]][o[1]])
        vals.append(s)
    print(max(map(int, vals)))
