#数据结构
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(1), a.count('x'))#计数
print(a.insert(2, -1))#insert指定位置插入元素-1为插入的元素 
a.append(333)#append 插在最后
a.index(333)#索引
a.remove(333)#删除值为x的第一个元素
a.reverse()
print(a)
a.sort()#排序
print(a)
#列表当堆栈使用
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()#移除指定位置元素，（）返回最后一个元素
print(stack)
#列表当作列队使用
from collections import deque
queue = deque(["eric", "john", "michael"])
queue.append("jerry")
queue.append("tom")
queue.popleft()
print(queue)
#列表推导式 逐个元素调用
vec = [2, 4, 6]
c = [3*x for x in vec]
print(c)
d = [[x, x**2] for x in vec]
print(d)
freshfruit = [' banana', ' blueberry', ' strawberry']
e = [weapon.strip() for weapon in freshfruit]# 逐个调用
print(e)

f = [3*x for x in vec if x > 3]
print(f)
f = [3*x for x in vec if x <= 1]
print(f)
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
f = [x*y for x in vec1 for y in vec2]
print(f)
#使用复杂表达式或嵌套函数
f = [str(round(355/113, i)) for i in range(1, 6)]
print(f)

