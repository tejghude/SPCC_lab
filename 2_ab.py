## ends with ab
s = input("Enter the string: ")
state=0
for x in s :
    if state == 0:
      if x == 'a':
        state = 1
      elif x == 'b':
        state = 0

    elif state == 1: 
      if x == 'a':
        state = 1
      elif x == 'b':
        state = 2

    elif state == 2:
      if x == 'a' :
        state = 1
      elif x == 'b':
        state = 0

if state == 2:
    print("String is accepted")
else :
    print("String is Rejected")