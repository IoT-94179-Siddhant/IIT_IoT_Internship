#to find factorial
def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial(num))

#to find power X^n
def power(x, n):
    if n == 0:            # Base case
        return 1
    else:
        return x * power(x, n - 1)


base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Power =", power(base, exponent))
