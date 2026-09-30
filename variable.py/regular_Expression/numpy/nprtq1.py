import numpy as np
a=np.array([76,89,11,32,67,90])
print(np.max(a))
print(np.min(a))
print(np.mean(a))
print(np.sum(a))
print(a[a>75])
print(a[a<75])

salary=np.array([23000,55000,45000,56000,67000,22000])
print(salary[:5])
print(salary[-5:])
print(salary[::])