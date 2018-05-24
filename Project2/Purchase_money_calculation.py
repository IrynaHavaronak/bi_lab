# a program calculates total cost. One item costs M dollars and N cents.
# Customer bought L items. Print total price in dollars and cents for L items
dollars = int(input("Put dollars:  "))
cents = int(input("Put cents: "))
items = int(input("Put items: "))
dollars = dollars * items + cents * items // 100
cents = cents * items % 100
print("Total cost: %d dollar(s) and %d cent(s)" % (dollars, cents))
