__author__ = 'Tontsu'

import converter
import re

validation_regex = "^(?=[MDCLXVI])M*(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
roman_numeral = input("Enter roman numeral: ")

if re.search(validation_regex, roman_numeral.upper()):
    converter = converter.Converter(roman_numeral.upper())
    converter.convert()
    print(converter.get_dec())
else:
    print("Invalid roman numeral")