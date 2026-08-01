with open("THINGS.txt","r") as file:
    d=file.readlines()
    
for line in d:
    print(line.strip())
    