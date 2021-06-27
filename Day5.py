# 函数的定义依靠 def(参数名): 声明一个参数
# 可以创建变量接受来自return的返回值
def voice():
    return "noise"
sound=voice()
print(sound)
# 通过不同的模块用以区分相同名称的函数
# 后续加载的模块会覆盖掉前一个加载模块相同函数名的功能
# mian方法，加载模块后，模块内可能有自身会执行的方法，通过使用main方法，来
# 只运行当前程序下的代码
print(__name__)
import time
from typing import Counter
print(time.__name__)

#作用域
# 变量在不同的模块下，的调用关系
#全局变量
global_variable="global_variable"
print(global_variable)
# #局部变量，声明在函数中
# local_Variable=0
# def change(local_Variable):
#     local_Variable="local_Variable"
#     # 通过global 关键字将变量声明为全局变量(全局需要有对应的变量名)
#     global local_Variable
# change(local_Variable)
# print(local_Variable)

#字符串处理
test_str=" hello,world   "
print(test_str.split(","))
print(test_str.strip())
print(test_str.lstrip())
print(test_str.rstrip())
print(test_str.index("world"))

# 字符串生成
str1=[i for i in range(10)]
print(str1.__str__())

# 列表处理
# 切片
list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
list1.remove(1)
list1.insert(3,3)
list1.sort()
print(list1)

#约瑟夫环问题
def jump(position,number):
    if len(number)>15 :
        position=position+8 if position+8<=len(number) else position+8-len(number)
        number.pop(position)
        print(number)
        return jump(position,number)
    return number

number=[i for i in range (1,31)]
print(jump(0,number))

# 面向对象，将所有内容都视作对象，改顺序操作为对对象执行操作。
#封装：通过内部函数获取、修改内部属性
#继承：继承来自父类的变量初始化、方法
#多态：调用同一个属性、或方法，返回不同的行为
class human():
    def __init__(self,name) -> None:
        self._name=name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,set_name):
        self._name=set_name

    def wei(self,someone_need_eat,things):
        print(f"{self._name}喂了{someone_need_eat.eat(things)}")

class dog():
    def __init__(self,name) -> None:
        self.eat_list=[]
        self._name=name
    def eat(self,things):
        self.eat_list.append(things)
        return f"{self._name}吃{things}"
        

class baba():
    def __init__(self,xing) -> None:
        self._xing = xing
    
    @property
    def xingshenme(self):
        return self._xing
    
    @xingshenme.setter
    def gaixing(self,xing):
        print(f"想姓{xing}，混账东西！")

class son(baba):
    def __init__(self, xing) -> None:
        super().__init__(xing)

    def gaixing(self,xing):
        self._name=xing
         
    


zs=human("张三")
zs.name="王二"
egz=dog("二狗子")
zs.wei(egz,"骨头")
b=baba("王")
s=son("王")
print(s.xingshenme)
print(s.gaixing("刘"))

import math
class position():
    def __init__(self,x,y) -> None:
        self._x=x
        self._y=y

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,get_x):
        self._x=get_x

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,get_y):
        self._y=get_y
    
    def __str__(self) -> str:
        return f"({self._x},{self._y})"
    
    def __repo__(self):
        return self.__str__()
    
    def move_to(self,item):
        x = item.x-self._x 
        if x > 0 :
            str1=f"向右移动{x}"
        else :
            str1=f"向左移动{-x}"
        y = item.y-self._y
        if y > 0 :
            str2=f"向上移动{y}"
        else :
            str2=f"向下移动{-y}"
        print(str1,str2)

    def distance(self,item):
        self._distance=math.sqrt((item.x-self._x)**2+(item.y-self._y)**2)
        print(f"到点{item}的距离为%.2f"%(self._distance))


a = position(2,2)
print(a)
b = position(4,4)
a.move_to(b)
b.move_to(a)
a.distance(b)

def Upper(function,*arg,**kwarges):
    def fun(*arg,**kwargs):
        print("welcome")
        function(*arg,**kwarges)
        print("good bye")
    return fun

@Upper
def hello(*arg,**kwargs):
    print(*arg)

hello("女孩")

#__slots_—— 限制对象只能绑定哪些属性

class class_method():
    counter=0
    def __new__(cls) :
        if counter==None:
            cls.counter=0
        else :
            cls.counter+=1
        return cls.counter
    def __init__(self) -> None:
        print(__dict__)
class_method() 
 
# 类与类之间的关系
# is a 继承
# has a 关联
# use a 依赖
