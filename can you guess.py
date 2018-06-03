import random
n=0
z=[]
m=[]
k=0
while k!='q':
 x = random.randint(1, 9)
 y = int(input("enter your no.\n"))
 n=n+1
 z.append(x)
 m.append(y)
 if x==y:
    print("you are lucky")
    break
 elif x>y :
    if x-y>=3:
        print('guessed too low')
    else:
        print('you are close')
 elif x<y :
    if y-x>=3:
        print('guessed too high')
    else:
        print('you are close')

 k=input("if want to quit then press q\n")
 if k=="q":
    break
print(z)
print(m)
print("you guessed ",n,"times to get it right")
