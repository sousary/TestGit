"""class Cat:
    
        
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name 
    def get_age(self):
        return self.age 
    
c=Cat('dara',12)
print(c.get_age())
print(c.get_name())"""
class Student:
    def __init__(self, name, score, grade):
        self.name = name
        self.score = score
        self.grade = grade
    def get_name(self):
        return self.name
    def get_score(self):
        return self.score
    def get_grade(self):
        return self.grade
class Course:
    def __init__(self, name,max):
        self.name = name
        self.max = max
        self.student=[]
    def add_student(self,student):
        if len(self.student)< self.max:
            self.student.append(student)
            return True
        return False
    def get_grade(self):
        value=0
        for i in self.student:
            value+= i.get_grade()
        
        return value/len(self.student)
    
s1=Student("dara",55,12)
s2 = Student("bot",67,12) 
s3 = Student("botiq",66,12)  
course=Course("math",22)
course.add_student(s1)
print(course.add_student(s2))
print(course.get_grade())