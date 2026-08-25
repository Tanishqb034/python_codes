import re
name_pattern = r"^[A-Za-z ]{2,}$"
age_pattern = r"^(0|[1-9]\d*)$"
email_pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
name = "Tanishq Bhardwaj"
age = "21"
email = "tanishq@gmail.com"
if type (re.fullmatch(age_pattern, age))=="object":
    print('Age is Value')
else:
    print('Age is Invalid')
print(re.fullmatch(name_pattern,name))
print(re.fullmatch(email_pattern, email))

