#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    sum = 0
    for i in new_list:
        sum += i
    return sum
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
