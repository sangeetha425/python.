# n=int(input("enter a number"))
# temp=n
# l=len(str(n))
# sum=0
# while temp>0:
#     rem=temp%10
#     sum+=rem**l
#     temp=temp//10
# if sum==n:
#     print("armstrong")
# else:
#     print("not armstrong")

# num1=int(input('enter number'))
# temp=num1
# sum=0
# while num1>0:
#     rem=num1%10
#     print(rem)
#     sum+=rem**3
#     num1=num1//10

# print(sum)
# if temp==sum:
#     print('armstrong number')
# else:
#     print('armsweak number')

num2=2463
count=0
while num2>0:
    digit=num2%10
    num2=num2//10
    count+=1

print(count)
