import pandas as pd
data = {
    "Name" : ["RAJAT","MOHIT","LAKSHYA","PRATAP"],
    "Age" : [24,44,32,22],
    "Roll_no" : [1,2,3,4],
    "Marks" : [89,88,78,90],
    "City" : ["Jaipur","Delhi","Lahore","Karachi"]
}

a = pd.DataFrame(data)
print(a)
print(type( a))

print(a.shape)
print(a.columns)
print(a.index)
print(a.dtypes)
print(a.size)
print(a.ndim)

print(a.head())
print(a.head(2))
print(a.tail())
print(a.tail(2))
print(a.info())

print(a.describe())
print(a["Name"])
print(a[["Name","Marks"]])
print(a.iloc[0])
print(a.iloc[2])
print(a[a["Marks"]>=80])
print(a[(a["Marks"] >= 80) & (a["Age"] >=25)])

