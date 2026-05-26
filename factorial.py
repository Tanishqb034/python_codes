n=int(input("ENTER THE NUMBER "))
if n==0 or n==1:
    print(1)
else:
    f=1
    for i in range (n,1,-1):
    
         f*=i   
         
print(f)        