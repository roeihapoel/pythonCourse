''' Exercise #8. Python for Engineers.'''

class Minibar:
    def __init__(self, drinks, snacks):
        pass

    def __repr__(self):
        pass

    def eat(self, snack):
        pass

    def drink(self, drink):
        pass

#########################################
# Question 2 - do not delete this comment
#########################################
class RoomError(Exception):
    #A subclass of Exception that defines a new error type
    #DO NOT change this class
    pass

class Room:
    def __init__(self, minibar, floor, number, guests, clean_level, is_suite, satisfaction=0.5):
        pass # replace this with your implementation
    
    def __repr__(self):
        pass # replace this with your implementation

    def is_occupied(self):
        pass # replace this with your implementation

    def clean(self):
        pass # replace this with your implementation

    def better_than(self, other):
        pass # replace this with your implementation

    def check_in(self, guests):
        pass # replace this with your implementation

    def check_out(self):
        pass # replace this with your implementation
    
    def move_to(self, other):
        pass # replace this with your implementation
   
#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        pass # replace this with your implementation
            
    def __repr__(self):
        pass # replace this with your implementation
                      
    def check_in(self, guests, is_suite):
        pass # replace this with your implementation

    def check_out(self, guest):
        pass # replace this with your implementation

    def upgrade(self, guest):
        pass # replace this with your implementation

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
        pass
    
    
    def __str__(self):
        pass


    def __repr__(self):
        pass


    def __neg__(self):
        pass


    def __add__(self, other):
        pass


    def __lt__(self, other):
        pass
    
    
    def __gt__(self, other):
        pass
    

    def __floordiv__(self, other):
        pass


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