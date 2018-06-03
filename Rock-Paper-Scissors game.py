import random
print("Rock-Paper-Scissors game")

list=['rock','paper','scissors']

while True:
 x = input("your turn\n")
 y = random.choice(list)
 print(y)
 if y==x:
       print("try again")
 elif (y=='scissors' and x=='rock') or (y == 'rock' and x == 'paper') or (y == 'paper' and x == 'scissors'):
        print("you won\n")



 else:
    print("you lost\n")

 quit=input("press q to quit or any other key to play\n")
 if quit=='q':
     print("bye")
     break
