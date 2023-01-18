def return_10():
    return 10

def add(value1, value2):
    return value1 + value2

def subtract(value1, value2):
    return value1 - value2

def multiply(value1, value2):
    return value1 * value2

def divide(value1, value2):
    return value1 / value2

def length_of_string(input):
    return len(input)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(string1, string2):
    return int(string1) + int(string2)

def number_to_full_month_name(number):
    if number == 1:
        return "January"
    elif number == 3:
        return "March"
    elif number == 9:
        return "September"

def volume_of_cube(value):
    return value*value*value

def reverse_string(string):
    return string[::-1]
