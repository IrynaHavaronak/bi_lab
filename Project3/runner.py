import pytasks
import sys


def runner(*args):
    if len(args) == 0:
        print(pytasks.generate_numbers())
        print(pytasks.count_characters())
        print(pytasks.fizzbuzz())
        print(pytasks.is_palindrome())
        print(pytasks.count_characters())
    for str1 in args:
        if str1 == "generate_numbers":
            print(pytasks.generate_numbers())
        elif str1 == "count_characters":
            print(pytasks.count_characters())
        elif str1 == "fizzbuzz":
            print(pytasks.fizzbuzz())
        elif str1 == "is_palindrome":
            print(pytasks.is_palindrome())
        elif str1 == "count_characters":
            print(pytasks.count_characters())
        elif str1 == "happy_numbers":
            print(pytasks.happy_numbers())


if __name__ == "__main__":
    arguments = sys.argv[2:]
    runner(*arguments)
