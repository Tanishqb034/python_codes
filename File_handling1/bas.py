import tkinter
print(tkinter.TkVersion)
with open("THINGS.txt","w") as file:
    d=file.read(5)
    
    print(d)