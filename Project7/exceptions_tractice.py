def div(dev=5, d=0):
    try:
        return dev / d
    except ZeroDivisionError:
        print("Zero Division is prohibited!")
        return None


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        print("Index is out of bounds!")


def add_to_list_in_dict(thedict, listname, element):
    try:
        lol = thedict[listname]
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    else:
        print("%s already has %d elements." % (listname, len(lol)))
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))


div(5, 1)
div()
print_list_element(["a", "b", "c"], 3)
test_dict = {"a": [1, 2, 3, 4], "b": [10, 20, 30]}
add_to_list_in_dict(test_dict, "c", 100)
add_to_list_in_dict(test_dict, "a", 5)
