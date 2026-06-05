x=int(input("ENTER THE NUMBER "))
y=int(input("ENTER THE NUMBER "))
c=0
s=3
for i in range (x,y):
    if i%2==0:
        continue
    c=c+1
print("NO OF ODD NUMBER ",c)    
for i in range(x,y):
    if i==3:
        pass
        s=0
    else:
        print(i)

print(s)       
    