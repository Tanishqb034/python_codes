import re
pattern=r"\D+"
pattern2=r"\d+"
text="I HAVE 4 Apple 10 ORANGES AND 5 bananan "
result=re.findall(pattern,text)
result1=re.findall(pattern2,text)
print(result1)
print(result)