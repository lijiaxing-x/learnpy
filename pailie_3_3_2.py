from itertools import combinations,permutations

roads = {'x', 'y'}
cars = {'1', '2'}
max_car = 2
def combine(road, data, n):
    ret = list(combinations(data, n))
    new_ret = []
    if not ret:
        return [f'{road} 0']
    if not ret[0]:
        return [f'{road} 0']
    for each in ret:
        each = list(each)
        each.insert(0, road)
        new_ret.append(' '.join(each))
    return new_ret
cadidate = {}
cadidate = []
for road in roads:
    for j in range(0, max_car+1):
        cadidate.extend(combine(road, cars, j))
        
results = []
for possibility in list(permutations(cadidate, len(roads))):
    
    check_road = []
    check_car = []
    
    for each in possibility:
        road = each.split(' ')[0]
        car = each.split(' ')[1:]
        check_road.append(road)
        check_car.extend(car)
    check_car = [each for each in check_car if each != '0']

        
    
    if len(check_road) != len(set(check_road)):
        continue
    if len(check_car) != len(set(check_car)):
        continue
    if len(set(check_car)) != len(cars):
        continue
    results.append(possibility)
for each in results:
    print(each)

print(len(results))

for result in results:
    for element in result:
        element.lstrip()
        


'''
for i in range(results.count(' ')):
    results.remove(' ')
    print(results)
'''