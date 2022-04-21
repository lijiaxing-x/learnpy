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
#print(tsklist)
tsklp2_1 = []
for i in range(len(tsklp2)):
    tsklp2_1.append(tsklp2[i][0])
#print(tsklp2_1)
#print('终端超出时隙负载，slot1中发送任务：', tsklist[0], 'slot2中发送任务：', tsklist[1])
print('\n终端超出时隙负载，slot1中发送任务：', tsklp2_1[0:8], 'slot2中发送任务：', tsklp2_1[8:12])



'''
③终端少于8，但数据超过时隙负载，一个时隙发一项业务（×）一个时隙发n个业务，可以并发
'''