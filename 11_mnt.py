inp_mnt=[['MACRO'],
['&LAB', 'ADDM', '&ARG1', '&ARG2'], 
['&LAB', 'A', '1', '&ARG1'],
['','A', '2', '&ARG2'],
['MEND'],
['MACRO'],
['&LAB', 'ADDM', '&ARG1', '&ARG2'], 
['&LAB', 'A', '1', '&ARG1'],
['','A', '2', '&ARG2'],
['MEND']]
op=['A', 'S']
mdtc=0
mnt=[]
flag = 0
count = 0 
for x in inp_mnt :
  if x[0]=='MACRO':
    flag = 1 
  elif len(x)>1 and x[1] not in op: 
    y=[x[1],mdtc]
    mdtc+=1
    mnt.append(y)
  elif x[0]=='MEND':
    mdtc+=1
    flag=0
  else:
    if flag==1:
      mdtc+=1
 
print ("MNT table")
print('='*50)
for s in range (0,len(mnt)):
  print(s,' ',mnt[s][0], mnt[s][1]) 