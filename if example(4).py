from itertools import filterfalse

value = input('enter value: ')
if value.isalpha():
    print('{} is alphabet'.format(value))
if value.isdigit():
    print('{} is digit'.format(value))
if value.isalnum():
    print('{} is alphanumeric'.format(value))
if value.isalnum() == False and value.isdigit() == False and value.isalpha() == False:
    print('{} is special symbol'.format(value))
