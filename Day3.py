#循环  for in 结构
for i in ("hello world") :
    print(i,end="")

def hw():
    n = 0
    while n < 10 :
        yield(n)
        n+=1
for i in hw() :
    print(i,end=" ")

# for ... in range 
for i in range (1,10):
    print(i,end=" ")
print("++++++++++")
for j in range (10,1,1):
    print(j,end=" ")

# while 循环
i = 0
while i < 10 :
    print(i)
    i+=1
else :
    print("end")


# break 中断当前循环
# continue 跳过本次循环的后续内容

