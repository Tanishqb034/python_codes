import re

text="TANISHQ BHARDWAJ Python"
pattern="Python"
result=re.search(pattern,text)
print(result)
print(result.start())
