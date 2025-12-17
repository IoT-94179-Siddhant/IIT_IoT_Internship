# operations/__init__.py
# (can be empty or used to expose functions)

#main program
from arithmetic import add, multiply
from string import reverse_string, count_vowels

# Arithmetic operations
a, b = 10, 5
print("Addition:", add(a, b))
print("Multiplication:", multiply(a, b))

# String operations
text = "Hello Python"
print("Reversed String:", reverse_string(text))
print("Vowel Count:", count_vowels(text))
