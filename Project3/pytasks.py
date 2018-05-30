
def generate_numbers(n=20):
    return {i: i**2 for i in range(1, n + 1)}


def count_characters(count_str="irina havaronak"):
    return {i: count_str.count(i) for i in count_str}


def fizzbuzz(count=100):
    result_list = []
    for num in range(1, count + 1):
        if num % 15 == 0:
            result_list += ["FizzBuzz"]
        elif num % 5 == 0:
            result_list += ["Buzz"]
        elif num % 3 == 0:
            result_list += ["Fizz"]
        else:
            result_list += [num]
    return result_list


def is_palindrome(input_str="madam"):
    return input_str == input_str[::-1]


def happy_numbers(n=100):
    past = set()
    result = [1]
    for i in range(2, n + 1):
        num = i
        while True:
            num = sum(int(j) ** 2 for j in str(num))
            if num in past:
                break
            past.add(num)
            if num == 1:
                result.append(i)
        past.clear()
    return result
