import re

# 1 line: Output
print('Hello, world!')

# 2 lines: Input, assignment
name = input('What is your name?\n')
print("Hi, %s." % name)

# 3 lines: For loop, built-in enumerate function, new style formatting
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

# 4 lines: Fibonacci, tuple assignment
parents, babies = (1, 1)
while babies < 100:
    print(f'This generation has {babies} babies')
    parents, babies = (babies, parents + babies)

# 6 lines: Import, regular expressions

for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, 'is a valid US local phone number')
    else:
        print(test_string, 'rejected')
