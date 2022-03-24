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
str = '1234567890'
#输出从第一位到倒数第二位
print(str[0:-1])
#输出第3-5个字符
print(str[2:5])
print(str[0:])
print(str[0:5])#区间就是左闭右开
print(str[1:5:2])#2为步长，左闭右开
print(str * 2)#输出两次
print(str + '\n你好')
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
str = '2abcd'
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
    
#tuple
