n=int(input("ENTER THE NUMBER "))
for i in range (1,n):
    for j in range (1,i+1):
        print(j,end=" ")
    for k in range (i-1,0,-1):
        print(k,end=" ")
    
    print(end="\n")