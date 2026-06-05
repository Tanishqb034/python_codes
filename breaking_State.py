x=int(input("ENTER UPPER"))
y=int(input("ENTER THE LOWER "))

for i in range(x,y+1):
    for j in range (2,i):
        if i%j==0:
            break
    else:
            print(i)