'''
4.6
'''
#函数
#定义hello




def hello():
    print("hello world!")

hello()
#比较两个数，并返回大的
def max(a, b):
    if a > b:
        return a
    else:
        return b

a = 4
b = 5
print(max(a, b))
#计算面积函数
def area(width, height):
    return width * height

def print_welcome(name):
    print("welcome", name)

print_welcome("tracer")
w = 4
h = 5
print("width = ", w,"height = ", h,"area = ", area(w, h))
#函数调用
def printme(str):
    print(str)
    return

printme("我要调用用户自定义函数")
printme("再次调用同一函数")
#参数传递
a = [1, 2, 3]
a = "tracer"
#传不可变对象实例
#通过id()函数来查看内存地址变化
def change(a):
    print(id(a))
    a = 10
    print(id(a))

a = 1
print(id(a))
change(a)
#传可变对象实例
def changeme(mylist):
    #修改传入列表
    mylist.append([1, 2, 3, 4])
    print("函数内取值：", mylist)
    return
#调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值：", mylist)
#参数
#必须参数\关键字参数
def printme(str):
    print(str)
    return

printme("hh")
#不按指定顺序
def printinfo(name, age = 35):
    print("名字：", name)
    print("年龄：", age)
    return

printinfo(age=50, name="alice")
#默认参数
print("----------------------")
printinfo(name="bob")
#不定长参数
def printinf(arg1, *vartuple):
    print("输出：")
    print(arg1)
    print(vartuple)
   
printinf(70, 60, 50)

def printin(arg1, *vartuple):
    print("输出：")
    print(arg1)
    for var in vartuple:
        print(var)
    return

printin(10)
printin(70, 60, 50)

#**会以字典的形式导入
def printi(arg1, **vardict):
    print("output:")
    print(arg1)
    print(vardict)

printi(1, a=2,b=3)
#匿名函数Python 使用 lambda 来创建匿名函数。所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
x = lambda a: a+ 10
print(x(5))
#匿名设置俩参数
sum = lambda arg1, arg2: arg1 + arg2

print("和为：", sum(10, 20))
print("和为：", sum(20, 20))

def myfunc(n):
    return lambda a: a*n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#return语句
def sum1(arg1, arg2):
    tot = arg1 + arg2
    print("函数内：", tot)
    return tot

tot = sum1(10, 20)
print("函数外：", tot)

