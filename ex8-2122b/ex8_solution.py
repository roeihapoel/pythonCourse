''' Exercise #8. Python for Engineers.'''

class Minibar:
    def __init__(self, drinks, snacks):
        self.drinks = drinks
        self.snacks = snacks
        self.bill = 0

    def __repr__(self):
        if self.bill > 0:
            return "Drinks – ({}). Snacks – ({}). Bill - {}.".format(", ".join(list(self.drinks.keys())),
                                                                     ", ".join(list(self.snacks.keys())), self.bill)
        else:
            return "Drinks – ({}). Snacks – ({}). No bill yet.".format(", ".join(list(self.drinks.keys())),
                                                                       ", ".join(list(self.snacks.keys())))

    def eat(self, snack):
        try:
            self.bill += self.snacks.pop(snack)
        except Exception as e:
            raise ValueError("The snack {} was not found".format(snack))

    def drink(self, drink):
        try:
            self.bill += self.drinks.pop(drink)
        except Exception as e:
            raise ValueError("The drink {} was not found".format(drink))

#########################################
# Question 2 - do not delete this comment
#########################################
class RoomError(Exception):
    #A subclass of Exception that defines a new error type
    #DO NOT change this class
    pass

class Room:
    def __init__(self, minibar, floor, number, guests, clean_level, is_suite, satisfaction=0.5):
        for guest in guests:
            if not isinstance(guest, str):
                raise TypeError("Type error of guests argument.")
        if not isinstance(clean_level, int) or not isinstance(is_suite, (bool, int)) or not isinstance(satisfaction, (float, int)):
            raise TypeError("Type error of at least one of the arguemnts")
        if clean_level < 1 or clean_level > 15:
            raise TypeError("Type error of clean level argument.")
        if satisfaction > 1 or satisfaction <0:
            raise TypeError("Type error of satisfaction argument.")

        self.guests = [guest.lower() for guest in guests]
        self.minibar = minibar
        self.floor = floor
        self.number = number
        self.clean_level = clean_level
        self.is_suite = is_suite
        self.satisfaction = satisfaction


    def __repr__(self):

        if len(self.guests) > 0:
            guests_text = (", ").join(self.guests)
        else:
            guests_text ="empty"

        attibutes = ["Minibar: " + repr(self.minibar)
                     ,"Floor: " +  str(self.floor) + "."
                     ,"Number: " + str(self.number) + "."
                     ,"Guests: " + guests_text + "."
                     ,"Clean level: " + str(self.clean_level)+ "."
                     ,"Is suite: " + str(self.is_suite)+ "."
                     ,"Satisfaction: " + str(round(self.satisfaction,2))+ "."]
        text = "\n".join(attibutes)
        return text



    def is_occupied(self):
        return len(self.guests) > 0

    def clean(self):
        self.clean_level = min(15, self.clean_level + 1 + int(self.is_suite))

    def better_than(self, other):
        if not isinstance(other, Room):
            raise TypeError("Other must be an instance of Room")
        if (self.is_suite, self.clean_level, self.floor) > (other.is_suite, other.clean_level, other.floor):
            return True
        else:
            return False



    def check_in(self, guests):
        if not self.guests:
            self.guests = [guest.lower() for guest in guests]
            self.satisfaction = 0.5
        else:
            raise RoomError("Can’t check-in new guests to an occupied room")

    def check_out(self):
        if self.guests:
            self.guests = []
        else:
            raise RoomError("Cannot check-out an empty room")

    def move_to(self, other):
        if not self.guests:
            raise RoomError("Cannot move guests from an empty room")
        if other.guests:
            raise RoomError("Can’t move guests into an occupied room")

        other.guests= self.guests
        self.guests = []
        if other.better_than(self):
            other.satisfaction = min(1.0, self.satisfaction + 0.05)
        else:
            other.satisfaction = self.satisfaction

   
#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

    def __repr__(self):
        occupied_length = len([room for room in self.rooms if room.is_occupied()])
        return """{} Hotel has: {}/{} occupied rooms.""".format(self.name, occupied_length , str(len(self.rooms)))

    def check_in(self, guests, is_suite):

        for room in list(reversed(self.rooms)):
            if not room.is_occupied() and room.is_suite == is_suite:
                room.check_in(guests)
                return room
        return None

    def check_out(self, guest):
        for room in self.rooms:
            if guest.lower() in room.guests:
                room.check_out()
                return room
        return None

    def upgrade(self, guest):

        current_room = None
        for room in self.rooms:
            if guest.lower() in room.guests:
                current_room = room
                break
        if current_room is None:
            return None
        for room in self.rooms:
            try:
                if room.better_than(current_room):
                    current_room.move_to(room)
                    return room
            except Exception as e:
                pass
        return None

