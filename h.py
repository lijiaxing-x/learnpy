#排2min 10业务task 周期t为20ms 50ms 100ms 200ms 500ms 优先级lp
#①先排1s 2000 slot 100ms周期



n = 2000
task = ['a', 'b', 'c', 'd', 'e']
lp = [1, 1, 1, 2, 2]
t = [20, 50, 100, 200, 500]

list1 = []
slots = [4, 8, 9]
s = 4

for b in range(0,201):
    slot = s + 10*b
    if slot <= 2000:
        b += 1
    else:
        break
    list1.append(slot)

            
print(list1)
    




