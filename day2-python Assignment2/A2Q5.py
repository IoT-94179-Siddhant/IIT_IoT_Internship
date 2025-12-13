# Function to print a number in binary format
def print_binary(num):
    print("Binary representation:", bin(num)[2:])

# Accept number from the user
number = int(input("Enter a number: "))
print_binary(number)
