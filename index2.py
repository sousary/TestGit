"""x=5
y=20
def func():
    if x>y:
        print(x,"is bigger than ",y)
    if y>x:
        print(y,"is bigger thanx",x)

func()

def home(name,location):
    
    print("welcome come to "+name+" "+"in"+location)
    
name =input('input name:')
location =input('input location:')   
home(name,location)"""

#if else
"""a=int(input("enter a:"))
b=int(input("enter b:"))
def func(a,b):
    return a*b
if func(a,b)>10:
    print("sum is god")
    
elif func(a,b)<10:
    print("sum is normal")
else:
    print("none of above")
print(func(a,b))"""
#check number
"""num=int(input("Enter a number:"))
if num%2==0:
    print("it even number")
elif num%2 !=0:
    print("it odd number")
else:
    print('it none of above')"""

"""my_doc={
    'name':"hen",
    "age" : 12,
    "location": "califonia"
    
    
    
}
print(type(my_doc["age"]))
#loop

i=1
while i<=10 :
    print(i)
    i +=1"""
#loop for
"""fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
for y in range(2,6,2):
    print(y)"""
    
#list
"""
lists =[
    [1,2,3],[4,5,6],[8,9,10]
]
for list1 in lists:
    for row in list1:
        print(row)"""
        
#lambda
"""def func(n):
    return lambda a: (a*n)+(n/a)
cal=func(10)
cax=func(20)
print(int(cal(2)))
print("result of cax iS:\n",int(cax(2)))  """

#array 
"""
bike=["honda","yamaha","bmw","suzuki"]
bike.append("sym")
bike.pop(0)
for i in bike:
    print(i)

x=len(bike)
print(x)
"""
num1=int(input("Enter  number1:"))
num2=int(input("Enter a number2:"))
op = input("Enter a operator:")
print("answer is:\n")
if(op == "+"):
    print(num1+num2)
elif(op=="*"):
    print(num1*num2)
elif(op == "pow"):
    print(pow(num1,num2))
else:
    print(num1-num2)








