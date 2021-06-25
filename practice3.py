# int_number=int(input("输入一个整数："))
# for i in range (int_number-1,0,-1):
#     if int_number%i ==0 and i!=1 :
#         print(f"{int_number}不是一个素数")
#         break
#     elif int_number%i ==0 and i==1 :
#         print(f"{int_number}是一个素数")

# while True:
#     number1,number2=input("输入两个数字:").split(",")
#     number1=int(number1)
#     number2=int(number2)
#     tl=(number1,number2) if number1>number2 else (number2,number1)
#     print(tl)
#     n = tl[0]//tl[1]
#     n = n if n > tl[1] else tl[1]
#     while n>0:
#         if tl[0]%n==0 and tl[1]%n==0 :
#             print(f"最大公约数为{n}")
#             break
#         else :
#             n-=1

for i in range (1,6):
    print("*"*i+"\n")
for i in range (5,0,-1):
    print("*"*i+"\n")
while True:
    ss=int(input("行数"))
    n = ss//2+1
    m=1
    while n>=0:
        print(" "*n+"*"*m)
        m+=2
        n-=1