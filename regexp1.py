import re
pattern=r"\d{10}"
text="9928996660"
result=re.search(pattern,text)
print(result)     
print(result.group())