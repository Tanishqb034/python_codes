n=int(input("ENTER THE NUM "))
n2=int(input("ENTER THE SECOND NUM "))
c=input("ENTER THE CHOICE + |-|/|%|*| ")

if c=="+":
    print(n+n2)
elif c=="-":
    print(n-n2)
elif c=="/":
    if n2!=0:
      print(n/n2)
    else:
        print("DINOMINATOR IS NOT EQ=0 ")
        
elif c=="*":
       print(n*n2)
elif c=="%":
       print(n%n2)
else:
    print("YOU ENTER INVALID CHOICE ")                    
            