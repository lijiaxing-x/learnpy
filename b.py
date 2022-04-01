from itertools import count
import sys

'''
4.1 迭代器与生成器
'''
#迭代器
list1 = [1, 2, 3, 4]
it = iter(list1)#创建迭代器对象
print(next(it))#输出迭代器的下一个元素
print(next(it))
#迭代器对象可以使用常规for语句遍历：
list2 = [1, 2, 3, 4]
it1 = iter(list2)
#for x in it1:
#    print(x, end=" ")


#while True:
    #try:
    #    print(next(it1))
    #except StopIteration:
    #    sys.exit()

#创建一个迭代器
class mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = mynumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))

#stopIteration
class mynumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            b = self.a
            self.a += 1
            return b
        else:
            raise StopIteration
        
myclass = mynumber()
myiter = iter(myclass)

for b in myiter:
    print(b)

#生成器 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)

while True:
    try:
        print(next(f), end = " ")
    except StopIteration:
        sys.exit()
