from turtle import position
from unittest import result
import numpy
'''
num_list = [1, 1, 2, 3, 4, 5, 4, 5, 3, 2]
def permute(nums):
    from itertools import permutations
    result = []
    for i in permutations(nums, len(nums)):
        result.append(list(i))
    
    return result

print('\n')
#print(permute(num_list))
print(len(permute(num_list)))

'''
n1 = [1, 2, 3]
n2 = [1, 4, 5]

t = numpy.indices(n1, n2)