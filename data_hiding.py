#data hiding
"""
class Myclass:
    __hiddingVariable=0
    def add(self,increment):
        self.__hiddingVariable +=increment
        print(self.__hiddingVariable)
obj=Myclass()
obj.add(2)
obj.add(5)
print(obj._Myclass__hiddingVariable)"""

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
  
    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)
  
    def __str__(self):
        return "From str method of Test: a is %s," \
              "b is %s" % (self.a, self.b)
  
# Driver Code        
t = Test(1234, 5678)
print(t) # This calls __str__()
print([t]) # This calls __repr__()

    
        
        