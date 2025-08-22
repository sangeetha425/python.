 #def connect_to_db(**args):
#     print(args)
# connect_to_db(db_loc="localhost:3000",db_pool="2345",db_port="3300",db_password="2240")

# def connect_to_db2(*args):
#     print(args)
# connect_to_db2('localhost:3000','2345','3300','2240')

# def even_or_odd(a):
#     return(a%2==0)
# result=even_or_odd(a)
# print(result)

# def even_or_odd(a):
#     if a%2==0:
#         return 'even'
#     else:
#         return 'odd'
# r1= even_or_odd(3)
# print(r1)

# def even_or_odd(a):
#     if a%2==0:
#         return 'even'
#     else:
#         return 'odd'
# r1=even_or_odd(4)
# r2=even_or_odd(5)
# print(r1)
# print(r2)

# def function(a):
#     for i in range(1,a):
#         print(i)
#         if i==9:
#             return
# r1=function(3)
# print(r1)

# num1=int(input('enter a value'))
# for i in range(1,21):
#     print(num1,'x',i,'=',num1*i)

# def function(n):
#     result=1
#     for i in range(1,n+1):
#         result=result*i
#         print(result)
# function(6)

def function(n):
    result=0
    for i in range(1,n+1):
        result=result+i
        print(result)
function(8)


