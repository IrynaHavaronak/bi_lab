list1 = [i + j for i in 'ab' for j in 'bcd']
print(list1)
list2 = list1[::2]
list3 = [str(i) + 'a' for i in range(1, 5)]
list3.remove('2a')
print(list3)
list3_copy = list3 + ['2a']
print(list3_copy)
