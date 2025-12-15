#input string
s = "Programming"

#1.basic slicing
print(s[0:5])   # Progr
print(s[3:8])   # gramma

#2.slicing from start
print(s[:6])    # Progra

#3.slicing till end
print(s[4:])    # ramming

#4.negative index slicing
print(s[-5:])   # ming
print(s[-8:-3]) # rammi

#5.slicing with step
print(s[0:11:2])  # Pormig
print(s[::3])     # Pgmig

#6.reverse a string
print(s[::-1])   # gnimmargorP

#7.copy a string
copy = s[:]
print(copy)      # Programming

#8.revome first and last character
print(s[1:-1])   # rogrammin
