#排2min 10业务task 周期t为20ms 50ms 100ms 200ms 500ms 优先级lp
#先排1s 2000 slot 100ms周期


n = 2000
slot = []
s1 = 4
s2 = 8
s3 = 9
'''
for slot in range(len(slots)):
    for b in range(0,3):
        slots[slot] += 10*b
        print(slots)
        if slot <= 2000:
            b += 1
            
        else:
            break
        list1.append(slot)

print(list1)
''' 
a = int(n / 10)
for b in range(0, a):
    slot1 = s1 + 10*b
    slot2 = s2 + 10*b
    slot3 = s3 + 10*b

    if slot1 <= n:
        b += 1
    else:
        break
    slot.append(slot1)
    slot.append(slot2)
    slot.append(slot3)
          
print(slot, '2s内上行时隙共有：', len(slot))
    
#将slot和时间对应起来然后将任务排进dict，计算时间差 错峰 
#将任务的时间反过来对应slot
t = [20, 50, 100, 200, 500]
na = int(20 / 0.5)
nb = int(50 / 0.5)
nc = int(100 / 0.5)
nd = int(200 / 0.5)
ne = int(500 / 0.5)
print('五个任务的周期间隔slot数',na, nb, nc, nd, ne)
#此时ne的间隔发送时间>2s
#①终端和业务都占不满网络，发送数据只需要排列优先级，将数据在同一时隙发送
#业务输入
tasks = ['a', 'b', 'c', 'd', 'e']
lps = [3, 1, 4, 2, 5]
tl = zip(tasks, lps)
tsklp1 = list((task,lp) for task, lp in tl)
print('业务与优先级输入：',tsklp1)
#优先级排序
#tsklp = [('a', 3), ('b', 1), ('c', 4), ('d', 2), ('e', 5)]
tsklp1.sort(key=lambda x:x[1], reverse= True)
print('可按照如下顺序在slot1发出：', tsklp1)

#②终端多于8个，但业务数据量不超过时隙负载
#优先级排序
tasks = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1','d','e','f','g', 'h', 'k']
lps = [3, 1, 4, 2, 5,3, 1, 4, 2, 5,3, 1, 4]
tt = zip(tasks,lps)
tsklp2 = list((task, lp) for task, lp in tt)
tsklp2.sort(key=lambda x:x[1], reverse= True)
print(tsklp2)

#③终端少于8，但数据超过时隙负载，一个时隙发一项业务（×）一个时隙发n个业务，可以并发
#同一slot里的同一时刻也是可以并发业务的，基站给到slot的资源，分配到终端，怎么使用是终端行为







