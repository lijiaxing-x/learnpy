#python条件控制
import numbers


var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)
var2 = 0
if var2:
    print("2 - if 表达式条件为true")
    print(var2)
print("bye!")
#计算狗的年龄
age = int(input("请输入你家狗狗的年龄： "))
print("")
if age <= 0:
    print("false")
elif age == 1:
    print("14岁的人")
elif age == 2:
    print("22岁的人")
elif age > 2:
    hum = 22 + (age - 2)*5
    print("对应人的年龄：", hum)
input("press enter continue")
#if 常用操作运算符
print(5 == 6)
x = 5
y = 8
print(x != y)
#数字的比较运算
num = 7
guess = -1
print("puzzle!")
while guess != num:
    guess = int(input("请输入你猜的数字："))

    if guess == num:
        print("congratulions")
    elif guess < num:
        print("猜小了")
    elif guess > num:
        print("猜大了")
#if 嵌套
number = int(input("输入一个数字："))
if number % 2 == 0:
    if number % 3 == 0:
        print("此数可被2和3整除")
    else:
        print("别算了")
else:
    if number % 3 == 0:
        print("整除3")
    else:
        print("蒜了")