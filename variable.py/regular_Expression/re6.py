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

pattern3=r"[a-zA-Z ]+$"
my="THIS IS A GOOD CHARECTER LIST "
resultnew=re.findall(pattern3,my)
print(resultnew)
patt=r"\D+"
text4="THIS IS MY 10 SOCKS PACK "
resultpack=re.findall(patt,text4)
print(resultpack)
text5=r"\d+"
pat="THIS IS MY PATTERN "
resu=re.findall(pat,text5)
print(resu)
pa1=r"\W+"
te="THIS IS !) BOOKS 12 pen"
rem=re.findall(pa1,te)
print(rem)
pa2=r"\w+"
te1="THIS IS (!@ BOOKS AND 12 Pen )"
rss=re.findall(pa2,te1)
print(rss)