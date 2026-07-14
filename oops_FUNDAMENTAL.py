

'''
Object Oriented Programming :
Fundamental Concepts :
1. Class -
2. Object -
3. Encapsulation -
4. Instance Vairable -
5. Class variables
6. Methods
7. Self keyword -
8. Encapsulations
9. Data Hiding
10. Inheritance
11. Polymorphism - One name many forms - Father -
12. Abstraction - Data Hiding -
13. Access Modifires -
14. Method Overloading
15. Method Overriding -
16. static methods
17. MAgic (Dunder Method)

'''
     

class Student:
  pass
print(Student)
a = Student()
b = Student()
print(a)
print(b)
print(type(a))
print(type(b))
     


class School:
  def __init__(self):
    print('Object Created')

a = School()
b = School()

     


class Student:
  def __init__(self,name,age):
    self.name = name
    self.age = age

a = Student('Sant',40)
print(a.name)
print(a.age)
# self is the keyword that refers to the current object
# note - without self, python cant identify object's variable which we are refereing

     


class Student:
  def __init__(self,name):
    self.name = name
a = Student("Ram")
b = Student('Shyam')
print(a.name)
print(b.name)
# Instance Vairable - each variable that belongs to an object.
# here a,b are instance of class Student.
#Class variable - variables which are shared by all objects.

     

class School:
  school = "Unique Computers"
  name = 'someone'
  def __init__(self,name):
    self.name = name
a = School('Ram')
b = School('Shyam')
print(a.name)
print(b.name)
print(a.school)
print(b.school)
     


# Methods
class Student:
  def __init__(self,name):
    self.name = name
  def show(self):
    print('Hello, ',self.name)

a = Student('Sant')
a.show()
     


class Bank:
  def __init__(self):
    self.__bal = 10000
  def deposit(self,amt):
    self.__bal+=amt
  def withdrawl(self,amt):
    self.__bal -= amt
  def showbal(self):
    print(self.__bal)

a = Bank()
a.deposit(1000)
a.withdrawl(500)
a.showbal()

     


# inheritance
class A:
  def hello(self):
    print('I am Base Class')
class B(A):
  def bye(self):
    print('Bye')

p = B()
p.hello()
p.bye()
     



class Dadaji:
  def land(self):
    print('Land for All')
class Father(Dadaji):
  def house(self):
    print('House made by Father')
class Son(Father):
  def car(self):
    print('Car')

a = Son()
a.land()
a.house()
a.car()
     


# polymorphis

class A:
  def hello(self):
    print('Base Class is SAying Hello')
class B:
  def hello(self):
    print('Child Class is Saying Bye')

data = [A(),B()]
for i in data:
  i.hello()
     

class A:
  def hello(self):
    print('Base class is SAying Hello')

class B(A):
  def hello(self):
    super().hello()
    print('Derived class is also Saying Hello')

obj = B()
obj.hello()
# obj = A()
# obj.hello()
     


# abstraction - hide implementations and show only functionality

     

# Access Modifires :
'''
  public:
    self.name
  private
    self.__name
  protected:
    self._name

'''
     