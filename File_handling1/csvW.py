import csv

# 1. Define your data (Headers in the first row, followed by data rows)
data = [
    ["Student_ID", "Name", "Grade"],
    ["S001", "Alice Smith", "A"],
    ["S002", "Bob Jones", "B"],
    ["S003", "Charlie Brown", "A+"]
]


with open("basic.csv", mode="w", newline="") as file:
    
    writer = csv.writer(file)
    

    writer.writerows(data)

print("CSV file created successfully!")
