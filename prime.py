n=int(input("ENTER THE NUMBER "))
if n<=1:
    print("THE NUMBER IS NOT PRIME ")
else:
    t = 0
    for i in range (2,n):
        if n%i==0:
            t = 1
            break;
    if t==0:
         print("Prime")
    else:
        print("Not")