#排2min 10业务task 周期t为20ms 50ms 100ms 200ms 500ms 优先级lp
#先排1s 2000 slot 100ms周期
#同一slot里的同一时刻也是可以并发业务的，基站给到slot的资源，分配到终端，怎么使用是终端行为

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
    slot += [slot1, slot2, slot3]
         
print('2s内上行时隙号：\n', slot, '2s内上行时隙共有：', len(slot))
    
#将slot和时间对应起来然后将任务排进dict，计算时间差 错峰 
#将任务的时间反过来对应slot
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
print('未达到网络资源满载，按照如下顺序在slot1发出：', tsklp1)
#同slot里业务发送时间，拍定时间发送
#列出业务占用时隙的列表


'''
②终端多于8个，但业务数据量不超过时隙负载
'''
#优先级排序
#最大承载终端数tps，优先级lps， 
tps = 8
tasks = ['a', 'b', 'c','d','e','f','g', 'h', 'i', 'j', 'k']
lps = [3, 1, 4, 2, 5, 3, 1, 4, 2, 5, 3]
tt = zip(tasks,lps)
tsklp2 = list((task, lp) for task, lp in tt)
tsklp2.sort(key=lambda x:x[1], reverse= True)
#print(tsklp2)
#切割list
def list_of_groups(init_list, children_list_len):
    list_of_groups = zip(*(iter(init_list),) *children_list_len)
    end_list = [list(i) for i in list_of_groups]
    count = len(init_list) % children_list_len
    end_list.append(init_list[-count:]) if count !=0 else end_list
    return end_list

tsklist = list_of_groups(tsklp2, tps)
print('终端超出时隙负载，slot1中发送任务：', tsklist[0], '\nslot2中发送任务：', tsklist[1])



'''
③终端少于8，但数据超过时隙负载，一个时隙发一项业务（×）一个时隙发n个业务，可以并发
'''







