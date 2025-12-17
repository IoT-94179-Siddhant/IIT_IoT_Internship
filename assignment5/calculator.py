#create the file calculator.py
#calculator.py
def add(a,b):
    """Return the addition of a and b"""
    return a+b

def subtract(a,b):
    """Return the subtraction of b from a"""
    return a-b

def multiply(a,b):
    """return the multiplication of a and b"""
    return a*b

def divide(a,b):
    """return the division of a by b"""
    if b==0:
        return"Error:Division by zero"
    return a/b

