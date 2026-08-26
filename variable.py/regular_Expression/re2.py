import re
pattern="12344"
text="abcd te45 12344 "
result=re.fullmatch(pattern,text)
print(result)