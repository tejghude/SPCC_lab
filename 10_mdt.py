inp_mdt=[['MACRO'],
['&LAB', 'ADDM', '&ARG1', '&ARG2', '&ARG3'], 
['&LAB', 'A', '1', '&ARG1'],
['','A', '2', '&ARG2'],
['','A', '3', '&ARG3'],
['MEND']]
op=['A', 'S']
mdtc=0
mntc=0
mdt=[]
mnt=[]
ala=[]

def createala(xt):
    tc = xt
    tc.pop(1)
    ala.extend(tc)

print ("MACRO definition table")
print('='*50)
for x in inp_mdt:
    if x[0]=='MACRO': 
        continue
    elif len(x)>1 and x[1] not in op:
    ## code for ALA will need only this elif
        print ([mdtc,x]) # first line of mdt was printed here
        mdtc+=1
        createala(x)
    elif len(x)>1 and x[1] in op : 
        temp = x
        yt=[]
        for y in range (len(temp)):
            if temp[y] in ala :
                yt.append('#' + str(ala.index(temp[y])))
            else :
                yt.append(temp[y])
        t=[mdtc,yt]
        mdtc+=1
        mdt.append(t)
    elif x[0]=='MEND':
        t=[mdtc, ['MEND']]
        mdtc+=1
        mdt.append(t)

for d in mdt: 
    print (d)