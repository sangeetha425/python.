# a=int(input('enter a value'))
# b=int(input('enter a value'))
# if a>b:
#     print('a is bigger')
# if b>a:
#     print('b is bigger')

# a=int(input('enter a value'))
# b=int(input('enter a value'))
# if a>b:
#     print('a is bigger')
# else:
#     print('b is bigger')

# a=int(input('enter a value'))
# b=int(input('enter a value'))
# c=int(input('enter a value'))
# if a>b:
#     print('a is bigger')
# else:
#     if a>c:
#         print('a is bigger')
#     else:
#         if b>c:
#             print('b is bigger')
#         else:
#             print('c is bigger')

# a=int(input('enter a value'))
# if a%2==0:
#     print('even number')
# else:
#     print('odd number')

# num1=10
# start=1
# while start<21:
#     print(num1,'x',start,'=',num1*start)
#     start+=1

# db_password='sangeetha'
# db_username='sangeetha_ramreddy'
# remaining_attempts=3
# while remaining_attempts>0:
#     entered_username=input('enter username')
#     entered_password=input('enter password')
#     if db_username==entered_username and db_password==entered_password:
#         print('login succesful')
#         break
#     else:
#         remaining_attempts -=1
#         print('login failed','you still have',remaining_attempts,'attempts' )
#         if remaining_attempts==0:
#          print('try after 24 hours') need practice for this.

# db_password='sangeetha'
# db_username='sangeetha_ramreddy'
# remaining_attempts=3
# while remaining_attempts>0:
#     entered_username=input('enter username')
#     entered_password=input('enter password')
#     if db_username==entered_username and db_password==entered_password:
#         print('login succesful')
#         break
#     else:
#         remaining_attempts -=1
#         print('login failed','you still have',remaining_attempts,'attempts' )
#         if remaining_attempts==0:
#          print('try after 24 hours')

# 
# def check_num_status(num1):
#     if num1>0:
#         print('positive')
#     elif num1==0:
#         print('zero')
#     else:
#         print('negetive')
# num1=int(input('enter a value'))
# check_num_status(num1)

# def even_or_odd(a):
#     res='even' if a%2==0 else 'odd'
#     print(res)
# even_or_odd(2)

# def eligibility_to_vote(a):
#     res='eligible to vote' if a>=18 else 'not eligible'
#     print(res)
# a=int(input('enter age'))
# eligibility_to_vote(a)

# def greatest_of_two_numbers(a,b):
#     res='a is greater'if a>b else 'b is greater'
#     print(res)
# a=int(input('enter a value'))
# b=int(input('enter a value'))
# greatest_of_two_numbers(a,b)

# def greatest_numbers(a,b):
#     return a if a>b else b
# print(greatest_numbers(5,8)) returns a value

# a=int(input('enter value'))
# b=int(input('enter value'))
# ope=str(input('enter str'))
# if ope=='add':
#     print(a+b)
# elif ope=='subtract':
#     print(a-b)
# elif ope=='multiply':
#     print(a*b)
# elif ope=='division':
#     print(a/b)

# def simple_calculator(a,b,op):
#     if op=='+' or op=='ADD':
#         print(a+b)
#     elif op=='-' or op=='subtract':
#         print(a-b)
#     elif op=='*' or op=='multiply':
#         print(a*b)
#     elif op=='/' or op=='division':
#         print(a/b)
# a1=float(input('enter value'))
# b1=int(input('enter value '))
# ope=input('enter').lower() #convert uppercase letters into lower case
# print(ope)
# simple_calculator(a1,b1,ope)

# a=str(input('enter string'))
# print(a[::-1])

# a='sangeetha'
# count=0
# for i in str('sangeetha'):
#     count+=1
#     print(count)

# a=int(input('enter age'))
# if a>=18:
#     print('eligible to vote')
# else:
#     print('not eligible to vote')

# def add(num1,num2):
#     return num1+num2
# value=add(8,6)
# print(value)

# def addition(a,b):
#     return a+b
# a=int(input('enter'))
# b=int(input('enter'))
# result=addition(a,b)
# print(a+b)

# def addition(a,*b):
#     temp=a
#     for i in b:
#         temp += i
#         print(temp)
# addition(1,3,4,6,8,9,10)
    
# num1=int(input('enter a value'))
# count=0
# for i in range(1,num1+1):
#     num1%i==0
#     count += 1
# if count==2:
#     print('prime number')
# else:
#     print('not a prime number')

# num1=int(input('enter a value'))
# if num1<=1:
#     print('not a prime number')
# else:
#     flag=True
#     for i in range(2,num1):
#         if num1%i==0:
#             flag=False
#             print('not a prime number')
#             break
    
#     if flag ==True:
#         print('prime')

# def check_prime(in_num):
#  if in_num<=1:
#      return'not a prime'
#  for i in range(2,in_num):
#    if in_num%i==0:
#      return 'not a prime'
#  return 'prime'
# print (check_prime(20))