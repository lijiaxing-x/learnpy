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
c = sys.ps1
sys.ps2
print(c)




