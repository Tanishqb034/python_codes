from functools import reduce

numbers = [1, 2, 3, 4]
# Multiplies elements step-by-step: ((1 * 2) * 3) * 4
result = reduce(lambda x, y: x * y, numbers) 
print(result) 
