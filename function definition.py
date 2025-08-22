#positional arguments- based on the position of parameter ,arguments can be passed.

# def function(a,b):
#     print(a,b)

# function(10,20) 

# #keyword arguments-keyword arguments are written by specifying the parameter names in the function call.

# def function(a,b):
#     print(a,b)

# function(a=10,b=20)

# #default arguments-default arguments can be declared in parameter.

# def function(a=10,b=20):
#     print(a,b)

# function(20,40) #here 20 and 40 are arguments acts as positional arguments and if we dont pass any arguments default values can be printed.

#Method overloading

def sum(a,b):
    print(a,b)

def sum(a,b,c):
    print(a,b,c)

def sum(a,b,c,d):
    print(a,b,c,d)

sum(1,3)
sum(1,2,3)
sum(1,2,3,4)  #here single function (or)same function name cannot access different parameters.

#Arbitrary arguments(*args)
def function(a,*b): # *b is now an arbitrary parameter which allows n number of arguments.
    print(a)#10
    print(b)#here b prints as tuple (20,30,40,50,60)

function(10,20,30,40,50,60)

#Arthemetic operation using arbitrary argument
# def sum(a,*b):
#     print(a+b) it is not correct way to perform addition here it only print values not sum

def sum(a,*b): #arbitrary argument take values in tuple format.
    temp=a
    for i in b:
        temp=temp+i
        print(temp) 

sum(1,2,3,4,5,6,7,8,9)

#keyword arbitrary argument.(**kargs)
#**kargs print as dictionary format.

def connect_to_db(**kargs):
    print(kargs)

connect_to_db(db_loc='local_host=3000',db_pool='2345',db_port='7625',db_password='6312')
