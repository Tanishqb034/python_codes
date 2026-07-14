b = [1,2,3,4,-1,0,9,-3,12,-7]
res4 = filter(lambda x : x<0 , b)
print(list(res4))

c=["TANISHQ","GAURAV","HELLO","HI","","sant","","jangid"]
rest=filter(lambda x: len(x)>5 ,c)
print(list(rest))
student ={'Gourav' : 12 , 'Someone' : 86 , 'Anyone' : 98 , 'Ok' : 76}
greter_50 = filter(lambda x : x[1]>50,student.items())
print(dict(greter_50))
print(list(greter_50))

rpi=filter(lambda x : len(x)!=0, c)
print(list(rpi))

b = list(filter(None,c))
print(b)

letters = ['a','e','t','y','e','o','u','k','r']
vowels =filter(lambda x: x in "aeiou",letters)
print(list(vowels))
