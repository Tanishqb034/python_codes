list1=[
       [10,20,30],
       [40,50,60],
       [70,80,90]
     ]
total=0
i=0
for row in list1:
    for col in row:
        if row[i]==col:
            total+=col
           
    i+=1
    
print(total)