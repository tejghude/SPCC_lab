##No. of lines :3
##1=a+b
##2=1-c
##x=2

n = int(input("No. of lines :"))
tac =[]

def op(y):
    if y=='+':
        return 'ADD'
    elif y=='-':
        return 'SUB'
    elif y=='*':
        return 'MUL'
    elif y=='/':
        return 'DIV'

for _ in range(n):
    temp = str(input())
    tac.append(temp)
print(tac)
t=0
reg=[]
s=[]
for x in tac :
    if len(x)==5:
        if not s or s[-1]!=x[2]:
            reg.append('R'+str(t))
            s.append(x[2])
            print('MOV',reg[-1],s[-1])
            t+=1
            reg.append('R'+str(t))
            s.append(x[4])
            print('MOV',reg[-1],s[-1])
            t+=1
            print(op(x[3]),reg[-2],reg[-1])
            reg.append(reg[-2])
            s.append(x[0])

        elif s[-1]==x[2]:
            reg.append('R'+str(t))
            s.append(x[4])
            print('MOV',reg[-1],s[-1])
            t+=1
            print(op(x[3]),reg[-2],reg[-1])
            reg.append(reg[-2])
            s.append(x[0])

    elif len(x)==3:
        print('MOV',x[0],reg[-1])