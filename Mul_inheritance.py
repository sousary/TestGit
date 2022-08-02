# class person:
#     def __init__(self,name):
#         self.name = name
#     def getName(self):
#         return self.name
#     def isEmployee(self):
#         return False
# class Employee(person):
#     def isEmployee(self):
#         return True
# name1=input("Enter your name:")
# name2=input("Enter your name:")
# emp=person(name1)
# print(f"This is your name : {emp.getName()}and you is :{emp.isEmployee()}")

# emp1=Employee(name2)
# print(emp1.getName(),emp1.isEmployee())
############# Inheritance
# class Base1:
#     def __init__(self):
#         self.str1="dara"
#         print("base1")
# class Base2:
#     def __init__(self):
#         self.str2="bakk"
#         print("Base2")
# class Derrive(Base1,Base2):
#     def __init__(self):
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("derrive")
#     def printstr(self):
#         print(self.str1,self.str2)
# ob=Derrive()
# ob.printstr()
        
class Base(object):
  
    # Constructor
    def __init__(self, x):
        self.x = x    
  
class Derived(Base):
  
    # Constructor
    def __init__(self, x, y):
          
        ''' In Python 3.x, "super().__init__(name)"
            also works''' 
        super(Derived, self).__init__(x)
        self.y = y
  
    def printXY(self):
  
       # Note that Base.x won't work here
       # because super() is used in constructor
       print(self.x, self.y)
  
  
# Driver Code
d = Derived(10, 20)
d.printXY()