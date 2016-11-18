from librip.gen import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 3,3,3, 2, 2, 2]
data2 = gen_random(1, 3, 10)

# Реализация задания 2
print(list(Unique(data1)))
print(list(Unique(data2)))
data = ['a', 'A', 'b', 'B']
print(list(Unique(data)))
data = ['a', 'A', 'B', 'b']
print(list(Unique(data, ignore_case=True)))
