

from math_mod import add, subtract, multiply, divide
from string_mod import concatenate_strings, create_string_from_list, contains_digit

# Math operations
num1 = 4
num2 = 17

print(f"Result of adding {num1} and {num2} is {add(num1, num2)}")
print(f"Result of subtracting {num1} and {num2} is {subtract(num1, num2)}")
print(f"Result of multiplying {num1} and {num2} is {multiply(num1, num2)}")
print(f"Result of dividing {num1} by {num2} is {divide(num1, num2)}")

# String operations
str1 = "Hello"
str2 = "DCI"

print(f"Result of concatenation of '{str1}' and '{str2}' is {concatenate_strings(str1, str2)}")

string_list = ['Hello', 'DCI']
print(f"Result of creating string from list {string_list} is {create_string_from_list(string_list)}")

test_string = "HelloDCI007"
print(f"Result of checking digits in the string '{test_string}' is {contains_digit(test_string)}")
