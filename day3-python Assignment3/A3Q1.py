#1.case conversion method
s = "Hello World"
print(s.upper())      # HELLO WORLD
print(s.lower())      # hello world
print(s.title())      # Hello World
print(s.capitalize()) # Hello world
print(s.swapcase())   # hELLO wORLD

#2.checking/testing method
s = "Python123"
print(s.isalpha())    # False
print(s.isdigit())    # False
print(s.isalnum())    # True
print(s.islower())    # False
print(s.isupper())    # False
print(s.isspace())    # False

#3.searching and finding method
s = "hello python"
print(s.find("python"))   # 6
print(s.index("hello"))   # 0
print(s.count("o"))       # 2
print(s.startswith("he")) # True
print(s.endswith("on"))   # True

#4.replace & modify method
s = "Gayatri is my friend"
print(s.replace("Gayatri", "Sakshi"))  # Sakshi is my friend

#5.splitting and joining method
s = "apple,banana,orange"
words = s.split(",")
print(words)  # ['apple', 'banana', 'orange']
print("-".join(words))  # apple-banana-orange

#6.removing spaces
s = "  Hello  "
print(s.strip())   # "Hello"
print(s.lstrip())  # "Hello  "
print(s.rstrip())  # "  Hello"

#7.formatting strings
name = "Siddhant"
age = 22
print("My name is {} and I recently turned {} years old".format(name, age))

#8.length & indexing
s = "Python"
print(len(s))   # 6
print(s[0])     # P
print(s[-1])    # n
