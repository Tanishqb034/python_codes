import re
pattern="TANISHQ"
text="TANISHQ IS VERY GOOD BOY "
result=re.match(pattern,text)
print(result.group())
print(result.start())
print(result.end())