#########################################
# Question 4 - do not delete this comment
#########################################

class Roman():
    
    def get_int_from_roman(self):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_string = self.roman_value.strip('-')
        int_val = 0
        for counter in range(len(roman_string)):
            if counter > 0 and rom_val[roman_string[counter]] > rom_val[roman_string[counter - 1]]:
                int_val += rom_val[roman_string[counter]] - 2 * rom_val[roman_string[counter - 1]]
            else:
                int_val += rom_val[roman_string[counter]]
        int_val = -int_val if self.is_neg else int_val
        return int_val
    
    def get_roman_from_int(self):
        num = self.int_value if not self.is_neg else -self.int_value
        roman_num = '' if not self.is_neg else '-'
        counter = 0
        
        roman_char = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        int_vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        while num > 0:
            for _ in range(num // int_vals[counter]):
                roman_num += roman_char[counter]
                num -= int_vals[counter]
            counter += 1
        return roman_num
    
    def __init__(self, input_value):
        if isinstance(input_value, int):
            self.is_neg = input_value < 0
            self.int_value = input_value
            self.roman_value = self.get_roman_from_int()

        else:
            self.is_neg = input_value.startswith("-")
            self.roman_value = input_value
            self.int_value = self.get_int_from_roman()


    def __str__(self):
        return self.roman_value

    def __repr__(self):
        return "int: {}; Roman Numeral: '{}'".format(str(self.int_value), self.roman_value)

    def __neg__(self):
        return Roman(-self.int_value)

    def __add__(self, other):
        if isinstance(other, int):
            int_value =  self.int_value + other
        else:
            int_value = self.int_value + other.int_value
        if int_value == 0:
            raise ValueError("Can't represent 0 with roman numerals")
        return Roman(int_value)

    def __lt__(self, other):
        if isinstance(other, int):
            return self.int_value < other
        else:
            return self.int_value < other.int_value
    
    def __gt__(self, other):
        if isinstance(other, int):
            return self.int_value > other
        else:
            return self.int_value > other.int_value

    def __floordiv__(self, other):
        if isinstance(other, int):
            int_value = self.int_value // other
        else:
            int_value = self.int_value // other.int_value
        if int_value == 0:
            raise ValueError("Can't represent 0 with roman numerals")
        return Roman(int_value)




if __name__ == '__main__':

      if __name__ == "__main__":

        def test_hotel():
                m = Minibar({'coke': 10, 'lemonade': 7}, {'bamba': 8, 'mars': 12})
                rooms = [Room(m, 15, 140, [], 5, True),
                         Room(m, 12, 101, ["Ronen", "Shir"], 6, True),
                         Room(m, 1, 2, ["Liat"], 7, False), Room(m, 2, 23, [], 6, True)]
                h = Hotel("Dan", rooms)
                test_sep = '\n------------------'
                print('PRINT h:\n', h, test_sep, sep="")
                print(m)
                print('PRINT h:\n', h, test_sep, sep="")
                print('CALL: h.upgrade("Liat")\n', h.upgrade("Liat"), test_sep, sep="")
                print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep,
                      sep="")
                print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep,
                      sep="")
                print('CALL: h.check_in(["Alice", "Wonder"], True)\n',
                      h.check_in(["Alice", "Wonder"], True), test_sep, sep="")
                print('CALL: h.check_in(["Alex"], True)\n', h.check_in(["Alex"], True), test_sep,
                      sep="")
                print('PRINT h:\n', h, test_sep, sep="")
                print('CALL: h.check_in(["Oded", "Shani"], False)\n',
                      h.check_in(["Oded", "Shani"], False), test_sep, sep="")
                print('CALL: h.check_in(["Oded", "Shani"], False)\n',
                      h.check_in(["Oded", "Shani"], False), test_sep, sep="")
                print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
                print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
                print('PRINT h:\n', h, test_sep, sep="")


        test_hotel() ## After you are done implementing all classes and methods, you may comment-in the call to test_hotel() and compare the results with the file test_hotel_output.txt


      print('==== Q4: Basic tests/output====')
      r2=Roman(2)
      print(Roman(2))
      print(str(r2))
      print(repr(r2))
      print('====')
      print(-Roman("IV"))
      print('====')
      r5 = Roman(2) + 3
      print(r5)
      print(str(r5))
      print(repr(r5))
      print(repr(Roman(6) // -5))