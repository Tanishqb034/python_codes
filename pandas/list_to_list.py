import pandas as pd 
data = [
    ["RAm",12,33],
    ["Shyam",24,55],
    ["Amit",55,33]
]
df = pd.DataFrame(
    data,columns=["Name","Age","Marks"]
)
print(df)

prod = {
    "Products" : ["Laptop","Mouse","Keyboards","Monitors"],
    "Price" : [50000,200,150,5000],
    "Stock" : [10,20,30,50]
}
df = pd.DataFrame(prod)
print(df)

p = [
    {"Name" : "Tanishq","Marks":44},
    {"Name" : "Gaurav","Marks":34}
]
df = pd.DataFrame(p)
print(df)

q = [
    {"Name" : "Rahul","Marks":55},
    {"Name" : "Sant","Marks" : 90, "City" : "Jaipur"},
    {"Name" : "Gaurav","Marks" : 44}
]
df = pd.DataFrame(q)
print(df)