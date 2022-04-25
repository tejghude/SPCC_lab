i=0
state=0
flag=0
s = input("Enter the string: ")
for x in s:
  if state == 0:
    if x =='<':
      state=1
    elif x=='>':
      state=5
    elif x== '=':
      state=2
    else:
      state= 3
    

  elif state == 1:
    if x=='>':
      state=9
    elif x== '=':
      state = 4
    
    
  elif state == 5:
    if x== '=':
      state=6
    else:
      state=7
  elif state == 4:
    if x== '=':
      state=8

if state==1:
  print('L')
elif state==4:
  print('LE')
elif state==3 or state==7:
  print('INVALID')
elif state==5:
  print('G')
elif state==6:
  print('GE')
elif state==8:
  print('E')
elif state==9:
  print('NT')
