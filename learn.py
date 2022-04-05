from ast import Str
from doctest import ELLIPSIS_MARKER
import sys
'''
3.18 1st dae
'''
print("hola")
#wo xie lai play play
'''
BUZZ & WOODY are best friends
'''
if True:
    print("1st")
    print("BUZZ LIGHTYEAR")
else:
    print("answer")
    print("false")
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
    item_two + \
        item_three
if total == 6:
    print("WOODY")
else:
        print("hh")
days = ['SUN','MON','TUE',
'WED','THUR']
print(days[2])

#input("按下ENTER退出，其他键显示。。。\n")

#创建类
'''
3.21 class classname:
    class_suite 
'''
class employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", salary: ", self.salary)
'''
3.22 创建 Employee第一个对象,访问属性
'''
emp1 = employee("Woody", 10)
emp2 = employee("BUZZ", 20)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % employee.empCount)

emp1.age = 7
emp1.age = 8
#del emp1.age
print(hasattr(emp1, 'age'))#has attribute
print(getattr(emp1,'age'))
setattr(emp1,'age', 10)
print(emp1.age)
print("Employee._doc_:",employee.__doc__)
print("employee._name_:",employee.__name__)
print("employee._module_:",employee.__module__)
print("employee._bases_:",employee.__bases__)
print("employee._dict_:",employee.__dict__)
'''
3.23 数字类型四种：int bool float complex
'''
#字符串
str1 = '1234567890'
#输出从第一位到倒数第二位
print(str1[0:-1])
#输出第3-5个字符
print(str1[2:5])
print(str1[0:])
print(str1[0:5])#区间就是左闭右开
print(str1[1:5:2])#2为步长，左闭右开
print(str1 * 2)#输出两次
print(str1 + '\n你好')
print(r'hola\nchao')#r表示原始字符串
print('------------\n------')

x = 'hahaa'
y = sys.stdout.write(x + '\n')
print(y)#输出字符和字符数
x = '111'
z = '233'
#不换行 end=" "

print( x, end=" ")
print( z, end=" ")

print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n python path is',sys.path)

'''
3.24 基本数据类型
'''
counter = 100 #整型
miles = 1000.0 #浮点型
name = "Tracer" #字符
a = counter + miles
print(a)
#多个变量赋值
a = b = c = 1
print(a, b, c)
a, b, c = 1, 2, 'Tracer'
print(a, b, c)
#标准数据类型 number string tuple不可变数据, list set dictionary可变数据;不可变数据类型:数据类型对应变量的值发生了改变,对应的内存地址发生改变 可变数据类型:数据类型对应变量的值发生了改变,对应的内存地址不发生改变 所以说,可不可变是针对内存里存放的内容是否可变而言的.
#number  int/float/bool/complex
a, b, c, d = 20, 5.5, True, 2+3j
print(type(a), type(b), type(c), type(d))
a = 111
b = isinstance(a, int)
c = isinstance(b, int)#bool是int的子类
d = isinstance(b, bool)
e = isinstance(c, complex)
print(b)
print(c)
print(d)
print(e)
print(a + c)#bool:true == 1; false == 0
print(a + e)
var1 = 1
var2 = 10
del var1, var2
#print(var1)
#数值运算(在混合计算时，Python会把整型转换成为浮点数)
a = 5 + 4
b = 4.2 - 2
c = 3 * 7
d = 2 / 4 #0.5 float
e = 2 // 4 #2 int
f = 17 % 3 #取余
g = 2 ** 5 #2的5次幂
#list
list = [ 'abcd', 786, 2.23, '85tracer', 70]
str1 = '2abcd'
tinylist = [123, '85tracer']
print(str)
#print(list)
list[0] = 'ab'
#str[0] = 'a'#str不能更改
#print(list[0])
#print(str)
#print(tinylist * 2)
#print(list + tinylist)

a = [1, 2, 3, 4, 5, 6]
a[0] = 0
print(a[0])

def reversewords(input):
    inputwords = input.split(" ")
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputwords = inputwords[-1::-1]
    output = ' '.join(inputwords)
    return output

if __name__ == "__main__":
    input = '屎 吃 可以 小狗'
    rw = reversewords(input)
    print(rw)
'''
3.25 tuple set dict 数据类型转换
'''    
#tuple 元素不可改变
tuple1 = ('abcd', 678, 2.23, 'tracer', 70.2)
tinytuple = (123, 'haha')
print(tuple1)
print(tuple1[0])
print(tuple1[1:3])
print(tuple1[2:])
print(tuple1*2)
print(tuple1 + tinytuple)
#set
sites = {'google', 'taobao', 'runoob', 'facebook', 'zhihu', 'baidu'}
print(sites)

if 'runoob' in sites :
    print('runoob在集合里')
else :
    print('没有')

a = set('abcdefghijk')
b = set('abcdezxy')
print(a - b) #差集
print(a | b) #并集
print(a & b) #交集
print(a ^ b) #ab中不同时存在的元素 交补
#dictionary
dict = {}
dict['one'] = "1 - 小狗"
dict[2] = "2 - 可以"

tinydict = {'name': 'runoob', 'code':1, 'site': 'www.runoob.com'}
print(dict['one'])
print(dict[2])
print(tinydict.keys())
print(tinydict.values())
#数据类型转换
#隐式类型转换
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo", type(num_flo))

print("value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

#显式转换
x = int(1)
y = int(2.8)
z = int("3")
print(x, y, z)

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x, y, z, w)

x = str("s1")
y = str(2)
z = str(3.0)
print(x, y, z)

num_int = 123
num_str = "456"
print("num_int 数据类型为：", type(num_int))
print("before，num_str数据类型为：", type(num_str))
num_str = int(num_str)
print("after，num_str数据类型为：", type(num_str))

num_sum = num_int + num_str
print("合计", num_sum, "数据类型为", type(num_sum))

'''
3.28
'''
#推导式
#list推导式
names = ['woody', 'buzz', 'tracy', 'alien', 'losto', 'belle']
new_names = [name.upper() for name in names if len(name)>3]
print(new_names)
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
#dict推导式 将列表中的各字符串值为键，各字符串长度为值，组成键值对 [out_exp_res for out_exp in input_list if condition]
listdemo = ['Google', 'runoob', 'taobao']
newdict = {key:len(key) for key in listdemo}
print(newdict)
#提供三个字数字，以三个数字为键，三个数字的平方值来创建字典 { key_expr: value_expr for value in collection if condition }
dic = {x:x**2 for x in (1, 2, 3)}
print(dic, type(dic))
#set推导式 { expression for item in Sequence if conditional }
#计算1，2，3的平方数
setnew = {i**2 for i in (1,2,3)}
print(setnew)
#判断不是abc的字母并输出
a = {x for x in 'acdcbdecxyz' if x not in 'abc'}
print(a, type(a))
#tuple推导式 (expression for item in Sequence if conditional )
a11 = (x for x in range(1,10))
print(type(a11))#返回生成器对象
b11 = tuple(a11)
print(b11)
#python解释器\注释\运算符
#pyhton3编程第一步
#写一个斐波那契数列
a, b = 0, 1
while b < 10:
    print(b)
    a, b =b, a + b
while b < 1000:
    print(b, end=' ')
    a, b = b, a+b







