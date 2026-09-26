import numpy as np

a=np.array([1,2,3,4,5,6])
print(np.max(a))


print(np.min(a))
num=np.array([80,90,90,99,100])
print(np.average(num))

print(np.sum(num))

result=np.where(num>75)
print(result)
r=num[num>75]
print(r)