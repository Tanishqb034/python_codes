
text = "Artificial Intelligence"

print("Total characters:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])
print("First 5 characters:", text[:5])
print("Last 5 characters:", text[-5:])

first = "Machine"
second = "Learning"
print("Concatenation:", first + " " + second)

text2 = "Data Science with Python"
print(text2.upper())
print(text2.lower())
print(text2.title())

sentence = "Python is powerful and Python is easy"
print("Python count:", sentence.count("Python"))
print("is count:", sentence.count("is"))
print("a count:", sentence.count("a"))

text3 = "I love Java"
print(text3.replace("Java", "Python"))


word = "DeepLearning"
print(word[:4])
print(word[4:])
print(word[2:5])
print(word[::-1])

print("Every second char:", "PythonProgramming"[::2])


name = input("Enter name: ")
print("Hello", name)
print("Length =", len(name))

sentence = input("Enter sentence: ")

vowels = "aeiouAEIOU"
v = 0
c = 0

for ch in sentence:
    if ch in vowels:
        v += 1
    elif ch.isalpha():
        c += 1

print("Vowels:", v)
print("Consonants:", c)
print("Spaces:", sentence.count(" "))



s = input("Enter word: ")
print("Palindrome:", s == s[::-1])

email = input("Enter email: ")
print("Valid email:", "@" in email and ".com" in email)

password = input("Enter password: ")

print("Strong password:",
      len(password) >= 8 and
      any(c.isupper() for c in password) and
      any(c.islower() for c in password) and
      any(c.isdigit() for c in password))


text = "Python"

for ch in text:
    print(ch)

text = "Python3 @AI"

upper = 0
lower = 0
digits = 0
spaces = 0
special = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Upper:", upper)
print("Lower:", lower)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special:", special)



text = "I love AI and AI loves data"
print("Word count:", len(text.split()))



sentence = "AI AI ML Data AI Data Python"
print("Unique words:", set(sentence.split()))

clean = " AI    is      powerful "
print("Clean sentence:", " ".join(clean.split()))




reviews = ["I love AI", "AI is difficult", "Python is great"]
lower_reviews = [r.lower() for r in reviews]
print(lower_reviews)

arr = ["AI", "ML", "AI", "Python"]
print(list(set(arr)))


text = input("Enter sentence ")

positive = ["good", "excellent", "happy"]
negative = ["bad", "poor", "sad"]

score = 0

for w in text.lower().split():
    if w in positive:
        score += 1
    if w in negative:
        score -= 1

if score > 0:
    print("Positive")
elif score < 0:
    print("Negative")
else:
    print("Neutral")