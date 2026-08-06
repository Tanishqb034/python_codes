import csv

# 1. Define your data (Headers in the first row, followed by data rows)
data = [
    ["Student_ID", "Name", "Grade"],
    ["S001", "Alice Smith", "A"],
    ["S002", "Bob Jones", "B"],
    ["S003", "Charlie Brown", "A+"]
]

# 2. Open the file in write mode ('w')
with open("basic.csv", mode="w", newline="") as file:
    # 3. Create a CSV writer object
    writer = csv.writer(file)
    
    # 4. Write all rows to the file
    writer.writerows(data)

print("CSV file created successfully!")
