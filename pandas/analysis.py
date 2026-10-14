import pandas as pd
data = {
    "Name" : ["Ram","Shyam","Mohan","Rohit","Mohit"],
    "Python" : [12,44,55,66,77],
    "Java" : [55,66,77,45,45],
    "DSA" : [34,44,55,66,77]
}

df = pd.DataFrame(data)
df["Total"] = df["Python"] + df["Java"] + df["DSA"]
df["Average"] = df[["Python","Java","DSA"]].mean(axis=1)
df["Result"]= df["Average"].apply(
    lambda x : "Pass" if x >=60 else "Fail"
)
df = df.sort_values("Average",ascending=False)
print(df)
