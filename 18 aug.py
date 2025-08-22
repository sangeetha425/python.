# def square(x):
#     return x**2


# print(list(map(square,[1,2,3,4,5,6,7,8,9])))

# # print(list(map(square,[11,22,33,44,55,66,77,88,99])))

# def check_even(x):
#     return x%2==0

# print(list(map(check_even,[1,2,3,4,5,6,7,8,9])))

# example=lambda a,b:a+b
# print(example(4,5))
# example=50
# print(example(4,5))

# def square(x):
#     return x**2

# print(list(map(lambda x:x**2,[1,2,3,4,5,6,7,8,9])))

#lambda function.
#Anonymous one line function in python are called Lambda function. 
# example_function=lambda a,b:a+b
# print(example_function(4,5)) #performs sum

# lam1=lambda a:a**2
# print(lam1(9)) #performs square of a number

# map ,filter - these are in-built higher order functions.
#map - applies a function to every element in a sequence.
# print(list(map(lambda a:a**2 ,[2,3,4,5,6,7,8])))
# print(list(map(lambda a:a+2,[2,3,4,5,6,7,8])))

#filter - picks only the elements that pass a condition.
#print(tuple(filter(lambda x:x%2==0,[22,33,44,55,66,77,88,99])))

#reduce -

# from functools import reduce
# print(reduce(lambda a,b:a+b,[1,2,3,4,5,6,7,8]))