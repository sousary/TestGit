#use comprehesion
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# thislist.sort(reverse = True)

# print(thislist)

# course =['history', 'math','english','code']
# # num = [1,2,3,45,6]
# # sort=sorted(course)
# # print(sort)
# # print(sum(num))
# # for index, i in enumerate(course):
# #     print(index,i)
# course_str='  '.join(course)
# print(course_str)

#tuple: do not modify
# course =('history', 'math','english','code')
# class1 = course
# print(course)
# print(class1)
# course[0]='art'
# print(course)
# print(class1)

#set:do'n care about order and unmutible
# course ={'history', 'math','english','code'}
# class1 = course
# print(course)
# print(class1)


#unpacking list
numbers=[1,2,3,4,5,6,7,7,8,9]
first,second,*orther=numbers
print(first)
print(orther)
