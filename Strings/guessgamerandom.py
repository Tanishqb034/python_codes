import random
jackpot=random.randint(1,10)
x=int(input("ENTER THE USER INPUT "))
s=True
while(s==True):
    if x>jackpot:
        print("THIS IS GRETER THEN JACKPOT ")
        x=int(input("ENTER THE USER INPUT "))
    elif x<jackpot:
        print("THIS IS LESS THEN JACKPOT ")
        x=int(input("ENTER THE USER INPUT "))
    else:        
        print(" CONGRATULATIONS YOU GUESS RIGHT ")
        s=False