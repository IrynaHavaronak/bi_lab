# Program  prints the numbers from 1 to 100, but for multiples of
# three print “Fizz” instead of the number and for multiples
# of five print “Buzz”.For numbers which are multiples of both
# three and five, print “FizzBuzz”.

num = 1
while num <= 100:
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
    num += 1
