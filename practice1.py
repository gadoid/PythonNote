#! coding=utf-8
value = input("输入华氏度:")
try :
    value = int(value)
except TypeError :
    print("请输入数值")
s_value = (value-32)/1.8
print(f"华氏度{value}转换为摄氏度为%.2f"%(s_value))

import math
from typing import Type
value = input("输入半径：")
try :
    value = int(value)
except TypeError :
    print("请输入数值")
radius = math.pi*2*value
print("周长为%.2f"%(radius))
area = math.pi*2*value**2
print("面积为%.2f"%(area))

value = input ("输入年份：")
try :
    value = int(value)
except TypeError:
    print("请输入数值")
# if value%400==0 :
#     print("是闰年")
# elif value%4==0 and value%100!=0:
#     print("是闰年")
# else :
#     print("不是闰年")

if value%400==0 or value%100!=0 and value%4==0:
    print("是闰年")