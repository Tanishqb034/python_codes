t=(10,20,30,40,50)
print(t)
print(type(t))
#print last element tuple
print(t[-1])
#print last element tuple
print(t[0])


# print 3 element
print(t[2])
#print len of tuple

print(len(t))

#print looping in tuple
for i in t:
    print(i)
    
    #check tuple has element
    
print(50 in t)  

#check 100 in tuple or not

print(100 in t)  

#max in tuple
print(max(t))

#min in tuple 
print(min(t))

#sum of tuple
print(sum(t))
#function
sr=0
for i in t:
    sr+=i
    
print(sr)
#slicing in tuple 
#first 3 element
print(t[:3])

#skip 1 -1 element
print(t[:len(t):2])

#last 3 element

print(t[-3:])

#middle element

#number of records in tuple
employees = (
    (101, "Amit", "IT", 55000),
    (102, "Neha", "HR", 45000),
    (103, "Ravi", "Sales", 60000),
    (104, "Priya", "IT", 70000),
    (105, "Karan", "Finance", 65000),
    (106, "Pooja", "HR", 48000)
)
print(len(employees))

#print(first employee info)

print(employees[0])

#print(last employee info)

print(employees[len(employees) -1])

for i in employees:
     print(i[2])
     
for i in employees:
    print(i[3])  
    
for i in employees:
    print(i[0])    
    
    