s="Artificial INTELLIGENCE"
print(len(s))
print(s[0])
print(s[-1])
print(s[0:5])
print(s[-5:])
first="Machine "
second="Learning"
x=first+second
print(x)
d="Data Science with Python"
print(d.lower())
print(d.upper())
strt="Python is powerful and Python is easy"
pyth=strt.count("Python")
print(pyth)
isss=strt.count("is")
a=strt.count("a")
print(a)

strii=" I LOVE JAVA "
print(strii.replace("JAVA","PYTHON"))
sss="DeepLearning"
ass=sss[::-1]
print(ass)
nest=sss+sss[3:6:2]+sss[6]
print(nest)

axe="TANISHQ"
print(axe[1:7:2])
ad="TANISHQ IS A BAD BOY"
print(ad.count(" "))
add="LOVE"
rev=add[::-1]
if rev== add:
    print("Palandrome")
else:
    print ("NOT A PALANDROME ")    
 
bss="TANISHQ BHARDWAJ"
res=""
rr=""
zx=0
for char in bss:
    if char not in res:
        res+=char
    else:
        rr+=char
        zx=zx+1
            
        
print(res)
print(rr)  
print(zx)      