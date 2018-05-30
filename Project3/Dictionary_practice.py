def generate_numbers(n=20):
    return {i: i**2 for i in range(1, n + 1)}


def count_characters(count_str):
    return {i: count_str.count(i) for i in count_str}


print(generate_numbers())
print(generate_numbers(4))
print(count_characters("abcdefabcdfe"))
