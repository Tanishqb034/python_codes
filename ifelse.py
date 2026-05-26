username=input("ENTER THE USER NAME ")
password=int(input("ENTER THE PASSWORD"))
if username=="TANISHQ" and password==123:
    print(" WELCOME ",username)
elif username=="TANISHQ" and password!=123:
    print("INVALID  PASSWORD ") 
else:
    print("INVALID USERNAME ")       