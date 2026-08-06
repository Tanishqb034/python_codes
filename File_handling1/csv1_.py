import csv

# 1. Open the file in read mode ('r')
with open('basic.csv', mode='r') as file:
    
    # 2. Create a reader object
    csv_reader = csv.reader(file)
    
    # 3. Loop through each row and print it
    for row in csv_reader:
        print(row)
