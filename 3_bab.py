def switcher(state,l):
    if state == 0:
        if l == 'a':
            return 0
        elif l == 'b':
            return 1
    elif state == 1:
         if l == 'a':
             return 2
         elif l == 'b':
             return 1
    elif state == 2:
        if l == 'a' :
            return 0
        elif l == 'b':
            return 3
    elif state == 3:
        if l == 'a' or l == 'b' :
            return 3
        
state = 0
    
s = input("Enter the string: ")
for l in s:
    state = switcher(state,l)
print (state)    
if state == 3:
    print("String is accepted")
else :
    print("String is Rejected")
