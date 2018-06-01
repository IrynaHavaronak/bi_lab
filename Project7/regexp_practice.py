import re


def find_email(check="irina@dom.ko, 1@gg.ss, @fdf, 4345@344.22"):
    print("Looking for emails string: " + check)
    return re.findall(r'[^\d\s]\w*@\w+\.\w+', check)


def length345(check='irina havaronak opo p 1235'):
    print("Looking for all three, four, five"
          " characters long words string: " + check)
    return re.findall(r'\w{3,5}', check)
    # return re.findall(r'[a-zA-Z]{3,5}', check)


def sep_num(check='4664 5454 5ggg p3gpo wrwr'):
    print("Looking for numbers string: " + check)
    return re.findall(r'\d+', check)


def replace(string="Irina Havaronal is a BI LAB student"):
    print("Initial string: " + string)
    print("Replacement whitespaces with an underscore: " +
          re.sub(r' ', r'_', string))
    print(" replace underscores with a whitespace" +
          re.sub(r'_', r' ', string))


print(find_email())
print(length345())
print(sep_num())
print(replace())
