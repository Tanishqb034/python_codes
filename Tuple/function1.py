def sum(a,b):
    return a+b

print(sum(10,20))

def largest(a,b,c):
    return max(a,b,c)
print(largest(10,20,40))

def ODD_even(x):
    if x%2==0 :
        return "EVEN"
    else :
         return "ODD"   
        
print(ODD_even(20))        

def maximum(lst):
    return max(lst)

print(maximum([10,20,30,40,50]))

def minimum(lst):
    return min(lst)

print(minimum([10,20,30,40,50]))


def average(lst):
    return sum(lst) / len(lst)

print(average([10,20,30,40,50]))