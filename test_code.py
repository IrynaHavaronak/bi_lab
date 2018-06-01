
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

