'''
4.11 数据结构
'''
#嵌套列表解析
mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
m = [[row[i] for row in mat] for i in range(4)]#列表转换
print(m)
#另一种实现方式
transposed = []
for i in range(4):
    transposed_row = []
    for row in mat:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed_row)#????
'''
mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = []
for i in [0, 1, 2, 3]:
    # transposed_row 作初始化使用
    transposed_row = []
    # 此时i = 0,1,2,3
    # 根据对齐，需要先把下两行循环运行完毕
    # 再进入 i = 1的循环
    for row in mat:
        #此时row为[1, 2, 3, 4]
        transposed_row.append(row[i])
        # transposed_row 添加 row[0]，即1;
        # 第二次循环 row变为[5,6,7,8] row[0] 变为 5
        # 以此类推
    transposed.append(transposed_row)
    # 此时 transposed_row 为 [1,5,6]
    # 进入下一个 i = 1的循环

# 两个循环结束之后 再进入下两行
print(transposed_row)  # ????
print(transposed)
mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = []
for i in [0, 1, 2, 3]:
    # transposed_row 作初始化使用
    transposed_row = []
    # 此时i = 0,1,2,3
    # 根据对齐，需要先把下两行循环运行完毕
    # 再进入 i = 1的循环
    for row in mat:
        #此时row为[1, 2, 3, 4]
        transposed_row.append(row[i])
        # transposed_row 添加 row[0]，即1;
        # 第二次循环 row变为[5,6,7,8] row[0] 变为 5
        # 以此类推
    transposed.append(transposed_row)
    # 此时 transposed_row 为 [1,5,6]
    # 进入下一个 i = 1的循环

# 两个循环结束之后 再进入下两行
print(transposed_row)  # ????
print(transposed)
'''
print(transposed)
#del语句
a = [-1, 1, 66.25, 333, 333, 123.45]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
#元组和序列
t = 12345, 54321, 'hello!'
print(t[0])
u = t, (1, 2, 3, 4, 5)
print(u)
#集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
#字典
tel = {'jack':123, 'sape':456}
tel['guide'] = 789
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 890
print(tel)
print(list(tel.keys()))
a = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(a)
#遍历技巧
knights = {'gallahad':'the pure', 'robin':'the brave'}
for k, v in knights.items():
    print(k, v)
#enumerate 索引位置和对应值
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
#同时遍历两个或更多序列，用zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('what is ur {0}? it is {1}.'.format(q, a))
#反向遍历
for i in reversed(range(1, 10, 2)):
    print(i)
for f in sorted(set(basket)):
    print(f)
    

