# num1=10
# def check_function():
#     global num1
#     num1=20
#     print(num1)
# check_function()
# print(num1) reassigning the value to global variable in the function using global keyword.

# num1=10
# def check_function():
#     num1=20
#     globals()['num1']=30
#     print(num1)
# check_function()
# print(num1) reassigning the value to global variable in the function using global function.

# num1=10
# def check_scope():
#     num1=20
#     print(num1)
# check_scope()
# print(num1) #global shadowing

def table_printer(n):
    for i in range(1,n+1):
        print(n,'x',i,'=',n*i)

table_printer(10)
