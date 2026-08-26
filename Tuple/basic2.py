import re
pattern=r"\d+"
text="I HAVE 10 mango 12 banana and 6 apple"
result=re.findall(pattern,text)
print(result)