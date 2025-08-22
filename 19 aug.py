from functools import reduce
print(reduce(lambda a,b:b if b>a else a,[1,2,3,4,-3,5,6,7]))
# print(reduce(lambda a,b:b if b<a else a[1,2,3,4,-3,5,6,7]))

#fibonacci
num1,num2=0,1
n=10
# for i in range(n):
#     print(num1)
#     third_num=num1+num2
#     num1=num2
#     num2=third_num

# for i in range(n):
#     print(num1)
#     num1,num2=num2,num1+num2 #another way to write fibonacci

# for i in range(n):
#     print(num1)
#     num1=num2
#     num2=num1+num2 #it is not correct way to print fibonacci as values are changing.

