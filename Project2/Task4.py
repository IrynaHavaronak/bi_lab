# A left rotation operation on an array of size n
# shifts each of the array's elements 1 unit to the left. For example, if
# 2 left rotations are performed on array [1,2,3,4,5],
# then the array would become [3,4,5,1,2].
#
# Given an array of n integers and a number, d. Perform d
# left rotations on the array. Then print the updated array
# as a single line of space-separated integers.


check = True
while check:
    nd = input("Insert n and d values separated by space: ").split(" ")
    if int(nd[0]) <= int(nd[1]):
        check = True
        print("Input data correctly: d should be less than n!")
    else:
        check = False
array = input("Input array: ").split(" ")
new_array = []
i = 1
j = 0
nd[0], nd[1] = [int(nd[0]) - 1, int(nd[1])]
while i <= nd[0] + 1:
    new_array.append(array[j + nd[1]])
    if nd[0] < (nd[1] + j + 1):
        j = - nd[1]
    else:
        j += 1
    i += 1
print(new_array)
