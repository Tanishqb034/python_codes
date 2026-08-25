import re
pattern=r"\d{10}"
name_pattern = r"^[A-Za-z ]+$"
age_pattern = r"^\d+$"
email_pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

text="9928996660"
result=re.search(pattern,text)
print(result)     
print(result.group())