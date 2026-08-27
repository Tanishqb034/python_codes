import re
pattern="TANISHQ"
text="KANISHK"
tet="I LOVE KANISHK"
result=re.sub(text,pattern,tet)
print(result)