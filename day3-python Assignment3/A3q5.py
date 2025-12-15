#1.default parameter values
def greet(name, message="wakeup"):
    print(message, name)

greet("Sid")                 # Uses default value
greet("Sid", "Hello")        # Overrides default value

#2.keyword arguments
def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_info(age=22, course="Python", name="Siddhantdev311")

#3.passing a function to another function
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(operation, x, y):
    return operation(x, y)

print("Addition:", calculate(add, 10, 5))
print("Subtraction:", calculate(subtract, 10, 5))
