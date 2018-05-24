# a program calculates total cost. One item costs M dollars and N cents.
# Customer bought L items. Print total price in dollars and cents for L items
import re
input_str = input("Input data:  ")
num = re.split(r"[^\d]+",  input_str)
print("Total cost: " + str(int(num[1])+int(num[2])*int(num[1])//3)
      + " dollar(s) " + str(int(num[2])*3 % 100) + " cent(s)")


# one item price is 3 dollars 20 cents, calculate price for 3 items

