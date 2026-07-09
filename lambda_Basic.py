a = [321,321,3,12,3,21,3,21,44,355,3,4,654,6,546,54,7,657,65]
res = filter(lambda i : i%2==0, a)
print(list(res))
res2 = filter(lambda x : x%2!=0, a)
print(list(res2))
res3= filter(lambda x :x>10 ,a)
print(list(res3))