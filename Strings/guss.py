import random
x=int(input("ENTER THE JACKOT NUMBER "))
s=True
while(s==True):
    if x>3:
        print("NUM IS GREATER THEN JACK POT ")
        x=int(input("ENTER THE JACKOT NUMBER "))
    elif x<3:
        print("NUM IS LESS THEN JACKPOT ")
        x=int(input("ENTER THE JACKOT NUMBER "))
    else:
         print(" CONGRATULATIONS YOU GUSS COREECT NUMBER ") 
         s=False       
   