lst = [1,2,3,4,5]

st = 0
end = len(lst)-1

while st < end:

    temp = lst[st]
    lst[st] = lst[end]
    lst[end] = temp

    st += 1
    end -= 1

print(lst)