list1 = ['a', 'b', 'c']
tuple1 = tuple(list1)
print(tuple1)
list2 = list(tuple1)
print(list2)
tuple3 = ('a', 2, 'gamma')
a, b, c = tuple3
tuple4 = (list1,)
print(tuple4)

print(c)