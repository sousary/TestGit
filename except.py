from new import Student

class Person(Student):
    pass
p1 = Person
print(p1.name)


"""while(1):
    try:
        x =int(input("Enter a number:"))
    
        print(x)
        
    except:
        print("try agnain!!!")
 """ 
#class and object methods
"""
class Person:
  def __init__(self, name, age,sex):
    self.name = name
    self.age = age
    self.sex = sex

  def myfunc(self):
    print("Hello my name is " +self.name+ " age: ",self.age)
    print("she is:",self.sex)

p1 = Person("John", 36,"f")
p1.age = 40

p1.myfunc() 
 """
