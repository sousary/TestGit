# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for i in thisdict:
#     print(i)
    
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# mydict=thisdict.copy()
# print(mydict)
# thisdict.update({"year":2022})
# for i,j in thisdict.items():
#     print(i,j)
    
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
child4={
    "age":2022,
    "grade":12
}
myfamily.update(child4)
del child1
print(myfamily)       