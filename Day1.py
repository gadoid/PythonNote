# int 整型 
# 可以用 int() 强制转换为整型
float_number=1.1
print(int(float_number))
str_info="a"

# 进制
# 0b 2进制 0o 八进制 默认十进制 0x 十六进制
result=0b101+0o17+10+0x1D
print(result)

# 对其
#5  右对齐5位
#-5 左对齐 5位
print("%5d"%(result),"aaa")
print("%-5d"%(result),"aaa")

#float 浮点型
#转换整型为浮点型
int_number=2
print(float(int_number))

# .+数字打印固定位数小数
print("%5.8f"%(int_number))

# 字符串型
# 由单、双引号括起来的任意文本
print("hello world")

#可以用Unicode 数值表示
a= u"Hello world"
print("\150\145\154\154\157\40\167\157\162\154\144")

#跨行输出 三个单/双 引号
print("""hello
        world""")

#字符串支持切片
hello = "hello world"
print(hello[:6])
print(hello[6:])

#布尔值 数值True\False 或其他可转换值

# 如0，1
print(bool(0),bool(1))

# 如非空、空
print(bool(" "),bool(None),bool(""))

# 运算式结果
print(bool(1>2),bool(1<2))

# 变量命名
# 支持的元素 大小写字母、数字、下划线 不能用数字开头
# 大小写敏感 不要和自带关键子冲突

# 驼峰命名法
def ApplePie():
    print("This is a apple pie")
ApplePie()
# 小驼峰命名法
def applePie():
    print("This is a apple pie")
applePie()

#PEP8
#  用小写字母拼写，多个单词用下划线连接
#  受保护的实例属性用单个下划线开头
#  私有的实例属性用两个下划线开头

# Python 变量声明
# Python_variable
Python_variable="variable"
print(Python_variable)

#Type函数检查变量类型
print(type(Python_variable))
Python_variable=1
print(type(Python_variable))

#变量运算
Python_int=8
Python_float=8.1
print(Python_float+Python_int)
Python_str="a"
try:
    print(Python_int+Python_str)
except TypeError:
    print("TypeError")

#强制转换函数
# float()
# str()
# chr()
# int()
# bool()
# ord()
print(ord("h"))
print(chr(0o150))

#变量传值
content="通过%+类型传递参数"
print("%s"%(content))
# 通过format函数
content="通过format函数"
#print("{content}".format())
#简化
print(f"{content}")
#直接使用变量连结
content="直接使用变量连接"
print("print"+content)

#运算符
# 切片,左闭右开[]
list1= [1,2,3,4,5] 
list2=list1
list3=list1[:]
print(id(list1),id(list2),id(list3))
import copy
list4=copy.deepcopy(list1)
print(id(list4))
#切片参数 [:,2,-1]
print(list1[-1::1])

#乘方
print(2**2)

print(-ord('h'))