def generate_numbers(n=20):
    dict1 = {}
    for i in range(1, n + 1):
        dict1.update({i: i ** 2})
    return dict1


def count_characters(count_me_string):
    count_me_list = list(count_me_string)
    dict1 = {}
    for i in count_me_list:
        if i not in dict1.keys():
            dict1.update({i: count_me_list.count(i)})
    return dict1


print(generate_numbers())
print(generate_numbers(4))
print(count_characters("abcdefabcdfe"))
