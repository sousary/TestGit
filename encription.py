
#encription
import random
message=input("Enter a message:")
alpha="abcdefghijklmnopqrstuvwxyz"
key=random.randrange(1,100)
encript=""
decript=""
for i in message:
    position = alpha.find(i)
    newposition = (position+key)%26
    encript+=alpha[newposition]
#write into file
file=open("../python.txt","w")
file.write(encript)
file.close()
#read from file
file1=open("../python.txt","r")
print(file1.readable())

for i in file1:
    #decript from file
    for j in i:
        pos = alpha.find(j)
        newpos = (pos - key)%26
        decript+=alpha[newpos]

print(decript)





