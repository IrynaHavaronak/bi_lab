class Room(object):
    """A simple example"""

    def __init__(self, number, accommodate,
                 price, engaged=False, rooms_num=1, bathroom=1):
        self.number = number
        self.accommodate = accommodate
        self.bathroom = bathroom
        self.rooms_num = rooms_num
        self.engaged = engaged
        self.price = price

    def __str__(self):
        if self.engaged:
            engaged_str = "engaged"
        else:
            engaged_str = "empty"
        return "Room number {:d}:\n" \
               "    accommodates {:d} guests\n" \
               "    has {:d} bathrooms\n" \
               "    has {:d} bedrooms\n" \
               "    costs {:d} dollars\n" \
               "    now it is {:s}".format(self.number, self.accommodate,
                                           self.bathroom, self.rooms_num,
                                           self.price, engaged_str)

    def to_list(self):
        ret = list()
        ret.append(self.number)
        ret.append(self.accommodate)
        ret.append(self.price)
        ret.append(self.bathroom)
        ret.append(self.rooms_num)
        ret.append(self.engaged)
        return list(ret)

    def __cmp__(self, x):
        first = self.to_list()[1:]
        second = x.to_list()[1:]
        if first == second:
            return True
        else:
            return False

    def change_engaged(self):
        self.engaged = not self.engaged

    def is_engaged(self):
        return self.engaged

    def tax(self):
        return self.price * 0.10


room101 = Room(101, 2, 105)
room102 = Room(102, 3, 105)
print(room101)
print("Does room 101 equal to room 102: ", room101 == room102)
print("Taxes for room 101: ", room101.tax())
