# A program checks whether a string is palindrome or Not.
# Before checking it asks do you prefer to input and check a string
# or check default strings.
quit_var = False
while not quit_var:
    choice = input("If you want input string press 1 \n"
                   "If you want check default strings pres any other button\n")
    if choice == "1":
        input_str = input("Please, input string\n")
        if input_str[::1] == input_str[::-1]:
            print("\""+input_str+"\" "+"is palindrome\n")
        else:
            print("\""+input_str+"\" "+"is not palindrome\n")
    else:
        for i in ["String", "refer", "Madam", "Iryna", "type"]:
            if i[::1] == i[::-1]:
                print("\"" + i + "\" " + "is palindrome\n")
            else:
                print("\"" + i + "\" " + "is not palindrome\n")
    choice_quit = input("If you want to quit press \"q\" and any other if you don't\n")
    if choice_quit == "q":
        quit_var = True
