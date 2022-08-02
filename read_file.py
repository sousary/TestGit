"""file=open("../python.txt","r")
print(file.readable())

for i in file:
    print(i)
file.close()"""

file=open("../python.txt","a")

file.write("\nThis i write to line 2")

file.close()