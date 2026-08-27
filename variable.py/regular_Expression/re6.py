import re
pattern=r"[a-z]"
text="THIS 7 is mmy hobby 12@#$"
result=re.findall(pattern,text)
print(result)
pattern2=r"[A-Z]"
result2=re.findall(pattern2,text)
print(result2)
digi=r"[0-9]"
result3=re.findall(digi,text)
print(result3)
allinone=r"[a-zA-Z0-9]"
result4=re.findall(allinone,text)
print(result4)
name_pat=r"^[A-Za-z ]+$"
name="TANISHQ BHARDWAJ"
result_name=re.findall(name_pat,name)
print(result_name)