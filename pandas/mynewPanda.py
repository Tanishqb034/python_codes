'''
Pandas python ki ek library hai jiska basic use tabluar data ko load, tranform, clean and organize karne ke liye use main liya jaata hai.

Numpy                             Pandas
Basic Data Structure - ndArray    Series / DataFrame
numerical Data                    tabular Data 
to perform numerical operation     to analyse & transform Data set
indexing                          labels and positions dono ho sakte hain.


'''
import pandas as pd
print(pd.__version__)

data = [1,2,3,4,5]
s = pd.Series(data)
print(s)
print(data)
print(type(s))
print(type(data))

a = [12,22,44.22,"Sant"]
b = pd.Series(a)
print(b)
d=["TANISHQ","GAURAV","SANT"]
e=pd.Series(d)
print(e)

roll_no = [1,2,3,4,5,6]
names = ["ram","shyam","ajay","vijay","rohan","sohan"]
my = pd.Series(roll_no,index=names)
print(my)
print(my["vijay"])

print(my.index)
print(my.values)
print(my.dtype)
print(my.shape)
print(my.size)
print(my.ndim)

marks = pd.Series([12,22,33,44,55])
print("Total : ",marks.sum())
print("Average is : ",marks.mean())
print("Max is : ",marks.max())
print("Min is : ",marks.min())
print("Count : ",marks.count())

print(marks+5)
print(marks*10)
print(marks>20)