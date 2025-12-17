#import python math
import math
#commonly used math functions
#1.square root
math.sqrt(16) #4.0
#2.power
math.pow(2,3) #8.0
#3.floor & ceil
math.floor(3.9) #3
math.ceil(4.1) #5
#4.factorial
math.factorial(3) #6
#5.trignometric functions (in radians)
math.sin(math.pi/2) #1
math.cos(0) #1
math.tan(math.pi/4) #1
#6.logarithmic functions
math.log(10) #natural log
math.log10(100) #2.0
#7.constants
math.pi #3.14
math.e #2.71


#import os module
import os
#commonly used functions
#1.current working directory
os.getcwd()
#2.list files in directory
os.listdir()
#3.change directory
os.chdir("C:\Users\shree\Desktop\python_programming")
#4.create & remove directory
os.mkdir("test")
os.rmdir("test")
#5.check file&directory exists
os.path.exists("file.txt")
os.path.isfile("file.txt")
os.path.isdir("test")
#6.rename file
os.rename("od.txt","new.txt")
#7.environment variables
os.environ
#8.run system command
os.system("dir") #windows
os.system("ls") #linux/mac

#main program (example using both modules)
import math
import os
print("square root of 25:",math.sqrt(25))
print("factorialof 3:",math.factorial(3))
print("value of PI:",math.pi)

print("\nCurrent Directory:",os.getcwd())
print("Files in directory:",os.listdir())
