import csv
list=[1,2,3,4]
name=["TANISHQ","MOHIT","KANISK","RAHUL"]

with open("students.csv","a",newline="") as file:
    writer=csv.writer(file)
    for i in list:
        writer.writerow(i)
            
            