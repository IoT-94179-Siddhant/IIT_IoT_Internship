def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Accept number of terms from the user
terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci(terms)
