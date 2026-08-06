import csv

student=[
    [106,"TANISHQ","JAIPUR"],
    [107,"KANISKH","ALWAR"],
    [108,"HIMASHI","AJMER"]
]
with open("students.csv","a",newline="") as file:
    writer=csv.writer(file)
    writer.writerows(student)
    