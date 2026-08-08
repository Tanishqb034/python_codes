def student(*name):
    print(name)
    
student("Tanishq","HARDIK","Vyom") 

def total(*numbers):
    # a,b,c,d,e = numbers
    # sum = a+b+c+d+e
    l = list(numbers)
    print(l)
    sum = 0
    for i in l:
        sum += i
    print(sum)    
total(1,2,3,4,5)    

def kinderjoy(**hi):
    print(hi)
    print(hi.keys())
    print(hi.values())
    
kinderjoy(hi="Tanishq",he="TANMAY",h="SIMBHA")  
  

numbers = (1, 2, 3)

print(*numbers)
