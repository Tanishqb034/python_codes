lst = [2,4,3,5,7,8]
target = 9

for i in range(len(lst)):

    for j in range(i+1, len(lst)):

        if lst[i] + lst[j] == target:
            print(lst[i], lst[j])