from typing import List


def generate_numbers(n=20):
    dict1 = {}
    for i in range(1, n + 1):
        dict1.update({i: i ** 2})
    return dict1


def count_characters(count_me_string="ababplplp"):
    count_me_list = list(count_me_string)
    dict1 = {}
    for i in count_me_list:
        if i not in dict1.keys():
            dict1.update({i: count_me_list.count(i)})
    return dict1


def fizzbuzz(count=100):
    num = 1
    result_list = []
    while num <= count:
        if num % 15 == 0:
            result_list += ["FizzBuzz"]
        elif num % 5 == 0:
            result_list += ["Buzz"]
        elif num % 3 == 0:
            result_list += ["Fizz"]
        else:
            result_list += [num]
        num += 1
    return result_list


def is_palindrome(input_str="madam"):
    if input_str == input_str[::-1]:
        checker = True
    else:
        checker = False
    return checker


def happy_numbers(n=100):
    past = set()
    result = [1]
    end_cycle = False
    for i in range(2, n+1):
        num = i
        while not end_cycle:
            num = sum(int(j)**2 for j in str(num))
            if num in past:
                end_cycle = True
            past.add(num)
            if num == 1:
                result.append(i)
                end_cycle = True
        past.clear()
        end_cycle = False
    return result
