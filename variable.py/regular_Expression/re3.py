import re
pattern=r"\D+"
text="I HAVE 4 Apple 10 ORANGES AND 5 bananan "
result=re.findall(pattern,text)
print(result)