# Exercise 11

nums = list(range(1, 21))

even = [i for i in nums if i % 2 == 0]
odd = [i for i in nums if i % 2 != 0]

print("Even:", even)
print("Odd:", odd)


# Exercise 12

nums = list(range(1, 16))

cubes = [i**3 for i in nums]

print("Cubes:", cubes)


# Exercise 13

words = ["python", "java", "c", "javascript"]

upper_words = [word.upper() for word in words]

print("Uppercase:", upper_words)


# Exercise 14

numbers = [5, 10, 15, 20, 25]

greater_than_10 = [i for i in numbers if i > 10]

print("Greater than 10:", greater_than_10)


# Exercise 15

names = ["amit", "rahul", "pooja", "rani"]

capital_names = [name.capitalize() for name in names]

print("Capitalized Names:", capital_names)


# Exercise 16

data = [
    [10, 20],
    [30, 40],
    [50, 60]
]

total = 0

for row in data:
    for value in row:
        total += value

print("Sum:", total)


# Exercise 17

students = [
    ["Amit", 78],
    ["Rahul", 85],
    ["Pooja", 92]
]

highest = students[0]

for student in students:
    if student[1] > highest[1]:
        highest = student

print("Highest Marks Student:", highest[0])


# Exercise 18

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal = []

for i in range(len(matrix)):
    diagonal.append(matrix[i][i])

print("Diagonal:", diagonal)
print("Diagonal Sum:", sum(diagonal))


# Exercise 19

nums = [1, 2, 3, 2, 4, 5, 1, 6, 3]

duplicates = []

for i in nums:
    if nums.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicates:", duplicates)


# Exercise 20

nums = [10, 20, 10, 30, 40, 20, 10]

freq = {}

for i in nums:
    freq[i] = freq.get(i, 0) + 1

print("Frequency:", freq)


# Exercise 21

items = ["Apple", "Banana", "Apple", "Mango", "Banana", "Apple"]

freq = {}

for item in items:
    freq[item] = freq.get(item, 0) + 1

most_item = max(freq, key=freq.get)

print("Most Frequent Item:", most_item)


# Exercise 22

nums = [10, 20, 30, 40, 50]

largest = max(nums)
second = max([i for i in nums if i != largest])

print("Second Largest:", second)


# Exercise 23

nums = [5, 1, 8, 3, 9, 2]

largest = nums[0]

for i in nums:
    if i > largest:
        largest = i

print("Largest:", largest)


# Exercise 24

nums = [1, 2, 3, 4, 5]

left_rotate = nums[1:] + [nums[0]]

print("Left Rotate:", left_rotate)


# Exercise 25

nums = [1, 2, 3, 4, 5]

right_rotate = [nums[-1]] + nums[:-1]

print("Right Rotate:", right_rotate)


# Exercise 26

nums = [1, 2, 3, 2, 1]

if nums == nums[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Exercise 27

nums = [1, 2, 3, 4, 5]

reverse = []

for i in range(len(nums)-1, -1, -1):
    reverse.append(nums[i])

print("Reverse:", reverse)


# Exercise 28

nums = [1, 2, 3, 4, 5, 6, 7, 8]

even = []
odd = []

for i in nums:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even.sort()
odd.sort()

print("Even:", even)
print("Odd:", odd)


# Exercise 29

nums = [10, 20, 30, 40, 50]

running_sum = []
total = 0

for i in nums:
    total += i
    running_sum.append(total)

print("Running Sum:", running_sum)


# Exercise 30

nums = [1, 2, 3, 4, 5]

pairs = []

for i in range(len(nums)-1):
    pairs.append((nums[i], nums[i+1]))

print("Adjacent Pairs:", pairs)