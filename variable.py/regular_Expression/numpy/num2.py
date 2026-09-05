import numpy as np
a=np.array([1,2,3])
print(a)
b=np.array([
    [1,2,3],[4,5,6]
])
print(b)
c=np.zeros((2,3))
print(c)  #zeroes matrix
d=np.ones((3,3))
print(d)   #one matrix

e=np.eye(3)
print(e) #identity matrix
e=np.diag([1,1])
print(e)
f=np.full((2,2),10)
print(f)
g=np.empty((2,2))
print(g)
h=np.arange(1,10)
print(h)
i=np.arange(0,20,2)
print(i)
j=np.linspace(0,10,5)
print(j)
