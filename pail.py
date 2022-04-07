from itertools import combinations,permutations
roads = {'r1', 'r2', 'r3', 'r4', 'r5'}
cars = {'c1','c2','c3','c4'}
max_car = 3
def combine(road, data, n):
    ret = list(combinations(data, n))
    new_ret = []
    if not ret:
        return [f'{road} None']
    if not ret[0]:
        return [f'{road} None']
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
        
result = []
for possibility in list(permutations(cadidate, len(roads))):
    
    check_road = []
    check_car = []
    
    for each in possibility:
        road = each.split(' ')[0]
        car = each.split(' ')[1:]
        check_road.append(road)
        check_car.extend(car)
    check_car = [each for each in check_car if each != 'None']

        
    
    if len(check_road) != len(set(check_road)):
        continue
    if len(check_car) != len(set(check_car)):
        continue
    if len(set(check_car)) != len(cars):
        continue
    result.append(possibility)
for each in result:
    print(each)