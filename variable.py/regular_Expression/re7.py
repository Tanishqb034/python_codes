import re

text = "efgge"

result = re.fullmatch(r"[efg]+", text)

if result:
    print("Valid")
else:
    print("Invalid")