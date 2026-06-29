#Functions in Python


def sum(a,b):
  return a+b

print(sum(12,22))
     

a = 10
def test():
  a=100
  print(a)

test()
a=44
print(a)
     


x = 10
def change():
  global x
  x = 100
change()
print(x)
     


# Types of Arguments
# keyword arguments
def student(name,age):
  print(name,age)
student(12,'Sant')
student(age=12,name='Sant')
     


# 2. Default ARguments
def hello(name='SAnt'):
  print(name)
hello()
hello('Tanishq')
     

#3. variable length arguments
def total(*n):
  print(n)
total(22,22)
total(432,34,24,2,432,4,32,4324)
     


#4. Keyword Vairable length arguments
def show(**student):
  print(student)
show(name='Sant',course='AI',batch='ebvening')
     
{'name': 'Sant', 'course': 'AI', 'batch': 'ebvening'}

#Mixin Arguments
def demo(a,b,*c,**d):
  print(a)
  print(b)
  print(c)
  print(d)
demo(12,22,22,33,x=100,y=200)
     


# NEsted Functions
def hello():
  print("Hello")
  def hi():
    print('Hi')
  hi()
hello()
     


# Function calling anither Function - Callback
def add(a,b):
  return a + b

def show():
  res = add(12,22)
  print(res)

show()

     

a = lambda p : p*p
print(a(12))

add = lambda a,b : a+b
print(add(23,32))
     


     

#HOF - Higer Order Functions - jo functions se parameters leta and ek pura function return karke deta hai.
def hello():
  print('Hello')

def execute(func):
  func()

execute(hello)
     


# Callback Functions - ek function ko dusre function ke arguments ke roop main bhejna taki dusra function jarurat padne par usko call kar sake.
def add():
  print(10+20)
def sub():
  print(12-1)
def calculate(operation):
  print('Calculation Started')
  operation()

calculate(add)
calculate(sub)
     



     

# map = iterable object ke harek element par specific function apply karo and aage badho
n = [1,2,3,4,5]
def double(a):
  return a*a

res = map(double,n)
print(list(res))

result = map(lambda x: x*x,n)
print(list(result))
     
