import csv
with open("students.csv","a",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["MOHIT",22])
    writer.writerow(["HERO",21])