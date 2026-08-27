import re
pattern=r"[a-z]"
text="THIS 7 is my hobby 12"
result=re.findall(pattern,text)
print(result)
pattern2=r"[A-Z]"
result2=re.findall(pattern2,text)
print(result2)
digi=r"[0-9]"
result3=re.findall(digi,text)
print(result3)