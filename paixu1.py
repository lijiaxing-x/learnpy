#排2min 10业务task 周期t为20ms 50ms 100ms 200ms 500ms 优先级lp
#先排1s 2000 slot 100ms周期
#同一slot里的同一时刻也是可以并发业务的，基站给到slot的资源，分配到终端，怎么使用是终端行为
#循环0-40获得第一个包的时间 for每个  输出站位表：每个slot里的带宽 终端 占满否


num = 2000
slot = []
s1 = 4
s2 = 8
s3 = 9
a = int(num / 10)
for b in range(0, a):
    slot1 = s1 + 10*b
    slot2 = s2 + 10*b
    slot3 = s3 + 10*b

    if slot1 <= num:
        b += 1
    else:
        break
    slot += [slot1, slot2, slot3]
         
print('1s内上行时隙号：\n', slot, '\n1s内上行时隙共有：', len(slot))
time_s = []
for i in slot:
    t = 0.5 * i 
    time_s.append(t)  

print('1s内上行时隙时刻：\n', time_s)
#将slot和时间对应起来然后将任务排进dict，计算时间差 错峰 
#将任务的时间反过来对应slot号
t = [20, 50, 100, 200, 500]
na = int(20 / 0.5)
nb = int(50 / 0.5)
nc = int(100 / 0.5)
nd = int(200 / 0.5)
ne = int(500 / 0.5)
print('五类任务的周期间隔slot数',na, nb, nc, nd, ne)
#此时ne的间隔发送时间>2s


'''
①终端和业务都占不满网络，发送数据只需要排列优先级，将数据在同一时隙发送
'''

#业务输入
tasks = ['a', 'b', 'c', 'd', 'e']
#周期为t列表中的
lps = [3, 1, 4, 2, 5]
tl = zip(tasks, lps)
tsklp1 = list((task,lp) for task, lp in tl)
print('业务与优先级输入：',tsklp1)
#优先级lp排序
#tsklp = [('a', 3), ('b', 1), ('c', 4), ('d', 2), ('e', 5)]
tsklp1.sort(key=lambda x:x[1], reverse= True)
tsklp1_1 = []
for i in range(len(tsklp1)):
    tsklp1_1.append(tsklp1[i][0])


print('未达到网络资源满载，按照如下顺序在slot1发出：', tsklp1_1)
#同slot里业务发送时间，拍定时间发送
#列出业务占用时隙的列表  时隙错了，重新改一下
s1 = [2.0]
for a in s1:
    a += 40*0.5
    if a <= 2000:
        s1.append(a)
    else:
        break
s2=[2.0]
for a in s1:
    a += 100*0.5
    if a <= 2000:
        s2.append(a)
    else:
        break
s3=[2.0]
for a in s1:
    a += 200*0.5
    if a <= 2000:
        s3.append(a)
    else:
        break
s4=[2.0]
for a in s1:
    a += 400*0.5
    if a <= 2000:
        s4.append(a)
    else:
        break
s5=[2.0]
for a in s1:
    a += 1000*0.5
    if a <= 2000:
        s5.append(a)
    else:
        break
print('a业务发送时隙时刻：', s1,'\nb业务发送时隙时刻：', s2, '\nc业务发送时隙时刻：', s3, '\nd业务发送时隙时刻：', s4,'\ne业务发送时隙时刻：', s5)










