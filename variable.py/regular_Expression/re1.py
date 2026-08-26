import re

text="TANISHQ BHARDWAJ Python"
pattern="TANISHQ"
result=re.search(pattern,text)
print(result)
print(result.start())
print(result.end())
if result:
    print("MATCH")
else:
    print("Not MATCH")    
    
result_2=re.match(pattern,text)  
print(result_2.group())
