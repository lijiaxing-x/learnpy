'''
3.31 循环语句
'''
# break 和 continue 语句及循环中的 else 子句
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print("循环结束")
#while中使用continue
a = 5
while a > 0:
    a -= 1
    if a == 2:
        continue
    print(a)
print("循环结束")
#例
for letter in 'tracers':
    if letter == 'r':
        continue
    print('当前字母：', letter)

var1 = 10
while var1 > 0:
    print('当前变量值：', var1)
    var1 -= 1
    if var1 == 5:
        break
print("bye!")
#查询质数的循环
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        print(n, ' 是质数')
#pass语句
'''while True:
    pass
#最小的类
class myemptyclass:
    pass
'''
for letter in 'tracer':
    if letter == "a":
        pass
        print('执行pass块')
    print('当前字母 ：', letter)
print("good bye!")



