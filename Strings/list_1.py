s=0
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1)
print(len(list1))
print(list1[0])
print(list1[-1])
print(list1.index(5))
list1[5]=100
print(list1[5])
list2=["apple","Banana","Cherry"]
list2.append("MANGO")
print(list2)
list2.remove("apple")
print(list2)
list3=[22,33,44,55,66]
print(max(list3))
print(min(list3))
x=len(list3)
for i in range (0,x):
    s+=list3[i]
    
avg=s/len(list3)
print(avg)  
cities = ["Delhi", "Mumbai", "Jaipur", "Pune", "Chennai"]
print(cities[0:3]) 
print(cities[-2:])
cities.reverse()
print(cities)