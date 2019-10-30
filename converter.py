__author__ = 'Tontsu'

class Converter:

    def __init__(self, string):
        self.dec = 0
        self.string = string
        self.roman_numerals = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

    def convert(self):
        prev = ""
        for char in self.string:
            self.dec += self.roman_numerals.get(char, 0)
            if self.roman_numerals.get(char, 0) > self.roman_numerals.get(prev, 0):
                self.dec -= self.roman_numerals.get(prev, 0)*2
            prev = char

    def get_dec(self):
        return(self.dec)