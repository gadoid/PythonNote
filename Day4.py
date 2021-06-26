# list1= []
# for i in range (1,100000):
#     i=str(i)
#     m=0
#     il=len(i)
#     for j in range (il):
#         o=int(i[j])**4
#         m+=o
#     if m==int(i):
#         list1.append(m)
    
# print(list1)

# for i in range (0,20) :
#     for j in range (0,33) :
#         if 5*i+3*j+(100-i-j)/3==100:
#             print(f"公鸡{i},母鸡{j},小鸡{100-i-j}")

# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

# def fibonacci(number):
#     if number<3 :
#         return number-1
#     return fibonacci(number-2)+fibonacci(number-1)

# n = int(input("number:" ))
# for i in range(1,n) :
#     print(fibonacci(i+1),end="")

def perfect():
    list1=[]
    for i in range (1,10000):
        m=i//2
        n=0
        while m>=1: 
            if i%m==0:
                n+=m
            m-=1
        if n==i:
            list1.append(n)
    print(list1)

perfect()