n=int(input("ENTER THE VALUE OF N "))
C=int(input("ENTER THE COUNTRY OF USER 1 :-> INDIAN || anyother :->: press any"))
if n>18:
    print("THE PERSON CAN GIVE THE VOTE ")
    
    if C==1:
        print("PERSION CAN GIVE VOTE ")
    elif C==2:
         print("PERSION CAN'T GIVE THE VOTE HE IS AMARICAN  ")
    else:
         print("PERSON CAN'T GIVE VOTE PERSON IS FROM OTHER COUNTRY")     
else:
     print("THE PERSON IS UNDER AGE ")             