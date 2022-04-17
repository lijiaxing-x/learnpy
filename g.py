'''
4.13 模块
'''
import sys
from unittest import result
import support
from fibo import fib, fib2


print('命令行参数：')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')
#import语句
support.print_func('tracer')
print(sys.path)
#斐波那契
import fibo
a = fibo.fib(1000)
fib(500)
#__name__属性
if __name__== '__main__':
    print('程序自身在运行')
else:
    print('我来自另一个模块')
#dir()函数
print(dir(fibo))
print(dir(sys))
#标准模块
#sys.ps1
#sys.ps2
'''
4.17 文件读取
'''
#输出格式美化
s = 'hola, tracer'
print(str(s))
repr(s)

import math

print('PI is: %5.3f'%math.pi)
#读取键盘输入
str1 = input("请输入：")
print("输入的内容是：", str1)

f = open("./milkt.txt","w")
f.write("我要一杯QQneinei好喝到咩噗茶\n你要不要听听看自己在说什么!\n")

f.close()

f = open("./milkt.txt", "r")

str1 = f.read()
print(str1)
f.close()
f = open("./milkt.txt", "r")
str1 = f.readline()
print(str1)
str2 = f.readlines()
print(str2)
f.close
#迭代读取
f = open("./milkt.txt", "r")

for line in f:
    print(line, end='')

f.close
#f.write
f = open("./milkt.txt", "w")

num = f.write("我们店的正常是别家店的半糖。\n珍奶正常去冰。\n")
print(num)
f.close

f = open("./milkt.txt", "w")
val = ('www.baidu.com', 14)
s = str(val)
f.write(s)
f.close
#f.seek(5)

#pickle模块 pickle.dump(obj, file, [,protocol])
import pickle

data1 = {'a':[1, 2.0, 3, 4+6j],
'b':('string', u'Unicode string'),
'c':None
}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

out = open('data.pk1','wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, out)
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, out, -1)

out.close




