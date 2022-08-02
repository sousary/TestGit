"""mylist=['book','pen','bag']
mylist.append('cat')
mylist.remove('book')
del mylist[0]
doc=['gun','knight','home ','banana','chery']
doc[2:3]=['cow','dof']
print(doc)
mylist.insert(3,'buy')
for i in mylist:

    print(i)
import random  
for i in range(10,100):
    if(i%2==0):
        print(i)"""
"""       
name =input("Enter a name:")
def func(name):
   
    print(f"this is a {name}")
    
func(name)

def increment(num,by):
    return num+by
print(increment(2,by=1))"""
num=int(input("Enter a number:"))
def fizz(num):
    if(num%3==0 and num%5==0):
        print("fizzbuzz")
        
    elif(num%3==0):
        print("fizz")
    elif(num%5==0):
        print("buzz")
    else:
        print(num)
fizz(num)
    

      