import csv
list=[1,2,3,4]
name=["TANISHQ","MOHIT","KANISK","RAHUL"]

with open("students.csv","a",newline="") as file:
    writer=csv.writer(file)
    for i,j in list,name:
        writer.writerow(i,j)
            