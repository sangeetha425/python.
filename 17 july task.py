a=int(input('enter a value'))
if a>0:
    print("Given value is positive")
else:
    if a==0:
     print("Given value is Zero")
    else:
      print("Given value is Negative") 

a=int(input('enter a value'))
if (a%2==0):
    print("given value is even")
else:
    print("given value is odd")

age=int(input('enter age'))
if age>=18:
    print('eligible to vote')
else:
    print('not eligibe to vote')

a=int(input('enter year'))
if (a%4==0):
    print("year is leap year")
else:
    print("year is not leap year")

a=int(input('enter a value'))
b=int(input('enter a value'))
if a>b:
    print("a is greater than b")
if a<b:
    print("b is greater than a")

a=int(input('enter a value'))
b=int(input('enter a value'))
if a>b:
    print("a is greater than b")
else:
    print("b greater than a")

#MEDIUM LEVEL
a=int(input('enter marks'))
if a>=90 and a<=100:
    print("Grade A")
elif a<=89 and a>=75:
    print("Grade B")
elif a>=60 and a<=74:
    print("Grade C")
elif a>=40 and a<=59:
    print("Grade D")
elif a<=40 and a>=0:
    print("Fail")
else:
    print("Invalid marks")
