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


