n=int(input("ENTER THE NUMBER "))
f=1
s=0
for i in range (1,n+1):
    f*=i
    s+=i/f
print(s)    