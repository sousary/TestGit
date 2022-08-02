class Student():
    name= "Tim"
    age = "22"
    sex = "men"
    
class People(Student):
    degree= "master"
    location= "cambodia"
    
obj1=People()

print(obj1.name +" have age "+obj1.age)
print(obj1.sex +" have degree ",obj1.degree)
print(obj1.name +" have sex ",obj1.location)