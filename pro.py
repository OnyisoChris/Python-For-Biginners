print("   /|")
print("  / |")
print(" /  |")
print("/___|")

number = "20"
name = "Chris"
print("My name is "+ name + " and am " + number + " years old")

#strings
print("Learn Python")
print("Learn\nPython")
print("Learn\"Python")
print("Learn\Python")

#variable and Datatypes
phrase = "Learn Python"
print(phrase + " is the best")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())

print(len(phrase))
print(phrase[11])
print(phrase.index("P"))
print(phrase.index("Python"))
print(phrase.replace("Python", "Programming"))

#Numbers
num = 7
print(3440.99930)
print(5 + 8.022 - 2)
print(12 % 5)
print(str(num) + " is my lucky number")

#functions
from math import *
num = -8
print(abs(num))
print(pow(4, 3))
print(max(7, 8))
print(min(3, 6))
print(round(5.5))
print(floor(4.9))
print(ceil(4.9))
print(sqrt(49))

#Input from users
name = input("Enter your name: ")
age = input("Enter you age: ")
print("Hello " + name + "! You are " + age)

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)